et-cli
===============

ExactTarget CLI Tool. This tool use FuelSDK(https://github.com/salesforce-marketingcloud/FuelSDK-Python).

Requirements
------------
Python 2.7.x

Installation
------------
You can use pip to install et-cli::

$ pip install et-cli

Configuration
-------------
::

$ et configure

'et configure' command create configure file in your home directory(~/.fuelsdk/config.python).

Usage
-----
Describe all DataExtension::

$ et describe_all_de

Retrive all rows for DataExtension::

$ et retrieve_de -c DATAEXTENSION_EXTERNALKEY

Retrieve Subscribers::

$ et et retrieve_subs

Describe DataExtension fields::

$ et describe_fields -c DATAEXTENSION_EXTERNALKEY
