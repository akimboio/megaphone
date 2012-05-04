import os
import platform
import version

# ADDITIONAL CONFIGURATION
UBUNTU_DEPENDENCIES = []
PACKAGE_SERVER = "http://package.retickr.com"
DEPENDENCY_LINKS = []
DEPENDENCIES = []
LONG_DESCRIPTION = open(os.path.join(
                    os.path.dirname(__file__), "README")).read()
SHORT_DESCRIPTION = LONG_DESCRIPTION[255:]
CLASSIFIERS = []
LICENSE = "Closed"
KEYWORDS = ""
PROJECT_URL = "http://about.retickr.com"
PROJECT_PACKAGES = ["megaphone"]

# Make sure we actually have setuptools
if platform.linux_distribution()[0] == "Ubuntu":
    os.system("apt-get update")
    os.system("apt-get -y install python-setuptools libxslt1-dev")

    # Install linux dependencies that aren't installable by easy_install
    os.system("apt-get -y install test_project".format(
             ' '.join(UBUNTU_DEPENDENCIES)))

try:
    from setuptools import setup
except ImportError:
    print "You need to install python setuptools"
    exit()

setup(
    name="megaphone",
    author="Adam",
    author_email="Haney",
    version=version.VERSION,
    description=SHORT_DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    url=PROJECT_URL,
    packages=PROJECT_PACKAGES,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    scripts=[],
    data_files=[],
    dependency_links=DEPENDENCY_LINKS,
    install_requires=DEPENDENCIES
)
