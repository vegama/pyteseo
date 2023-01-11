## :warning: Package under development!
## :soon: First usable version (v1.0.0) will be released soon!
---

<p align="center">
<img align="center" width="600" src="https://ihcantabria.github.io/pyteseo/_images/pyTESEO_logo.png">
</p>


[![Github release (latest by date)](https://img.shields.io/github/v/release/ihcantabria/pyteseo?label=last%20release)](https://github.com/IHCantabria/pyteseo/releases)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/IHCantabria/pyteseo?label=last%20tag)](https://github.com/IHCantabria/pyteseo/tags)
[![GitHub last commit](https://img.shields.io/github/last-commit/ihcantabria/pyteseo)](https://github.com/IHCantabria/pyteseo/commits/main)
[![docs](https://img.shields.io/github/deployments/ihcantabria/pyteseo/deploy-docs?label=deploy-docs)](https://ihcantabria.github.io/pyteseo)
[![GitHub license](https://img.shields.io/github/license/IHCantabria/pyteseo)](https://github.com/IHCantabria/pyteseo/blob/main/LICENSE.md)
[![GitHub repo size](https://img.shields.io/github/repo-size/IHCantabria/pyteseo)](https://github.com/IHCantabria/pyteseo)
[![GitHub file count](https://img.shields.io/github/directory-file-count/IHCantabria/pyteseo)](https://github.com/IHCantabria/pyteseo)
[![GitHub file count](https://img.shields.io/github/languages/count/IHCantabria/pyteseo)](https://github.com/IHCantabria/pyteseo)
[![GitHub file count](https://img.shields.io/github/languages/top/IHCantabria/pyteseo)](https://github.com/IHCantabria/pyteseo)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)



**pyTESEO** is a python package developed by [IHCantabria](https://ihcantabria.com/en/) to simplify and facilitate the setup and processing of [TESEO](https://ihcantabria.com/en/specialized-software/teseo/) simulations *(TESEO is a lagrangian numerical model also developed by IHCantabria.)*


---

## :computer: Installation

From github repositorie using `pip`:
```bash
pip install git+https://github.com/IHCantabria/pyteseo
# To install extra dev dependencies: pip install git+https://github.com/IHCantabria/pyteseo[dev]
# Using editable mode: pip install -e git+https://github.com/IHCantabria/pyteseo[dev]

```

:warning: `UNDER DEVELOPMENT` :construction: - From pypi:
```bash
pip install pyteseo
```
:warning: `UNDER DEVELOPMENT` :construction: - From conda-forge:
```bash
conda install -c conda-forge pyteseo 
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

## :recycle: Continuous integration (CI)

:warning: `UNDER DEVELOPMENT` :construction:
* deploy documentation on github page -> github action :heavy_check_mark:
* pass format -> Balck :x:
* pass linter -> ? :x:
* pass tests -> pytest :x:
* make documentation -> sphinx :x:
* install and pass tests in different systems -> github actions :x:

*For all the SO (Windows, Linux, Mac), and python versions (3.10) required!*

---

## :books: Documentation

Comprenhensive documentation is developed and mantained at https://ihcantabria.github.io/pyteseo

Documentation of all the package, usage and examples based on mockup input data are provided in [Jupyter Notebooks](https://jupyter.org/) format and ready to be used under [Google Colab](https://colab.research.google.com/) online platform.


![pyteseo_doc](docs/_static/doc_snapshoot.png)

---

## :copyright: Credits
Developed and maintained by :man_technologist: [German Aragon](https://github.com/aragong) @ :office: [IHCantabria](https://github.com/IHCantabria).

---