
"""Input and Output functionality for specific TESEO file formats
"""
from __future__ import annotations

from pathlib import Path, PosixPath
from typing import Tuple

import pandas as pd

# NOTE - Restricts the loading when from "pyteseo.io import *"" to the names defined here but it are loaded in pytest.CHECK BEHAVIOUR
# NOTE - Restricts what is documented by Sphinx (!!!)
__all__ = [
    "read_grid",
    "read_coastline",
    "write_grid",
    "write_coastline",
    "read_currents",
    "read_winds",
    "write_currents",
    "write_winds",
]


# 1. DOMAIN
def read_grid(path: str | PosixPath, nan_value: int | float = -999) -> pd.DataFrame:
    """Read TESEO grid-file to pandas DataFrame

    Args:
        path (str | PosixPath): path to the grid-file
        nan_value (float | int, optional): value to set nans. Defaults to -999.

    Returns:
        pd.DataFrame: DataFrame with TESEO grid data [lon, lat, depth]
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
    """Read TESEO coastline-file to pandas DataFrame

    Args:
        path (str | PosixPath): path to the coastline-file

    Returns:
        pd.DataFrame: DataFrame with TESEO coastline data [lon, lat]
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

    return _split_polygons(df)


def write_grid(
    df: pd.DataFrame, path: str | PosixPath, nan_value: int | float = -999
) -> None:
    """Write TESEO grid-file

    Args:
        df (pd.DataFrame): DataFrame with columns 'lon', 'lat', 'depth' (lon:[-180,180], lat:[-90,90])
        path (str | PosixPath): path to the new grid-file
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

    df.to_csv(
        path, sep="\t", na_rep=nan_value, header=False, index=False, float_format="%.8e"
    )


def write_coastline(df: pd.DataFrame, path: str | PosixPath) -> None:
    """Write TESEO coastline and polygons files

    Args:
        df (pd.DataFrame): DataFrame with columns 'lon', 'lat' and polygons separated by nan lines (lon:[-180,180], lat:[-90,90])
        path (str | PosixPath): path to the new coastline-file
    """

    def _write_polygons(
        df: pd.DataFrame, dir_path: str | PosixPath, filename: str = "coastline_polygon"
    ) -> None:
        """Write polygons from a coastline DataFrame

        Args:
            df (pd.DataFrame): input coastline DataFrame
            dir_path (str | PosixPath): directory where polygon files will be created
            filename (str, optional): filename for polygon-files (numbering and extension will be added). Defaults to "coastline_polygon".
        """
        grouped = df.groupby("polygon")

        for polygon, group in grouped:
            path_polygon = Path(dir_path, f"{filename}_{polygon:03d}.dat")
            group.to_csv(
                path_polygon,
                sep="\t",
                header=False,
                index=False,
                float_format="%.8e",
                na_rep="NaN",
            )

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

    df.to_csv(
        path, sep="\t", header=False, index=False, float_format="%.8e", na_rep="NaN"
    )
    _write_polygons(df, path.parent)


# 2. FORCINGS
def read_currents(path: str | PosixPath) -> Tuple[pd.DataFrame, float, float]:
    """Read TESEO currents-files (2dh: [lon, lat, u, v])

    Args:
        path (str | PosixPath): path to TESEO lstcurr.pre file

    Returns:
        Tuple[pd.DataFrame, float, float]: DataFrame of currents, number of files (times), and number of nodes
    """
    with open(path, "r") as f:
        files = [Path(path.parent, line.rstrip()) for line in f]

    df_list = _read_2dh_uv(files)

    n_rows = list(set([len(df.index) for df in df_list]))

    if len(n_rows) != 1:
        raise ValueError("Number of lines in each file are not equal!")

    return pd.concat(df_list), len(files), n_rows[0]


def read_winds(path: str | PosixPath) -> Tuple[pd.DataFrame, float, float]:
    """Read TESEO winds-files (2dh: [lon, lat, u, v])

    Args:
        path (str | PosixPath): path to TESEO lstwinds.pre file

    Returns:
        Tuple[pd.DataFrame, float, float]: DataFrame of winds, number of files (times), and number of nodes
    """
    with open(path, "r") as f:
        files = [Path(path.parent, line.rstrip()) for line in f]

    df_list = _read_2dh_uv(files)

    n_rows = list(set([len(df.index) for df in df_list]))

    if len(n_rows) != 1:
        raise ValueError("Number of lines in each file are not equal!")

    return pd.concat(df_list), len(files), n_rows[0]


def write_currents(df: pd.DataFrame, dir_path: PosixPath | str) -> None:
    """Write TESEO currents-files from a DataFrame

    Args:
        df (pd.DataFrame): DataFrame containing columns "time", "lon", "lat", "u", and "v".
        dir_path (PosixPath | str): directory path where will be created the files "lstcurr_UVW.pre" and all the "currents_*.txt"
        nan_value (int, optional): Value for replacing nans. Defaults to 0.
    """

    lst_filename = "lstcurr_UVW.pre"
    forcing = "currents"
    path = Path(dir_path, lst_filename)
    
    _write_2dh_uv(df, path, forcing)


def write_winds(df: pd.DataFrame, dir_path: PosixPath | str) -> None:
    """Write TESEO winds-files from a DataFrame

    Args:
        df (pd.DataFrame): DataFrame containing columns "time", "lon", "lat", "u", and "v".
        dir_path (PosixPath | str): directory path where will be created the files "lstwinds.pre" and all the "winds_*.txt"
        nan_value (int, optional): Value for replacing nans. Defaults to 0.
    """
    lst_filename = "lstwinds.pre"
    forcing = "winds"
    path = Path(dir_path, lst_filename)

    _write_2dh_uv(df, path, forcing)


def _write_2dh_uv(df: pd.DataFrame, path: PosixPath | str, forcing: str, nan_value: int=0):
    
    path = Path(path) if isinstance(path, str) else path

    # Check variable-names
    for varname in ["time", "lon", "lat", "u", "v"]:
        if varname not in df.keys():
            raise ValueError(f"{varname} not founded in the DataFrame")

    if (
        df.lon.max() >= 180
        or df.lon.min() <= -180
        or df.lat.max() >= 90
        or df.lat.min() <= -90
    ):
        raise ValueError(
            "lon and lat values should be inside ranges lon[-180,180] and lat[-90,90]!"
        )

    df = df.sort_values(["time", "lon", "lat"])
    
    grouped = df.groupby("time")
    for time, group in grouped:
        with open(path,"a") as f:
            f.write(f"{forcing}_{int(time):03d}h.txt\n")
        
        path_currents = Path(path.parent, f"{forcing}_{int(time):03d}h.txt")
        group.to_csv(
            path_currents,
            sep="\t",
            columns=["lon", "lat", "u", "v"],
            header=False,
            index=False,
            float_format="%.8e",
            na_rep=nan_value,
        )


# def read_waves(path_list):
#     print("doing something...")


# def write_waves(dir_path):
#     print("doing something...")


# def read_currents_depth_avg(path_list):
#     print("doing something...")


# def write_currents_depth_avg(dir_path):
#     print("doing something...")


# # 3. CONFIGURATION
# def write_cfg(dir_path):
#     print("doing something...")


# def read_cfg(path):
#     print("doing something...")


# def write_run(dir_path):
#     print("doing something...")


# def read_run(path):
#     print("doing something...")


# # 4. RESULTS
# def read_particles(path_list):
#     print("doing something...")


# def read_properties(path_list):
#     print("doing something...")


# def read_grids(path_list):
#     print("doing something...")


def _split_polygons(df: pd.DataFrame) -> pd.DataFrame:
    """Split DataFrame between nan values

    Args:
        df (pd.DataFrame): input DataFrame with nans

    Returns:
        pd.DataFrame: DataFrame with polygon and point number as indexes
    """
    splitted_dfs = []
    previous_i = count = 0
    n_nans = len(df[df.isna().any(axis=1)])

    for i in df[df.isna().any(axis=1)].index.values:
        count += 1
        if i == 0:
            continue
        if count == n_nans:
            splitted_dfs.append(df.iloc[previous_i:i])
            if i == df.iloc[[-1]].index.values:
                break
            else:
                splitted_dfs.append(df.iloc[i:])
        else:
            splitted_dfs.append(df.iloc[previous_i:i])
            previous_i = i

    if splitted_dfs[0].equals(df):
        print("WARNING - There is nothing to split in this DataFrame!")

    new_polygons = []
    for i, polygon in enumerate(splitted_dfs):
        polygon.loc[:, ("polygon")] = i + 1
        polygon.loc[:, ("point")] = polygon.index
        polygon = polygon.set_index(["polygon", "point"])
        new_polygons.append(polygon)

    return pd.concat(new_polygons)


def _read_2dh_uv(files: list[PosixPath | str]) -> list[pd.DataFrame]:
    """Read TESEO's 2dh velocity field files used for currents and winds. column format [lon, lat, u, v]

    Args:
        files (list[PosixPath | str]): paths where velocity field files are located. (sorted list)

    Returns:
        list[pd.DataFrame]: list of DataFrames for each file (adding time field)
    """
    df_list = []
    for file in files:
        df = pd.read_csv(file, delimiter="\s+", header=None)

        if df.shape[1] != 4:
            raise ValueError(
                "DataFrame should contains column variables lon, lat, u, and v only!"
            )

        df.columns = ["lon", "lat", "u", "v"]

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
            raise ValueError("lon and lat values should be monotonic increasing!")

        df["time"] = float(file.stem[-4:-1])
        df_list.append(df)
    return df_list

