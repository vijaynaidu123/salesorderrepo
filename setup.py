from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tasks/__init__.py
from tasks import __version__ as version

setup(
	name="tasks",
	version=version,
	description="work",
	author="abc",
	author_email="abc",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
