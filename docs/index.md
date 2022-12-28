
```{error}
This project is under heavy development. Documentation is also under construction!

```

# pyTESEO
pyTESEO is a Python package to setup [TESEO](https://ihcantabria.com/en/specialized-software/teseo/), lagrangian model developed by [IHCantabria](https://ihcantabria.com/en/)
```{image} _static/pyTESEO_logo.png
:width: 400px
:align: center
```
---
PyTESEO is a python package developed to help users to setup TESEO's simulations. The package includes a bunch of use case examples in jupyter notebook format under the folder `notebooks` and a bunch of python functions grouped by submodules under the folder {py:mod}`pyteseo`. The package uses mainly numpy, pandas, matplotlib and xarray packages to manage and plot data. Based on these functions, the user can read and write all the necessary files to run a TESEO simulation, plot default figures of the results and export results to standard formats as CSV, JSON, netCDF, GeoJSON...

---
```{image} _static/TESEO_logo.png
:width: 300px
:align: right
```
TESEO is a lagrangian numerical model developed by IHCantabria. The model allows to calculate trajectories of particles based on metocean conditions like ocean currents, winds and waves. It also includes weathering submodels to evaluate the degradation and physical characteristics of oil and hns substances. Implementation of a marine litter submodel is under development!

The soruce code of the model is located in this [github repository](https://github.com/IHCantabria/TESEO)

---

```{toctree}
:caption: CONTENTS

get-started.md
user-guide.md
changelog.md
autoapi/index.rst
```

```{toctree}
:caption: USE CASES
:titlesonly:
:numbered:
:glob: 

notebooks/*
```

