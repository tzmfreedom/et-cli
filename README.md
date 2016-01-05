# et-cli
ExactTarget CLI Tool. This tool use FuelSDK(https://github.com/salesforce-marketingcloud/FuelSDK-Python).

## Requirements
Python 2.7.x

## Installation
```bash
$ pip install et-cli
```

## Configuration
```bash
$ et configure
```
'et configure' command create configure file in your home directory(~/.fuelsdk/config.python).

## Usage
* Describe all DataExtension
```bash
$ et describe_all_de
```

* Retrive all rows for DataExtension
```bash
$ et retrieve_de -c DATAEXTENSION_EXTERNALKEY
```
* Retrieve Subscribers.
```bash
$ et et retrieve_subs
```

* Describe DataExtension fields
```bash
$ et describe_fields -c DATAEXTENSION_EXTERNALKEY
```

