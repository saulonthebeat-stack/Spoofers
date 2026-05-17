#!/usr/bin/env python
"""Weather Dashboard Setup Script."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README_WEATHER.md").read_text(encoding="utf-8")

setup(
    name="weather-dashboard",
    version="1.0.0",
    author="Saul on the Beat Stack",
    author_email="saulonthebeat@gmail.com",
    description="A modern real-time weather dashboard with OpenWeatherMap API integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saulonthebeat-stack/Spoofers",
    project_urls={
        "Bug Tracker": "https://github.com/saulonthebeat-stack/Spoofers/issues",
        "Documentation": "https://github.com/saulonthebeat-stack/Spoofers",
        "Source Code": "https://github.com/saulonthebeat-stack/Spoofers",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Flask>=2.3.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
        ],
        "build": [
            "pyinstaller>=6.0.0",
            "setuptools-scm",
        ],
    },
    entry_points={
        "console_scripts": [
            "weather-dashboard=weather_app:app.run",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*", "static/*", ".env.example"],
    },
)
