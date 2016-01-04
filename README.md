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
$ et describe_all_de -c DATAEXTENSION_EXTERNALKEY
```

* Describe DataExtension
```bash
$ et describe_de -c DATAEXTENSION_EXTERNALKEY
```

* Describe DataExtension fields
```bash
$ et describe_fields -c DATAEXTENSION_EXTERNALKEY
```