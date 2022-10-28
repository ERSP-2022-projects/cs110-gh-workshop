# CS110 Git/GitHub workshop

This repo contains a toy project used for the Git/GitHub workshop, CS110 F22.

## Workshop Activities
See the [workshop activities on Google Docs](https://docs.google.com/document/d/1szkAf39TYHknnqmfLKbG9r9m_DaxbIi3Mw7f2lQhdk8/edit?usp=sharing).

## Repo Contents
- `tool`: the ERSP tool's source code (and test code)
- `inputs`: the dataset inputted into the tool
  - *note: I like to put scripts to generate inputs here*
- `results`: the stdout/stderr/metrics outputted from the tool
  - *note: I like to put scripts to wrangle/tabulate results here*
- `runner.py`: the script which runs experiments in bulk
  
## Tool Usage
```
# run tool
python3 tool/my_tool.py [input file]

# run tests
pytest

# run experiments in bulk
sh runner.sh
```
