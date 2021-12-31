# Example Package using setup.cfg instead of setup.py

Using a setup.cfg is considered better practice than setting up a setup.py file

## Cliff note steps:

1. Make a pyproject.toml file per the [setuptools docs](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
2. Make sure all your source codes are nested like the diagram in [python's documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files)
3. In command prompt, navigate to package parent folder and run `python3 -m build`, which will create dist and egg-info files.
4. Navigate to the dist folder that was created
5. Make sure you're in the desired environment
6. In command prompt, run `pip install <full name of wheel file with .whl extension>`

# Resources for how to put packages together with setup.cfg

- [From python documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [setuptools documentation on setup.cfg](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)

# Gotchas

- Let's say you make a package named `my_pkg` and it contains a script named `my_functions`. If you did not specify to import `my_functions` in the `__init__.py` file, then if you use `my_pkg` in a script and want to use `my_functions`, you will need to import as `from my_pkg import my_functions` because it will not automatically import--to avoid this, you can specify to import it in the `__init__.py` file of `my_pkg`.
