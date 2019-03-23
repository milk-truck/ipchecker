from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipchecker',

    version='0.2.0',

    description='My ip checking tool',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/king-drew/ipchecker.git',

    author='Drew Burchfiel',

    author_email='drew.burchfiel@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    python_requires='>=3.5',

    install_requires=['requests'],

    entry_points={  # Optional
        'console_scripts': [
            'ipchecker=ipchecker:main',
        ],
    },
)
