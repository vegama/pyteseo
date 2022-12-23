from pyteseo.io import read_grid, write_grid, read_coastline, write_coastline
import pandas as pd
from pathlib import Path
import pytest


base_path = Path("./data/mock")
tmp_path = Path("./tmp")



@pytest.mark.parametrize("file, error", [("grid.dat", None), ("not_existent_file.dat","not_exist"), ("grid_badformat1.dat", "bad_format"), ("grid_badformat2.dat", "bad_format"), ("grid_badformat3.dat", "bad_format")])
def test_read_grid(file, error):

    path = Path(base_path, file)
    
    if error == "not_exist":
        with pytest.raises(FileNotFoundError) as err:
            df = read_grid(path, nan_value=-9999)
            print(err.value)

    elif error == "bad_format":
        with pytest.raises(ValueError) as err:
            df = read_grid(path, nan_value=-9999)
            print(err.value)
    else:
        df = read_grid(path, nan_value=-9999)
        assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize("error", [(None), ("df_n_var"), ("df_varnames"), ("lonlat_range"), ("sorting")])
def test_write_grid(error):
    
    if not tmp_path.exists():
        tmp_path.mkdir()

    grid_path = Path(base_path, "grid.dat")
    output_path = Path(tmp_path, "test_grid.dat")

    df = read_grid(path=grid_path, nan_value=-9999)

    if error == "df_n_var":
        df["var"] = 123
        with pytest.raises(ValueError) as err:
            write_grid(df=df, path=output_path, nan_value=-999)
            print(err.value)

    elif error == "df_varnames":
        df = df.rename(columns={"lon":"longitude"})
        with pytest.raises(ValueError) as err:
            write_grid(df=df, path=output_path, nan_value=-999)
            print(err.value)

    elif error == "lonlat_range":
        df["lon"][0] = 360
        with pytest.raises(ValueError) as err:
            write_grid(df=df, path=output_path, nan_value=-999)
            print(err.value)
    
    elif error == "sorting":
        df["lat"][0] == 90
        df["lat"][1] == 89
        
        write_grid(df=df, path=output_path, nan_value=-999)
        newdf = read_grid(path=output_path)
        output_path.unlink()
        output_path.parent.rmdir()
        assert all(newdf.get(["lon","lat"]) == df.get(["lon","lat"])) and all(df[df.get("depth").notna()] == newdf[newdf.get("depth").notna()])
    
    else:

        write_grid(df=df, path=output_path, nan_value=-999)
        newdf = read_grid(path=output_path)
        output_path.unlink()
        output_path.parent.rmdir()
        assert all(newdf.get(["lon","lat"]) == df.get(["lon","lat"])) and all(df[df.get("depth").notna()] == newdf[newdf.get("depth").notna()])


def test_read_coastline():
    assert True

def test_write_coastline():
    assert True