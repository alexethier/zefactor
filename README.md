# Python Zefactir
*zefactir* is library for renaming tokens in a project.

# Zefactor features
* Find and replace tokens in a directory.
* Detect similar tokens in alternate case and replace with proper casing
* Pure python

# Installation
```
pip install zefactor
```
# Guided Usage
Run zefactor without any arguments and it will provide a set of guided prompts to refactor a project.
```
$ zefactor
```

# Getting Started
The guided mode can be skipped with the `-y` option. A simple example is below:
```
# Replace all text 'red' with 'blue'.
# This will automtically include replacing 'RED' with 'BLUE' and 'Red' with 'Blue'
$ zefactor -f red -r blue -y

# Replace all text 'red rocket' with 'blue ship'
# This will automatically include replacing 'RedRocket' with 'BlueShip', 'RED ROCKET' with 'BLUE SHIP' and many alternatives
$ zefactor -f red -f rocket -r blue -r ship
```
# Usage
The Zefactor CLI helps refactor projects. It will find and replace text and all variations of casing of that text.
