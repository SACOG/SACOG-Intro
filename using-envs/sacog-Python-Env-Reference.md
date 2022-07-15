# SACOG Python Environment Reference



## Who this guide is for

This guide is primarily aimed at SACOG staff who have ArcGIS Pro installed along with an ESRI license to run python modules such as arcpy.

If the above doesn't describe you, or if you don't have access to ESRI modules, *and* you're not already set up with a python package management system (like conda), we recommend you still use conda as your package management system.

## Contents

1. What is an environment?
2. [Setting up your python environment](#Setting-up-your-python-environment)
    * Commonly-used python packages for SACOG tasks
3. [Troubleshooting](#Troubleshooting)
    * Issues importing arcpy module

## What is an environment?
[FreeCodeCamp](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) gives a good intro as to why you need python environments, and in so doing also gives a good sense of what they are.

## Setting up your python environment
[Conda](https://docs.conda.io/en/latest/) is a great package manager and is the system that ArcGIS Pro uses to manage all of the python practices we at SACOG are likely to use for our many data analysis tasks. 

### Most common conda commands (Using ArcGIS Pro's Python Command Prompt)
Below are some of the most common conda commands. For a full list of common conda commands, check out [conda's cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

NOTE that these commands use windows syntax. For Mac OS or Linux please refer to conda documentation.

List out conda environments (the starred environment is your current environment)

`conda env list`




Switch to a different environment

`activate <env name>`



Create a new, empty conda environment

`conda create --name <env name>`




Create a new conda environment as a clone of a conda environment

`conda create --clone <env you want to clone> --name <name of clone env>`



List out installed packages in current environment

`conda list`




Install new python package

`conda install <package name>`




### More resources for conda environment and package management

*  If you're at SACOG and installed ArcGIS Pro on your machine, you should start with [ESRI's documentation on using conda and package management](https://developers.arcgis.com/python/guide/understanding-conda/)
*  For more details on Conda beyond ESRI's intro to it, check out the [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)



### Commonly-used python packages for SACOG tasks
The table below lists packages we commonly use for data analysis that are not part of the standard set of packages that comes with ESRI's default conda environment.

| Package Name       | Distribution | Description and Notes                                        |
| ------------------ | ------------ | ------------------------------------------------------------ |
| dbfread            | conda        | Converting DBF to CSV and pandas df                          |
| sqlalchemy         | conda        | Run SQL Server commands--needed for exporting pandas df to SQL table |
| swifter            | pip          | Speeds up pandas df.apply() tasks                            |
| plotly             | conda        | Visualization                                                |
| geopandas          | conda        | Open source tool that converts GeoJSON and SHPs to pandas-like dataframes with geometry attribute |
| python-orca        | conda        | Needed to export plotly charts as static images (PNG, etc)   |
| fuzzywuzzy         | pip          | Fuzzy string similarity measurement--measures how similar two strings are |
| python-levenshtein | pip          | Speeds up fuzzywuzzy for large data sets. Requires C++ be installed. Can be downloaded through https://visualstudio.microsoft.com/downloads/ |
| statsmodels        | conda        | Needed for doing statistical analyses of plotly charts (e.g. adding trendlines) |
| fastparquet        | conda        | Required for reading/writing parquet files with pandas.      |
| pyarrow            | conda        | Needed if you want to export big pandas dfs to parquet format using snappy compression |
| python-snappy      | conda        | Needed if you want to export big pandas dfs to parquet format using snappy compression |
| jupyterlab         | conda        | Improved, latest (as of Dec 2021) way to load, edit, and interact with python notebooks (.ipynb files) |





## Troubleshooting

### Cannot load arcpy module
If you can successfully load most other python modules but not the arcpy module trying to `import arcpy` (e.g., you get an `ImportError`), it often means that you recently updated ArcGIS Pro and the only way to correct this issue is to make a new clone of the ESRI default environment (as of March 2021, the default environment is named arcgispro-py3). To do this:

1. Make a clone of the default environment
2. Install any dependencies you needed in the old environment you used
3. This new environment you created should now be able to import arcpy. If it does work, then consider it to be your new working environment.

