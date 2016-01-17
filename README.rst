et-cli
===============
.. image:: https://travis-ci.org/tzmfreedom/et-cli.svg?branch=master
  :target: https://travis-ci.org/tzmfreedom/et-cli

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

Push message to mobile device::

  $ et push_message -m MESSAGE_ID -s SUBSCRIBER_KEY

  $ et push_message -m MESSAGE_ID -d DEVICE_TOKEN

Send Email with TriggeredSend::

  $ echo '{"foo":"bar"}' | et triggered_send -c TRIGGERED_SEND_EXTERNAL_KEY \
  -s SUBSCRIBER_KEY -e EMAIL_ADDRESS -a

  $ et triggered_send -c TRIGGERED_SEND_EXTERNAL_KEY -s SUBSCRIBER_KEY \
  -e EMAIL_ADDRESS -a ATTRIBUTE_FILENAME

Fire event for JourneyBuilder Interaction::

  $ echo '{"foo":"bar"}' | et fire_event -e EVENT_DEFINITION_KEY -s SUBSCRIBER_KEY

  $ et fire_event -e EVENT_DEFINITION_KEY -s SUBSCRIBER_KEY -d DATA_FILENAME
