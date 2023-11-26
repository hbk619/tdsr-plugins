# TDSR Plugins

This repo works with [TDSR](https://github.com/tspivey/tdsr) to allow for some easier terminal parsing
(currently a [pull request](https://github.com/tspivey/tdsr/pull/35))

## Setup

Clone this repo into TDSR (the below example assumes you have tdsr in your home directory)

`git clone https://github.com/hbk619/tdsr-plugins ~/tdsr/plugins/hbk619`

### Pytest

If you would like to use pytest and have feedback as "3 errors. Module not found. 
Code is import blah" configure TDSR in the plugins section as below

```
hbk619.pytest_parser = p
```

If you would like to make parsing slightly faster and have a consistent command to run pytest
you can add it under the commands section

```
hbk619.pytest_parser = pytest -x
```


### Git status

If you would like to use git and have feedback for the status command indicating what files are staged e.g.
"new file path/to/file.txt modified another/file.py" configure TDSR in the plugins section as below

```
hbk619.git_status = p
```

If you would like to make parsing slightly faster and have a consistent command to run git status
you can add it under the commands section

```
hbk619.git_status = git status
```

### Tab auto complete

If you would like to hear the items shown in the terminal when you press tab to auto complete a path, along
with what is selected you can add the below to the commands section, provided you are using a zsh terminal

```
hbk619.tabbing = ^(\(.*\))?➜\s{2}.+✗?
```
