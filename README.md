# Terrario

An auxiliary tool for terraform

## Install

Make sure you have the `build` module in your system by running `pip install build` and then run `python -m build` followed by

`pip install .`

or, in case you don't want to rerun the command for every update:

`pip install --editable .`

## Commands

- `terrario init`: Create a new base structure for terraform project
- `terrario validate`: Validate the configuration of all (or selected) envs in a terraform project
- `terrario prune`: Removes all the `.terraform` files from all projects in the current dir

