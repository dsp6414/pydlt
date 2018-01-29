import os
import subprocess
from setuptools import setup, find_packages

version = '0.0.2'

# Got this from here
# http://blogs.nopcode.org/brainstorm/2013/05/20/pragmatic-python-versioning-via-setuptools-and-git-tags/
# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'dlt/version.py')

try:
    version_git = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).rstrip().decode("utf-8") 
except:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__ = \'" + version + '\'')


readme = open('README.rst').read()

setup(name='dlt',
      version=version,
      description='Deep Learning Toolbox for PyTorch',
      long_description=readme,
      url='https://github.com/dmarnerides/pydlt',
      license='BSD',
      author='Demetris Marnerides',
      author_email='dmarnerides@gmail.com',
      packages=find_packages(exclude=['docs', 'tests']),
      entry_points={
          'console_scripts': ['dlt-plot=dlt.viz.csvplot:plot_csv',
                              'dlt-dispatch=dlt.util.dispatch:dispatch']
      }
)
