# generator3
[![img](https://shields.io/badge/pypi-%20grey?logo=pypi)](https://pypi.org/project/generator3)<br>
generator3 is a Python package to export Scratch sprite scripts to the well known scratchblocks syntax.
## Installation
```bash
$ python3 -m pip install generator3
```
## Usage
```python
import generator3
# Converts to scratchblocks and puts each sprites' scripts in a HTML file
generator3.Generator(pid).toBlocks()
```
This is still in progress so not every block will be rendered!<br>
Made with ❤️ by themysticsavages