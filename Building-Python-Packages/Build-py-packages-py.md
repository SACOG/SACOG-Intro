# Building Python Packages for PIP- A Quick Guide

## Using this Guide

This guide assumes you:

* Are on a Windows machine (though most of these instructions are well-documented for OSX or Linux).
* Know basic commands in the command line.
* Are familiar with using python environments, including conda environments.

## Handy References

This quick guide is a distillation of the three links below. If you have never made a python package before, you should go through the links in the order listed below.

1. [ESRI guide for making a script or set of scripts into a package](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/extending-geoprocessing-through-python-modules.htm)

2. [ESRI guide for packaging and distributing a packable set of scripts](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/extending-geoprocessing-through-python-modules.htm)

3. [Python official guide for making packages (gives details and context not in the ESRI links)](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#requirements-for-packaging-and-distributing)

## Building a package

### Organize your scripts into a packageable structure

While there are various guides out there for organizing your script or set of scripts into a packageable format, [ESRI's guide for making a script or set of scripts into a package](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/extending-geoprocessing-through-python-modules.htm) is a good starting point. If you don't like ESRI's, you can google "how to build a python package from scratch" as a starting point.

### Write setup.py (or setup.cfg) and other metadata files

 [ESRI's python package distribution instructions](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#requirements-for-packaging-and-distributing) gives a good overview of what to include in a setup.py file. However, to get a complete overview of all of the parameters you can specify in the setup.py file, you should read the [official python documentation](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#requirements-for-packaging-and-distributing). One particularly important parameter is the  [`install requires`](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#requirements-for-packaging-and-distributing) variable, in which you list out all the dependencies your scripts use that are not part of the Python standard library.

The setup.py file is also an important place to update key information like the package name, your information, and to build a README file that gives instructions and notes to the user. It is also wise to specify a LICENSE to use so that others have permission to use your package and also protect yourself against any issues your script may have.

### Run setup.py 

As described in [ESRI's python package distribution instructions](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#requirements-for-packaging-and-distributing), run the following in a command prompt window:

`python setup.py sdist bdist_wheel`

This will create 3 folders respectively named "dist", "build", and a third with name ending in ".egg-info". These 3 folders will be created in the same directory as the setup.py script. The key file from this step will be the ["wheel" (.whl)](https://packaging.python.org/en/latest/glossary/#term-Wheel) file, which will be created within the "dist" folder. This is what you use to install a package into an environment.

## Install and share your package as a wheel file

As mentioned in the step for [running setup.py](#run-setup.py), running setup.py creates a ["wheel" (.whl)](https://packaging.python.org/en/latest/glossary/#term-Wheel) file in the "dist" folder.

After running setup.py, and you have the wheel and dist folders, you are ready to install your file or share your package with someone else.

### Installing from a wheel file

To add your package to a python environment (yes, you can do this with conda environments) do all of the following in the command line interface:

1. Ensure you are in the environment that you want to install the package into.
2. Navigate, in the command line interface using `cd`, to the folder containing the package's wheel file.
3. Run `pip install <name of your wheel file>.whl`. This should install the package and any dependencies you specified in [setup.py](#Run-setup.py).
4. Confirm that you can successfully import your package into a python script, and confirm that all modules were installed and work correctly.

### Sharing your package with others as a wheel

A simple way to internally share a package with others is to send them the wheel file and they can install it as described above. If you want to share it with the world, there are various resources to show you how to publish your package to PyPI--a good starting point is the [python documentation](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi).

Note, the wheel is the only file the recipient needs in order to install your package, but it would be good to also send them the .egg-info folder, which contains any README or other metadata files you created for the package.









