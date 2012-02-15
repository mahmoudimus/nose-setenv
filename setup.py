import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


PATH_TO_FILE = os.path.dirname(__file__)


with open(os.path.join(PATH_TO_FILE, 'README.rst')) as f:
    long_description = f.read()


VERSION = (0, 1, 1)


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
    author_email='mabdelkader@gmail.com',
    url='https://github.com/mahmoudimus/nose-setenv',
    install_requires=[
        'nose >=1.0.0',
    ],
    setup_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'nose_setenv = nose_setenv:SetEnvironmentVariables',
        ]
    },
)
