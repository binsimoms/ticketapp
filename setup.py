from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ticketapp/__init__.py
from ticketapp import __version__ as version

setup(
	name="ticketapp",
	version=version,
	description="ticket management",
	author="binsi",
	author_email="binsi.nk@momscode.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
