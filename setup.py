#!/usr/bin/env python3
"""
Setup script for Ecosystem Simulation package
"""

from setuptools import setup, find_packages
import os

# Read the requirements from requirements.txt
def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read the README from docs directory
def read_readme():
    readme_path = os.path.join('docs', 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Ecosystem Simulation - A port of the MATLAB ecosystem simulation"

setup(
    name="ecosystem-simulation",
    version="1.0.0",
    author="Ported from MATLAB by AI Assistant",
    description="A complex predator-prey ecosystem simulation with intelligent creature behavior",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements(),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Life",
    ],
    entry_points={
        "console_scripts": [
            "ecosystem-interactive=ecosystem_simulation.simulations.interactive:main",
            "ecosystem-headless=ecosystem_simulation.simulations.headless:run_simulation",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)