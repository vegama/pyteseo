# Get started
Quickstart guide to use pyTESEO

## :computer: Installation
```{note}
For now, this package can only be installed directly from github repository through pip!
This can be done also from a conda environment, but always using pip.
```
Directly from `github`:
```bash
pip install git+https://github.com/IHCantabria/pyteseo
```
from `pypi` repository:
```bash
pip install pyteseo
```
---
## :heavy_check_mark: Testing & Coverage
Tests are located in `pyteseo/tests/` and data required for tests are located in `pyteseo/tests/data/`. 
Tests have been developed using [pytest](https://docs.pytest.org/).

Run tests to verify your package installation:
```bash
pyteseo-test        # Run tests and prompt pytest-report
```

If you have cloned the repository, you also can run `coverage.py` functionalities based on current `pytproyect.toml` configuration from your terminal command line interface:
```bash
# Commands should be executed from the root directory of the repo

coverage run        # For run tests and generate ".coverage" file
coverage report     # For prompt results from ".coverage" file
coverage html       # For generate html report on "htmlcov" folder
```


---

## :recycle: Continuous integration and deployment (CI & CD)

:warning: `THINK AND DEVELOP!` (If able use precommit and github actions when push tags)
* deploy documentation on github page -> github action :heavy_check_mark:
* pass format -> Balck :x:
* pass linter -> ? :x:
* pass tests -> pytest :x:
* make documentation -> sphinx :x:
* install and pass tests in different systems -> github actions :x:

*For all the SO (Windows, Linux, Mac), and python versions (3.10) required!*

---


## :house: Structure
1. {py:mod}`pyteseo.io` - Bunch of functions to read and write all the necesary files for a TESEO simulation.
2. {py:mod}`pyteseo.config` - Bunch of functions to obtain configuration variables to write TESEO's configuration files (*.cfg and *.run)
3. {py:mod}`pyteseo.plot` - Bunch of functions to plot default figures of all the results calculated by TESEO model
4. {py:mod}`pyteseo.export` - Bunch of functions to export TESEO results to standard formats (*.csv, *.json, *.geojson, *.nc)

## :rocket: Use Cases
List of use cases developed as a guide to use this package
```{warning}
Link to notebooks, To be completed!
```

