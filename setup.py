from __future__ import unicode_literals
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PATH_TO_FILE = os.path.dirname(__file__)


with open(os.path.join(PATH_TO_FILE, 'README.rst')) as f:
    long_description = f.read()


VERSION = (0, 1, 'pre')


# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]


version = str_version


setup(
    name='nose-setenv',
    version=version,
    description="A python nose plugin to override environment variables.",
    long_description=long_description,
    author='Mahmoud Abdelkader',
    author_email='',
    url='https://github.com/mahmoudimus/nose-setenv',
    install_requires=[
        'nose >=1.0.0',
    ],
    setup_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    py_modules=['nose_setenv'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_setenv = nose_setenv:SetEnvironmentVariables',
        ]
    },
)
