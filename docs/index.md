
```{error}
This project is under heavy development. Documentation is also under construction!

```

# pyTESEO
pyTESEO is a Python package to setup [TESEO](https://ihcantabria.com/en/specialized-software/teseo/), lagrangian model developed by [IHCantabria](https://ihcantabria.com/en/)
```{image} ../img/pyTESEO_logo.png
:width: 400px
:align: center
```
---
PyTESEO is a python package developed to help users to setup TESEO's simulations. The package includes a bunch of use case examples in jupyter notebook format under the folder `notebooks`. The group of submodules provided is located under the folder `pyteseo`.

1. `io.py` - Bunch of functions to read and write all the necesary files for a TESEO simulation.
2. `config.py` - Bunch of functions to obtain configuration variables to write TESEO's configuration files (*.cfg and *.run)
3. `plot.py` - Bunch of functions to plot default figures of all the results calculated by TESEO model
4. `export.py` - Bunch of functions to export TESEO results to standard formats (*.csv, *.json, *.geojson, *.nc)
---
```{image} ../img/TESEO_logo.png
:width: 300px
:align: right
```
TESEO is a lagrangian numerical model developed by IHCantabria. The model allows to calculate trajectories of particles based on metocean conditions like ocean currents, winds and waves. It also includes weathering submodels to evaluate the degradation and physical characteristics of oil and hns substances. Implementation of a marine litter submodel is under development!

The soruce code of the model is located in this [github repository](https://github.com/IHCantabria/TESEO)

---
## Get started
### Installation
To install pyTESEO use:
```{code-block}
---
emphasize-lines: 1
---
$ pip install git+ssh://git@github.com/IHCantabria/pyteseo
```
### Use Cases
```{warning}
Link to notebooks!

```

---

## User Guide
You can use pyTESEO to generate TESEO simulation's files, obtain configuration variables, plot default figures of the results and export results to standard formats.

### Create domain files
TESEO model uses a grid of the computational domain where the depth of the water cells are defined as positive values. As default land values are defined as -999. To write this file you can use the function {py:func}`pyteseo.io.write_grid`. Also you can use the function {py:func}`pyteseo.io.read_grid` to read this file and load it into a pandas DataFrame.

TESEO domain files can be ploted using {py:func}`pyteseo.plot.plot_grid` and {py:func}`pyteseo.plot.plot_coastline`.

### Create forcing files

### Get forcing configuration variables

### Create Configuration files

### Export reults to standard formats
Bla bla bla

---

## CHANGELOG
Bla bla bla

---

## API Reference
```{toctree}
```
