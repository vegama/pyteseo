
<p align="center">
<img align="center" width="600" src="docs/_static/pyTESEO_logo.png">
</p>


![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/IHCantabria/pyteseo?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/IHCantabria/pyteseo?style=plastic)
![GitHub](https://img.shields.io/github/license/IHCantabria/pyteseo?style=plastic)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to centralize and standarize python modules to manage TESEO model I/O, config, plot...
Examples of the use of each functionality is provided through a set of notebooks


---

## :house: Local installation

* Install from github repositorie using `pip`:
```bash
pip install git+https://github.com/IHCantabria/pyteseo
# To install extra dev dependencies: pip install git+https://github.com/IHCantabria/pyteseo[dev]
# Using editable mode: pip install -e git+https://github.com/IHCantabria/pyteseo[dev]

```

* :warning: `UNDER CONSTRUCTION` :construction: - Installation from github repository using pip:
```bash
pip install pyteseo
```
* :warning: `UNDER CONSTRUCTION` :construction: - Install from conda-forge repositories:
```bash
conda install -c conda-forge pyteseo 
```

---

## :recycle: Continuous integration (CI)

:warning: `THINK AND DEVELOP!` (If able use precommit and github actions when push tags)
* pass format -> Balck
* pass linter
* pass tests -> pytest
* make documentation -> sphinx

*For all the SO, and python versions required!*

---

## :heavy_check_mark: Testing & Covergae
Tests are located at `tests/` and data required for tests should be located in `data/mock/`.

Run tests to verify your package installation:
```bash
pyteseo-test            # Run tests and prompt pytest-report
```
Also, you can run coverage assesment and generate html report:
```bash
pyteseo-coverage        # Run coverage and prompt coverage-report
pyteseo-coverage-html   # Run coverage and bluid coverage-html-report
```
Tests have been developed using [pytest](https://docs.pytest.org/).


---

## :copyright: Credits
Developed and maintained by :man_technologist: [German Aragon](https://github.com/aragong) @ :office: [IHCantabria](https://github.com/IHCantabria).

---