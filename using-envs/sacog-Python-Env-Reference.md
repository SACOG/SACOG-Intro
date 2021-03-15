# SACOG Python Environment Reference



## Who this guide is for

This guide is primarily aimed at SACOG staff who have ArcGIS Pro installed along with an ESRI license to run python modules such as arcpy.

If the above doesn't describe you, or if you don't have access to ESRI modules, *and* you're not already set up with a python package management system (like conda), we recommend you still use conda as your package management system.

## Contents

1. What is an environment?
2. Setting up your python environment (Please use Conda!)
    a. Commonly-used python packages for SACOG tasks
3. Common troubleshooting problems
    a. Issues importing arcpy module

## What is an environment?
[FreeCodeCamp](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) gives a good intro as to why you need python environments, and in so doing also gives a good sense of what they are.

## Setting up your python environment (Please use conda!)
[Conda](https://docs.conda.io/en/latest/) is a great package manager and is the system that ArcGIS Pro uses to manage all of the python practices we at SACOG are likely to use for our many data analysis tasks. 
*  If you're at SACOG and installed ArcGIS Pro on your machine, you should start with [ESRI's documentation on using conda and package management](https://developers.arcgis.com/python/guide/understanding-conda/)
*  [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)



### Commonly-used python packages for SACOG tasks
The table below lists packages we commonly use for data analysis that are not part of the standard set of packages that comes with ESRI's default conda environment.

| Package Name | Distribution | Description
|---------------------|---------------|-------------
| dbfread | conda | reads DBF files into pandas dataframe, CSV, etc.
| geopandas | conda | Allows pandas dataframes with geometry capabilities
| plotly | conda | Rich suite of visualization tools




## Troubleshooting
### Cannot load arcpy module
If you can successfully load most other python modules but not the arcpy module trying to import arcpy (e.g., you get an `ImportError`), it often means that you recently updated ArcGIS Pro and the only way to correct this issue is to make a new clone of the ESRI default environment (as of March 2021, the default environment is named arcgispro-py3). To do this:

1. Make a clone of the default environment
2. Install any dependencies you needed in the old environment you used
3. This new environment you created should now be able to import arcpy. If it does work, then consider it to be your new working environment.

