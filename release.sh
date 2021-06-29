#!/bin/sh

# remove generated files
rm -Rf .eggs
rm -Rf *.egg-info
rm -Rf dist
rm -Rf build
rm -Rf __pycache__

python setup.py sdist bdist_wheel
twine upload dist/*