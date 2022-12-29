from pyteseo.io import (
    read_grid,
    write_grid,
    read_coastline,
    write_coastline,
    _split_df_between_nans,
)
import pandas as pd
from pathlib import Path
import pytest

base_path = Path("./data/mock")
tmp_path = Path("./tmp")


@pytest.mark.parametrize(
    "file, error",
    [
        ("grid.dat", None),
        ("not_existent_file.dat", "not_exist"),
        ("grid_badformat1.dat", "bad_format"),
        ("grid_badformat2.dat", "bad_format"),
        ("grid_badformat3.dat", "bad_format"),
    ],
)
def test_read_grid(file, error):

    path = Path(base_path, file)

    if error == "not_exist":
        with pytest.raises(FileNotFoundError):
            df = read_grid(path, nan_value=-9999)
    elif error == "bad_format":
        with pytest.raises(ValueError):
            df = read_grid(path, nan_value=-9999)
    else:
        df = read_grid(path, nan_value=-9999)
        assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "error", [(None), ("df_n_var"), ("df_varnames"), ("lonlat_range"), ("sorting")]
)
def test_write_grid(error):
    if not tmp_path.exists():
        tmp_path.mkdir()

    grid_path = Path(base_path, "grid.dat")
    output_path = Path(tmp_path, "test_grid.dat")

    df = read_grid(path=grid_path, nan_value=-9999)

    if error == "df_n_var":
        df["var"] = 123
        with pytest.raises(ValueError):
            write_grid(df=df, path=output_path, nan_value=-999)

    elif error == "df_varnames":
        df = df.rename(columns={"lon": "longitude"})
        with pytest.raises(ValueError):
            write_grid(df=df, path=output_path, nan_value=-999)

    elif error == "lonlat_range":
        df["lon"][0] = 360
        with pytest.raises(ValueError):
            write_grid(df=df, path=output_path, nan_value=-999)

    elif error == "sorting":
        df["lat"][0] == 90
        df["lat"][1] == 89

        write_grid(df=df, path=output_path, nan_value=-999)
        newdf = read_grid(path=output_path)
        output_path.unlink()
        output_path.parent.rmdir()
        assert all(newdf.get(["lon", "lat"]) == df.get(["lon", "lat"])) and all(
            df[df.get("depth").notna()] == newdf[newdf.get("depth").notna()]
        )

    else:
        write_grid(df=df, path=output_path, nan_value=-999)
        newdf = read_grid(path=output_path)
        output_path.unlink()
        output_path.parent.rmdir()
        assert all(newdf.get(["lon", "lat"]) == df.get(["lon", "lat"])) and all(
            df[df.get("depth").notna()] == newdf[newdf.get("depth").notna()]
        )


@pytest.mark.parametrize(
    "file, error",
    [
        ("coastline.dat", None),
        ("not_existent_file.dat", "not_exist"),
        ("coastline_badformat.dat", "bad_format"),
        ("grid.dat", "bad_format"),
    ],
)
def test_read_coastline(file, error):

    path = Path(base_path, file)

    if error == "not_exist":
        with pytest.raises(FileNotFoundError):
            df = read_coastline(path)
    elif error == "bad_format":
        with pytest.raises(ValueError):
            df = read_coastline(path)
    else:
        df = read_coastline(path)
        assert isinstance(df, pd.DataFrame)
        assert not df.empty


@pytest.mark.parametrize(
    "error", [(None), ("df_n_var"), ("df_varnames"), ("lonlat_range")]
)
def test_write_coastline(error):
    if not tmp_path.exists():
        tmp_path.mkdir()

    coastline_path = Path(base_path, "coastline.dat")
    output_path = Path(tmp_path, "test_coastline.dat")

    df = read_coastline(path=coastline_path)

    if error == "df_n_var":
        df["var"] = 123
        with pytest.raises(ValueError):
            write_coastline(df=df, path=output_path)

    elif error == "df_varnames":
        df = df.rename(columns={"lon": "longitude"})
        with pytest.raises(ValueError):
            write_coastline(df=df, path=output_path)

    elif error == "lonlat_range":
        df["lon"][0] = 360
        with pytest.raises(ValueError):
            write_coastline(df=df, path=output_path)

    else:
        write_coastline(df=df, path=output_path)
        newdf = read_coastline(path=output_path)

        output_path.unlink()
        output_path.parent.rmdir()

        assert all(newdf.get(["lon", "lat"]) == df.get(["lon", "lat"]))

    if tmp_path.exists():
        tmp_path.rmdir()


@pytest.mark.parametrize(
    "filename", [("coastline.dat"), ("coastline_othernanformat.dat")]
)
def test_split_df_between_nans(filename):

    coastline_path = Path(base_path, filename)
    df = read_coastline(coastline_path)

    polygons = _split_df_between_nans(df)

    assert isinstance(polygons, list)
    assert len(polygons) == 3

    for item in polygons:
        assert isinstance(item, pd.DataFrame)
        assert len(item.index) != 0
