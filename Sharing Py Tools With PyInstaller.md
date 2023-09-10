# Packaging and sharing tools with PyInstaller
Example packaging of python application into .exe file so you can share it with
others to run and they don't need to worry about dependencies or python environments.

More details and installation instructions at https://pyinstaller.org/en/stable/index.html

## Basic Usage
Generally, go to the quickstart guide on the pyinstaller website

## Things to be aware of
* pyinstaller will package up all python dependencies, but will *not* automatically package up data files and config files that your app may need (e.g., a YAML file, a spec/parameter CSV, etc.). You must manually copy these files into the resulting bundle folder after pyinstaller has done all its work.