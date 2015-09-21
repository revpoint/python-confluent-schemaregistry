# Setup
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
from sys import version_info

import confluent.schemaregistry

install_requires = []

version = '.'.join([ str(confluent.schemaregistry.__version__[i]) for i in range(3) ])

setup(
    name = 'rpm-confluent-schemaregistry',
    version = version,
    packages = ['confluent',
                'confluent.schemaregistry',
                'confluent.schemaregistry.serializers',
                'confluent.schemaregistry.client'],


    # Project uses simplejson, so ensure that it gets installed or upgraded
    # on the target machine
    install_requires = ['avro'],

    # metadata for upload to PyPI
    author = 'Verisign',
    author_email = 'vsrtc-dev@verisign.com',
    description = 'Confluent Schema Registry lib',
    keywords = 'This is a mirror of https://github.com/verisign/python-confluent-schemaregistry until that package is registered on PyPI.',
    extras_require = {
        'fastavro': ['fastavro'],
    },
    test_requires = ['unittest2']
)
