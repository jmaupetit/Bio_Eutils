"""Distutils minimalist setup script for Bio_Eutils module

Bio_Eutils is the standalone version of the Entrez and Medline
BioPython (http://www.biopython.org) module. It is used to access to
the NCBI E-utilities (http://www.ncbi.nlm.nih.gov/books/NBK25501/) - a
set of (web)services to query Entrez databases.

The main purpose of this module is to keep the installation step as
small and simple as possible. Hence the module comes with no other
dependencies. For a quick install, just type the following command
from a terminal:

python setup.py install

For more info, please refer to the github repository:
https://github.com/jmaupetit/Bio_Eutils
"""

from distutils.core import setup

setup(
    name="Bio_Eutils",
    packages=["Bio_Eutils", "Bio_Eutils.Entrez", "Bio_Eutils.Medline"],
    package_data={
        'Bio_Eutils.Entrez': ['DTDs/*.dtd', 'DTDs/*.ent', 'DTDs/*.mod'],
        },
    version="1.59",
    description="Standalone version of the Biopython Eutils modules",
    author="The Biopython Consortium",
    author_email="biopython@biopython.org",
    maintainer="Julien Maupetit",
    maintainer_email="julien@maupetit.net",
    url="https://github.com/jmaupetit/Bio_Eutils",
    download_url="https://github.com/jmaupetit/Bio_Eutils/zipball/master",
    keywords=["biopython", "Entrez", "Eutils", "Medline", "NCBI"],
    platforms=["Platform independant", ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        ],
    license="Biopython",
    long_description="""Bio_Eutils is the standalone version of the Entrez
and Medline BioPython (http://www.biopython.org) modules. It is used to access
to the NCBI E-utilities (http://www.ncbi.nlm.nih.gov/books/NBK25501/) - a set
of (web)services to query Entrez databases.

The main purpose of this module is to keep the installation step as small and
simple as possible. Hence the module comes with no other dependencies.""",
)
