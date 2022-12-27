# pyTESEO
![pyTESEO_logo](img/pyTESEO_logo.png)
![GitHub top language](https://img.shields.io/github/languages/top/IHCantabria/pyteseo?style=plastic)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/IHCantabria/pyteseo?label=latest%20tag&style=plastic)
![GitHub repo size](https://img.shields.io/github/repo-size/IHCantabria/pyteseo?style=plastic)
![GitHub](https://img.shields.io/github/license/IHCantabria/pyteseo?style=plastic)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to centralize and standarize python modules to manage TESEO model I/O, config, plot...
Examples of the use of each functionality is provided through a set of notebooks

Link to [Kanban panel](https://tasks.office.com/unican.onmicrosoft.com/Home/PlanViews/77hd5AVHEEeYOvNXygI2j5YAAfJE?Type=PlanLink&Channel=Link&CreatedTime=638073235719140000)

---

## :house: Local installation
Installation from github repository using pip:
```bash
pip install git+https://github.com/IHCantabria/pytest
```
Install from conda-forge repositories:
```bash
conda install -c conda-forge pyteseo 
```

Install from pypi repositories:
```bash
pip install pyteseo
```
---


## :recycle: Continuous integration (CI)
* Pre-commit with **black formatter** hook on `commit`. ([.pre-commit-config.yaml](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.pre-commit-config.yaml))
* Github workflow with conda based **deployment** and **testing** on `tag`. ([Github action](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.github/workflows/main.yml))
* Test and update coverage badge **manually** through vscode [task](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.vscode/tasks.json): `run test and coverage`
---

## :heavy_check_mark: Testing
* To run tests manually:
```bash
# Unzip data for testing stored in "data.zip" in "tests/" folder
7z x tests/data.zip -otests/ 

# Run pytests from console
pytest
```
* **Update coverage badge manually** through vscode task `run test and coverage` or running:
```bash
pytest --cov=./
coverage-badge -o coverage.svg -f
```
---

<!-- ## :rocket: Package deployment
Check [DEPLOY_REQUIREMENTS.md](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/DEPLOY_REQUIREMENTS.md) for a full detailed explanation. 
--- -->

## :copyright: Credits
Developed and maintained by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).

---