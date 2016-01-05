# coding:utf-8
import sys
import csv
import json

import FuelSDK
import ET_Client

client = FuelSDK.ET_Client()

def describe_de(customer_key):
    """
    describe data extension with customer key.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    de_target_fields = [
        "Name",
        "CustomerKey",
        "DefaultValue",
        "FieldType",
        "Scale",
        "MaxLength",
        "IsPrimaryKey",
        "IsRequired",
    ]
    myDEColumn = ET_Client.ET_DataExtension_Column()
    myDEColumn.auth_stub = client
    myDEColumn.props = de_target_fields
    myDEColumn.search_filter = {'Property' : 'DataExtension.CustomerKey','SimpleOperator' : 'equals','Value' : customer_key}
    response = myDEColumn.get()
    return [convert_field_to_dict(result, de_target_fields) for result in response.results]


def convert_field_to_dict(field, target_fields):
    converted_dict = {}
    for field_name in target_fields:
        if hasattr(field, field_name):
            converted_dict[field_name] = getattr(field, field_name)
    return converted_dict


def retrieve_de(customer_key):
    """
    retrieve all rows from data extension.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    fields = describe_de(customer_key)
    row = ET_Client.ET_DataExtension_Row()
    row.auth_stub = client
    row.CustomerKey = customer_key
    row.props = [field['Name'] for field in fields]
    response = row.get()
    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(fields)

    for result in response.results:
        row = []
        for prop in result.Properties[0]:
            if prop.Value is None:
                row.append("")
            else:
                row.append(prop.Value)
        writer.writerow(row)

    sys.exit()


def describe_all_de():
    """
    describe all data extension.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    de = ET_Client.ET_DataExtension()
    de.auth_stub = client
    de.props = ["Name", "CustomerKey", "ObjectID"]
    response = de.get()

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(de.props)

    for result in response.results:
        writer.writerow([result.Name.encode("utf-8"), result.CustomerKey.encode("utf-8"), result.ObjectID.encode("utf-8")])


def retrieve_subs():
    """
    retrieve all subscriber rows.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    getSub = ET_Client.ET_Subscriber()
    getSub.auth_stub = client
    response = getSub.get()

    attributes = []
    if (hasattr(response.results[0], 'Attributes')):
        attributes = [attr.Name.encode("utf-8") for attr in response.results[0].Attributes]

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    header = ["SubscriberID", "EmailAddress", "SubscriberKey"]
    header.extend(attributes)
    writer.writerow(header)

    for result in response.results:
        field_map = {}
        if (hasattr(result, 'Attributes')):
            for field in result.Attributes:
                field_map[field.Name] = field.Value

        fields = [result.ID, result.EmailAddress, result.SubscriberKey]
        for attribute in attributes:
            val = field_map[attribute]
            if val is None:
                fields.append("")
            else:
                fields.append(val.encode("utf-8"))

        writer.writerow(fields)


def retrieve_triggeredsend(customer_key):
    """
    retrive a triggered send with customer key.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    getTS = ET_Client.ET_TriggeredSend()
    getTS.auth_stub = client
    getTS.props = ["CustomerKey", "Name", "TriggeredSendStatus", "ObjectID"]
    getTS.search_filter = {'Property' : 'CustomerKey','SimpleOperator' : 'equals','Value' : customer_key}
    getResponse = getTS.get()

    for result in getResponse.results:
        return result.ObjectID
    return ""


def retrieve_sentevent(customer_key):
    """
    retrieve all sent event with triggered send's customer key.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    triggeredSendDefinitionObjectID = retrieve_triggeredsend(customer_key)
    getSentEvent = ET_Client.ET_SentEvent()
    getSentEvent.auth_stub = client
    getSentEvent.props = ["SendID","SubscriberKey","EventDate","Client.ID","EventType","BatchID","TriggeredSendDefinitionObjectID","ListID","PartnerKey","SubscriberID"]
    getSentEvent.search_filter = {'Property' : 'TriggeredSendDefinitionObjectID','SimpleOperator' : 'equals','Value' : triggeredSendDefinitionObjectID}
    getResponse = getSentEvent.get()

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(["EventDate", "SubscriberID"])
    for result in getResponse.results:
        writer.writerow([result.EventDate, result.SubscriberKey])

    while getResponse.more_results:
        getResponse = getSentEvent.getMoreResults()
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])


def retrieve_openevent(customer_key):
    """
    retrieve all open event with triggered send's customer key.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    triggeredSendDefinitionObjectID = retrieve_triggeredsend(customer_key)
    getSentEvent = ET_Client.ET_OpenEvent()
    getSentEvent.auth_stub = client
    getSentEvent.props = ["SendID","SubscriberKey","EventDate","Client.ID","EventType","BatchID","TriggeredSendDefinitionObjectID","ListID","PartnerKey","SubscriberID"]
    getSentEvent.search_filter = {'Property' : 'TriggeredSendDefinitionObjectID','SimpleOperator' : 'equals','Value' : triggeredSendDefinitionObjectID}
    getResponse = getSentEvent.get()
    print(getResponse)

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(["EventDate", "SubscriberID"])
    for result in getResponse.results:
        writer.writerow([result.EventDate, result.SubscriberKey])

    while getResponse.more_results:
        getResponse = getSentEvent.getMoreResults()
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])


def retrieve_bounceevent(customer_key):
    """
    retrieve all bounce event with triggered send's customer key.

    :param string customer_key: data extension's customer key
    :return: data extension's name array.
    """
    triggeredSendDefinitionObjectID = retrieve_triggeredsend(customer_key)
    getSentEvent = ET_Client.ET_BounceEvent()
    getSentEvent.auth_stub = client
    getSentEvent.props = ["SendID","SubscriberKey","EventDate","Client.ID","EventType","BatchID","TriggeredSendDefinitionObjectID","ListID","PartnerKey","SubscriberID"]
    getSentEvent.search_filter = {'Property' : 'TriggeredSendDefinitionObjectID','SimpleOperator' : 'equals','Value' : triggeredSendDefinitionObjectID}
    getResponse = getSentEvent.get()
    print(getResponse)

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writerow(["EventDate", "SubscriberID"])
    for result in getResponse.results:
        writer.writerow([result.EventDate, result.SubscriberKey])

    while getResponse.more_results:
        getResponse = getSentEvent.getMoreResults()
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])


def create_de_row(customer_key, attributes_json):
    """
    create data extension row.

    :param string customer_key: data extension's customer key
    :param string attributes_json:
    :return: data extension's name array.
    """
    de4 = ET_Client.ET_DataExtension_Row()
    de4.CustomerKey = customer_key
    de4.auth_stub = client
    de4.props = json.loads(attributes_json)
    postResponse = de4.post()
    for result in postResponse.results:
        print(result)
