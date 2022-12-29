
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

* Install from pypi repositories as any other dependecy:
```bash
pip install git+https://github.com/IHCantabria/pyteseo
```
* Clone repository and install with pip from repository root directory:
```bash
git clone git+https://github.com/IHCantabria/pyteseo

cd pyteseo

pip install .
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

:warning: `THINK AND REBUILD!` (If able use precommit and github actions when push tags)
* pass format -> Balck
* pass linter
* pass tests -> pytest
* make documentation -> sphinx

*For all the SO, and python versions required!*

---

## :heavy_check_mark: Testing & Covergae
Run tests to verify your package installation:

```python
import pyteseo
pyteseo.tests()

# CLI: pytest pyteseo" or "coverage run -m pytest pyteseo" to update '.coverage'
```

Additionally, tests are located at `tests/` folder and use data located at `data/mock/` folder.
Tests have been developed using [pytest](https://docs.pytest.org/).

To see coverage report:
```python
import pyteseo
pyteseo.coverage()

# CLI: "coverage report"
```
---

## :copyright: Credits
Developed and maintained by :man_technologist: [German Aragon](https://github.com/aragong) @ :office: [IHCantabria](https://github.com/IHCantabria).

---