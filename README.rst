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

Retrive sent event for triggered send::

$ et retrieve_sentevent -c TRIGGERED_SEND_EXTERNALKEY

Retrive open event for triggered send::

$ et retrieve_openevent -c TRIGGERED_SEND_EXTERNALKEY

Retrive bounce event for triggered send::

$ et retrieve_bounceevent -c TRIGGERED_SEND_EXTERNALKEY

Retrieve Subscribers::

$ et retrieve_subs

Describe DataExtension fields::

$ et describe_fields -c DATAEXTENSION_EXTERNALKEY
