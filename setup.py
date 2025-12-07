#!/usr/bin/env python

from setuptools import setup


from setuptools import find_packages, setup


def get_requirements():
    """Collects requirements"""
    with open("requirements.txt", "r") as fp:
        requirements = [line.strip() for line in fp if line.strip()]
        print(requirements)
        return requirements

def main():
    setup(name='vortex_radioss',
        version='1.02',
        description='vortex-radioss library for Radioss',
        license="Mozilla Public License Version 2.0",
        packages=['vortex_radioss.animtod3plot'],
        install_requires=get_requirements(),)


if __name__ == "__main__":
    main()
