# pylint: disable=invalid-name, exec-used
"""Setup monoprice6z package."""
from __future__ import absolute_import
import sys
import os
from setuptools import setup, find_packages
# import subprocess
sys.path.insert(0, '.')

CURRENT_DIR = os.path.dirname(__file__)

# to deploy to pip, please use
# make pythonpack
# python setup.py register sdist upload
# and be sure to test it firstly using "python setup.py register sdist upload -r pypitest"
setup(name='monoprice6z',
      # version=open(os.path.join(CURRENT_DIR, 'xgboost/VERSION')).read().strip(),
      version='0.0.1',
      description=open(os.path.join(CURRENT_DIR, 'README.md')).read(),
      install_requires=['requests'],
      maintainer='John Martin',
      maintainer_email='jrmartin.iii@gmail.com',
      zip_safe=False,
      packages=find_packages(),
      include_package_data=True,
      url='https://github.com/johnnyletrois/monoprice6z.git')
