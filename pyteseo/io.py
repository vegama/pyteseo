"""Input and Output functionality for specific TESEO file formats
"""

import pandas as pd
from pathlib import Path, PosixPath

# 1. DOMAIN
def read_grid(path: str | PosixPath, nan_value: int | float = -999) -> pd.DataFrame:
    """Read TESEO grid-file and load it in a pandas DataFrame

    Args:
        path (str | PosixPath): path to the grid-file
        nan_value (float | int, optional): value to set nans. Defaults to -999.

    Returns:
        pd.DataFrame: DataFrame with TESEO's grid data [lon, lat, depth]
    """

    df = pd.read_csv(path, delimiter="\s+", na_values=nan_value, header=None)

    if df.shape[1] != 3:
        raise ValueError(
            "TESEO grid-file should contains lon, lat and depth values only!"
        )

    df.columns = ["lon", "lat", "depth"]
    if (
        df.lon.max() >= 180
        or df.lon.min() <= -180
        or df.lon.max() >= 90
        or df.lon.min() <= -90
    ):
        raise ValueError(
            "lon and lat values in TESEO grid-file should be inside ranges lon[-180,180] and lat[-90,90]!"
        )

    if not all(
        df.get(["lon", "lat"]) == df.sort_values(["lon", "lat"]).get(["lon", "lat"])
    ):
        raise ValueError(
            "lon and lat values in TESEO grid-file should be monotonic increasing!"
        )

    return df


def read_coastline(path: str | PosixPath) -> pd.DataFrame:
    """Read TESEO coastline-file and load it in a pandas DataFrame

    Args:
        path (str | PosixPath): path to the coastline-file

    Returns:
        pd.DataFrame: DataFrame with TESEO's coastline data [lon, lat]
    """
    df = pd.read_csv(path, delimiter="\s+", header=None)
    if df.shape[1] != 2:
        raise ValueError("TESEO coastline-file should contains lon, lat values only!")

    df.columns = ["lon", "lat"]
    if (
        df.lon.max() >= 180
        or df.lon.min() <= -180
        or df.lat.max() >= 90
        or df.lat.min() <= -90
    ):
        raise ValueError(
            "lon and lat values in TESEO grid-file should be inside ranges lon[-180,180] and lat[-90,90]!"
        )

    return df


def write_grid(
    df: pd.DataFrame, path: str | PosixPath, nan_value: int | float = -999
) -> None:
    """Write TESEO grid-file

    Args:
        df (pd.DataFrame): DataFrame with columns 'lon', 'lat', 'depth' (lon:[-180,180], lat:[-90,90])
        path (str | PosixPath): path of the new grid-file
        nan_value (int | float, optional): define how will be writted nan values in the grid-file. Defaults to -999.
    """

    if (
        "lon" not in df.keys().values
        or "lat" not in df.keys().values
        or "depth" not in df.keys().values
    ):
        raise ValueError(
            "variable names in DataFrame should be 'lon', 'lat' and 'depth'!"
        )

    if df.shape[1] != 3:
        raise ValueError(
            "DataFrame should contains column variables lon, lat and depth only!"
        )

    if (
        df.lon.max() >= 180
        or df.lon.min() <= -180
        or df.lat.max() >= 90
        or df.lat.min() <= -90
    ):
        raise ValueError(
            "lon and lat values should be inside ranges lon[-180,180] and lat[-90,90]!"
        )

    if not all(
        df.get(["lon", "lat"]) == df.sort_values(["lon", "lat"]).get(["lon", "lat"])
    ):
        df = df.sort_values(["lon", "lat"])

    df.to_csv(path, sep="\t", na_rep=nan_value, header=False, index=False)



def _split_df_between_nans(df:pd.DataFrame) -> list[pd.DataFrame]:
    """Split DataFrame between nan values and return a list of new DataFrames

    Args:
        df (pd.DataFrame): input DataFrame with nans

    Returns:
        list: ouput splitted DataFrames without nan values
    """    
    splitted_dfs=[]
    previous_i = count = 0
    n_nans = len(df[df.isna().any(axis=1)])
    
    for i in df[df.isna().any(axis=1)].index.values:
        count += 1
        if i==0:
            continue
            
        if i == df.iloc[[-1]].index.values:
            break
        elif count == n_nans:
            splitted_dfs.append(df.iloc[previous_i:])
        else:
            splitted_dfs.append(df.iloc[previous_i:i])
            previous_i=i

    if splitted_dfs[0].equals(df):
        print("WARNING - There is nothing to split in this DataFrame!")

    return splitted_dfs



def write_coastline(df: pd.DataFrame, path: PosixPath) -> None:


    
    def _write_polygons(df: pd.DataFrame, dir_path: PosixPath, filename="coastline_polygon") -> None:

        # TODO - escribir archivos de polygonos

        polygons = _split_df_between_nans(df)
        del df

        for i, df in enumerate(polygons):
            path_polygon = Path(dir_path, f"{filename}_{i:03d}.dat")
            df.to_csv(path_polygon, sep="\t", header=False, index=False, na_rep="NaN")


    if "lon" not in df.keys().values or "lat" not in df.keys().values:
        raise ValueError("variable names in DataFrame should be 'lon' and 'lat'!")

    if df.shape[1] != 2:
        raise ValueError("DataFrame should contains column variables lon and lat only!")

    if (
        df.lon.max() >= 180
        or df.lon.min() <= -180
        or df.lat.max() >= 90
        or df.lat.min() <= -90
    ):
        raise ValueError(
            "lon and lat values should be inside ranges lon[-180,180] and lat[-90,90]!"
        )

    df.to_csv(path, sep="\t", header=False, index=False, na_rep="NaN")
    _write_polygons(df, path.parent)


# 2. FORCINGS
def read_currents(path_list):
    print("doing something...")
    # return df


def write_currents(dir_path):
    print("doing something...")


def read_winds(path_list):
    print("doing something...")
    # return df


def write_winds(dir_path):
    print("doing something...")


def read_waves(path_list):
    print("doing something...")
    # return df


def write_waves(dir_path):
    print("doing something...")


def read_currents_depth_avg(path_list):
    print("doing something...")
    # return df


def write_currents_depth_avg(dir_path):
    print("doing something...")


# 3. CONFIGURATION
def write_cfg(dir_path):
    print("doing something...")


def read_cfg(path):
    print("doing something...")


def write_run(dir_path):
    print("doing something...")


def read_run(path):
    print("doing something...")


# 4. RESULTS
def read_particles(path_list):
    print("doing something...")
    # return df


def read_properties(path_list):
    print("doing something...")
    # return df


def read_grids(path_list):
    print("doing something...")
    # return df
