# NAU school network CLI

The CLI tool use Click, Requests to help you login to NAU school network

## Install
Install python3 and pip, then
```bash
pip install nau_net
```

## Usage
```bash
nau --help
nau add --username --password
nau remove
nau login
nau logout
nau status
```

## Develop
```bash
git clone
pip install requirement.txt
pip install -e . #install nau_net in editable mode
```

## Publish
```bash
python setup.py sdist bdist_wheel
twine register dist/mypkg.whl #need ~/.pypirc
twine upload dist/*
```
[About Python packaging](https://packaging.python.org/current/)


## Plan
- Python2.x Compatibility
