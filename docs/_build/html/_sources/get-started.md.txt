# Get started
Quickstart guide to use pyTESEO

---

## Installation
```{note}
For now, this package can only be installed directly from github repository. Will be published on pypi and conda-forge soon with the first stable release!
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

## Package structure
* {py:mod}`pyteseo.io` - Bunch of functions to read and write all the necesary files for a TESEO simulation.
* {py:mod}`pyteseo.config` - Bunch of functions to obtain configuration variables to write TESEO's configuration files (*.cfg and *.run)
* {py:mod}`pyteseo.plot` - Bunch of functions to plot default figures of all the results calculated by TESEO model.
* {py:mod}`pyteseo.export` - Bunch of functions to export TESEO results to standard formats (*.csv, *.json, *.geojson, *.nc)

---

## Testing and coverage
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

## Use cases
Some use cases have been developed as an examples of use of this package.
All the use cases are provided as notebooks (*.ipynb) in the source code repository under the path `docs/notebooks`. Moreover, all the notebooks include a link to be opened and executed in `Google Colab`.

Check **USE CASES** section at left panel to access them.

---

## Continuous integration
* deploy documentation on github page -> github action
* pass format -> Balck?
* pass linter -> ?
* pass tests -> pytest
* make documentation -> sphinx
* install and pass tests in different systems -> github actions

*For all the SO (Windows, Linux, Mac), and python versions (3.10) required!*
