"""Input and Output functionality for specific TESEO file formats
"""

import pandas as pd
from pathlib import PosixPath

# 1. DOMAIN
def read_grid(path: str|PosixPath, nan_value:int|float=-999) -> pd.DataFrame:
    """Read TESEO grid-file and load it in a pandas DataFrame

    Args:
        path (str | PosixPath): path to the grid-file
        nan_value (float | int, optional): value to set nans. Defaults to -999.

    Returns:
        pd.DataFrame: _description_
    """

    df = pd.read_csv(path, names=["lon", "lat", "depth"], delimiter="\s+", na_values=nan_value)
    
    if df.shape[1] != 3:
        raise ValueError("TESEO grid-file should contains lon, lat and depth values only!")
    
    if df.lon.max()>=180 or df.lon.min()<=-180 or df.lon.max()>=90 or df.lon.min()<=-90:
        raise ValueError("lon and lat values in TESEO grid-file should be inside -180<=>180 and -90<=>90!")
    
    if not all(df.get(["lon", "lat"]) == df.sort_values(["lon", "lat"]).get(["lon", "lat"])):
        raise ValueError("lon and lat values in TESEO grid-file should be monotonic increasing!")
    
    return df


def write_grid(df:pd.DataFrame, path:str|PosixPath, nan_value:int|float=-999) -> None:
    """Write TESEO grid-file

    Args:
        df (pd.DataFrame): DataFrame with columns 'lon', 'lat', 'depth' (lon:[-180,180], lat:[-90,90])
        path (str | PosixPath): path of the new grid-file
        nan_value (int | float, optional): define how will be writted nan values in the grid-file. Defaults to -999.
    """    
    
    if "lon" not in df.keys().values or "lat" not in df.keys().values or "depth" not in df.keys().values:
        raise ValueError("variable names in DataFrame should be 'lon', 'lat' and 'depth'!")

    if df.shape[1] != 3:
        raise ValueError("DataFrame should contains column variables lon, lat and depth only!")
    
    if df.lon.max()>=180 or df.lon.min()<=-180 or df.lon.max()>=90 or df.lon.min()<=-90:
        raise ValueError("lon and lat values in DataFrame should be inside -180<=>180 and -90<=>90!")
    
    if not all(df.get(["lon", "lat"]) == df.sort_values(["lon", "lat"]).get(["lon", "lat"])):
        df = df.sort_values(["lon", "lat"])
    
    df.to_csv(path, sep="\t", na_rep=nan_value, header=False, index=False)



def read_coastline(path):
    print("doing something...")
    # return df

def write_coastline(dir_path):
    print("doing something...")



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
