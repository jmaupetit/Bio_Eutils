# Bio_Eutils

## Introduction

Bio_Eutils is the standalone version of the Entrez and Medline
[BioPython](http://www.biopython.org) modules. It is used to access to
the [NCBI E-utilities](http://www.ncbi.nlm.nih.gov/books/NBK25501/) -
a set of (web)services to query Entrez databases.

## Version

The latest version of the module follows the latest biopython release:
[1.63](http://biopython.org/wiki/Download) at this time.

## Installation

The main purpose of this module is to keep the installation step as
small and simple as possible. Hence the module comes with no other
dependencies. You can either choose to clone the repository or install
it from pip.

### Clone the module from [Github](git://github.com/jmaupetit/Bio_Eutils.git)

    git clone git://github.com/jmaupetit/Bio_Eutils.git
    cd Bio_Eutils
    python setup.py install

### Install from PyPI with pip

    pip install Bio_Eutils

## Usage

A sample script to fetch references from J. Monod follows.
	
	from Bio_Eutils import Entrez, Medline
    Entrez.email = "me@myself.org"
    
	# Search for PMIDs from author text based search
    handle = Entrez.esearch(db="pubmed", retmax=100, term="monod j[author]")
    pub_search = Entrez.read(handle)
    handle.close()
	
    # Fetch matching entries
    handle = Entrez.efetch(db='pubmed', id=pub_search['IdList'], retmax=20, rettype="medline", retmode="text")
    pub_items = Medline.parse(handle)
    
    # Work with it
    for pub_item in pub_items:
	    print "*" * 10
        print "%s - %s." % (
            pub_item.get("TI","?"),
            ", ".join(pub_item.get("AU","?"))
            )

    handle.close()

For more informations about the Entrez and Medline modules, refer to
the
[Biopython documentation](http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc96).

## Running tests

If you want to contribute to this project, you may want to run tests. This could be achieve *via*:

    $ cd Tests
    $ python run_tests.py

## Disclaimer

> Please not that [J. Maupetit](http://julien.maupetit.me) is not the
> author of the Bio.Entrez and Bio.Medline packages. He only maintains
> this standalone version for his own usage. The Bio.* modules are
> distributed under the Biopython license agreement (see LICENSE).
