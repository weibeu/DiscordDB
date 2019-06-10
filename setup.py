"""
DiscordDB
---------

A simple database which uses a Discord channel to store data.

"""


import re
import os

from setuptools import setup, find_packages


def __get_version():
    with open("discordDB/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [
    "discord.py",
]


if os.getenv('READTHEDOCS') == 'True':
    requirements += [
        'sphinxcontrib-napoleon',
    ]

extra_requirements = {
    'docs': [
        'sphinx==2.1.0'
    ]
}


setup(
    name='DiscordDB',
    author='□ | The Cosmos',
    url='https://github.com/thec0sm0s/DiscordDB',
    version=__get_version(),
    packages=find_packages(),
    license='MIT',
    description='A simple database which uses a Discord channel to store data.',
    long_description=__doc__,
    include_package_data=True,
    install_requires=requirements,
    extras_require=extra_requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Utilities',
    ]
)
