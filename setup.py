
import sys
import os
# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'z2lablelmap_moc',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '2.0.1',
      description      =   'Convert lh/rh z-score vector to FreeSurfer labelmap', 
      long_description =   readme(),
      author           =   'Rudolph Pienaar',
      author_email     =   'rudolph.pienaar@gmail.com',
      url              =   'https://github.com/FNNDSC/pl-z2lablelmap_moc',
      packages         =   ['z2lablelmap_moc'],
      install_requires =   ['chrisapp', 'pandas', 'numpy', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['z2lablelmap_moc/z2lablelmap_moc.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
