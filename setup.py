from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The root directory
ROOT = pathlib.Path(__file__).parent

# The text of the README file
README = (ROOT / "README.md").read_text()

# Automatically captured dependencies from requirements.txt file
with open(path.join(ROOT, "requirements.txt"), encoding="utf-8") as f:
    install_requires = [x.strip() for x in f.read().split("\n")]

setup(
    name="rgate",
    version="1.0.0",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        rgate=gateway.server:run
    """,
)
