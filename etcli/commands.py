# coding:utf-8
import sys
import csv
import json
import os

import FuelSDK
import et_objects
from getpass import getpass

CONFIG_PATH = '~/.fuelsdk/config.python'


class Commands(object):
    def authenticate(self, client_id=None, client_secret=None, debug=False):
        if client_id is None or client_secret is None:
            self.client = FuelSDK.ET_Client(debug=debug)
        else:
            self.client = FuelSDK.ET_Client(
                params={
                    'clientid': client_id,
                    'clientsecret': client_secret
                }, debug=debug)

    def configure(self, args):
        fuelsdk_config = os.path.expanduser(CONFIG_PATH)
        if (
            os.path.isfile(fuelsdk_config) and
            raw_input('Do you want to overwrite {} ?(y/n)'.format(CONFIG_PATH)) != 'y'
        ):
            return

        client_id = raw_input('Input Your ExactTarget Client ID: ')
        client_secret = getpass('Input Your ExactTarget Client Secret: ')

        fuelsdk_dir = os.path.expanduser('~/.fuelsdk')
        if not os.path.isdir(fuelsdk_dir):
            os.mkdir(fuelsdk_dir)

        f = open(fuelsdk_config, 'w')
        f.write("""[Web Services]
appsignature: none
clientid: {0}
clientsecret: {1}
defaultwsdl: https://webservice.exacttarget.com/etframework.wsdl
authenticationurl: https://auth.exacttargetapis.com/v1/requestToken?legacy=1""".format(client_id, client_secret))

    def describe_de_command(self, args):
        fields = self.describe_de(args)
        print(json.dumps(fields))

    def describe_de(self, args):
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
        deColumn = FuelSDK.ET_DataExtension_Column()
        deColumn.auth_stub = self.client
        deColumn.props = de_target_fields
        deColumn.search_filter = {
            'Property': 'DataExtension.CustomerKey',
            'SimpleOperator': 'equals',
            'Value': args.customer_key
        }
        response = deColumn.get()
        return [
            self.convert_field_to_dict(result, de_target_fields)
            for result in response.results
        ]

    def convert_field_to_dict(self, field, target_fields):
        converted_dict = {}
        for field_name in target_fields:
            if hasattr(field, field_name):
                converted_dict[field_name] = getattr(field, field_name)
        return converted_dict

    def retrieve_de(self, args):
        """
        retrieve all rows from data extension.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        fields = self.describe_de(args)
        row = FuelSDK.ET_DataExtension_Row()
        row.auth_stub = self.client
        row.CustomerKey = args.customer_key
        row.props = [field['Name'] for field in fields]
        response = row.get()
        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(row.props)

        for result in response.results:
            row = []
            for prop in result.Properties[0]:
                if prop.Value is None:
                    row.append("")
                else:
                    row.append(prop.Value.encode("utf-8"))
            writer.writerow(row)

    def describe_all_de(self, args):
        """
        describe all data extension.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        de = FuelSDK.ET_DataExtension()
        de.auth_stub = self.client
        de.props = ["Name", "CustomerKey", "ObjectID"]
        response = de.get()

        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(de.props)

        for result in response.results:
            writer.writerow([
                result.Name.encode("utf-8"),
                result.CustomerKey.encode("utf-8"),
                result.ObjectID.encode("utf-8")
            ])

    def retrieve_subs(self, args):
        """
        retrieve all subscriber rows.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        getSub = FuelSDK.ET_Subscriber()
        getSub.auth_stub = self.client
        response = getSub.get()

        attributes = []
        if (hasattr(response.results[0], 'Attributes')):
            attributes = [
                attr.Name.encode("utf-8")
                for attr in response.results[0].Attributes
            ]

        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
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

    def retrieve_triggeredsend(self, args):
        """
        retrive a triggered send with customer key.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        getTS = FuelSDK.ET_TriggeredSend()
        getTS.auth_stub = self.client
        getTS.props = [
            "CustomerKey",
            "Name",
            "TriggeredSendStatus",
            "ObjectID"
        ]
        getTS.search_filter = {
            'Property': 'CustomerKey',
            'SimpleOperator': 'equals',
            'Value': args.customer_key
        }
        getResponse = getTS.get()

        for result in getResponse.results:
            return result.ObjectID
        return ""

    def retrieve_sentevent(self, args):
        """
        retrieve all sent event with triggered send's customer key.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        triggeredSendDefinitionObjectID = self.retrieve_triggeredsend(args)
        getSentEvent = FuelSDK.ET_SentEvent()
        getSentEvent.auth_stub = self.client
        getSentEvent.props = [
            "SendID",
            "SubscriberKey",
            "EventDate",
            "Client.ID",
            "EventType",
            "BatchID",
            "TriggeredSendDefinitionObjectID",
            "ListID",
            "PartnerKey",
            "SubscriberID"
        ]
        getSentEvent.search_filter = {
            'Property': 'TriggeredSendDefinitionObjectID',
            'SimpleOperator': 'equals',
            'Value': triggeredSendDefinitionObjectID
        }
        getResponse = getSentEvent.get()

        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(["EventDate", "SubscriberID"])
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])

        while getResponse.more_results:
            getResponse = getSentEvent.getMoreResults()
            for result in getResponse.results:
                writer.writerow([result.EventDate, result.SubscriberKey])

    def retrieve_openevent(self, args):
        """
        retrieve all open event with triggered send's customer key.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        triggeredSendDefinitionObjectID = self.retrieve_triggeredsend(args)
        getOpenEvent = FuelSDK.ET_OpenEvent()
        getOpenEvent.auth_stub = self.client
        getOpenEvent.props = [
            "SendID",
            "SubscriberKey",
            "EventDate",
            "Client.ID",
            "EventType",
            "BatchID",
            "TriggeredSendDefinitionObjectID",
            "ListID",
            "PartnerKey",
            "SubscriberID"
        ]
        getOpenEvent.search_filter = {
            'Property': 'TriggeredSendDefinitionObjectID',
            'SimpleOperator': 'equals',
            'Value': triggeredSendDefinitionObjectID
        }
        getResponse = getOpenEvent.get()

        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(["EventDate", "SubscriberID"])
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])

        while getResponse.more_results:
            getResponse = getOpenEvent.getMoreResults()
            for result in getResponse.results:
                writer.writerow([result.EventDate, result.SubscriberKey])

    def retrieve_bounceevent(self, args):
        """
        retrieve all bounce event with triggered send's customer key.

        :param string customer_key: data extension's customer key
        :return: data extension's name array.
        """
        triggeredSendDefinitionObjectID = self.retrieve_triggeredsend(args)
        getBounceEvent = FuelSDK.ET_BounceEvent()
        getBounceEvent.auth_stub = self.client
        getBounceEvent.props = [
            "SendID",
            "SubscriberKey",
            "EventDate",
            "Client.ID",
            "EventType",
            "BatchID",
            "TriggeredSendDefinitionObjectID",
            "ListID",
            "PartnerKey",
            "SubscriberID"
        ]
        getBounceEvent.search_filter = {
            'Property': 'TriggeredSendDefinitionObjectID',
            'SimpleOperator': 'equals',
            'Value': triggeredSendDefinitionObjectID
        }
        getResponse = getBounceEvent.get()

        writer = csv.writer(
            sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(["EventDate", "SubscriberID"])
        for result in getResponse.results:
            writer.writerow([result.EventDate, result.SubscriberKey])

        while getResponse.more_results:
            getResponse = getBounceEvent.getMoreResults()
            for result in getResponse.results:
                writer.writerow([result.EventDate, result.SubscriberKey])

    def create_de_row(self, args):
        """
        create data extension row.

        :param string customer_key: data extension's customer key
        :param string attributes_json:
        :return: data extension's name array.
        """
        deRow = FuelSDK.ET_DataExtension_Row()
        deRow.CustomerKey = args.customer_key
        deRow.auth_stub = self.client
        args.attributes = json.loads(args.attribute_file.read())

        deRow.props = json.loads(args.attributes_json)
        deRowResponse = deRow.post()
        print(json.dumps(deRowResponse.results))

    def triggered_send(self, args):
        sendTrig = FuelSDK.ET_TriggeredSend()
        sendTrig.auth_stub = self.client
        sendTrig.props = {"CustomerKey": args.customer_key}
        if args.attribute_file is None:
            attributes = {}
        else:
            attributes = json.loads(args.attribute_file.read())

        sendTrig.subscribers = [{
            "EmailAddress": args.email,
            "SubscriberKey": args.subscriber_key,
        }]
        sendTrig.attributes = [{"Name": key, "Value": val} for key, val in attributes.items()]
        sendResponse = sendTrig.send()
        print(json.dumps([{
            "StatusCode": result.StatusCode,
            "StatusMessage": result.StatusMessage,
            "OrdinalID": result.OrdinalID,
            "NewID": result.NewID,
            "ErrorCode": result.ErrorCode if hasattr(result, "ErrorCode") else None,
        } for result in sendResponse.results]))

    def push_message(self, args):
        pushMessageContact = et_objects.ET_PushMessageContact()
        pushMessageContact.auth_stub = self.client
        pushMessageContact.props = {
            "messageId": args.message_id,
            "SubscriberKeys": args.subscriber_keys,
            "DeviceTokens": args.device_tokens
        }
        if args.is_override:
            pushMessageContact.props['Override'] = True
            input_data = args.additional_params if args.additional_params is not None else sys.stdin.read()
            pushMessageContact.props.update(json.loads(input_data))

        pushMessageContactResponse = pushMessageContact.post()
        print(json.dumps(pushMessageContactResponse.results))

    def fire_event(self, args):
        postInteractionEvent = et_objects.ET_InteractionEvents()
        postInteractionEvent.auth_stub = self.client
        postInteractionEvent.props = {
            "ContactKey": args.subscriber_key,
            "EventDefinitionKey": args.event_definition_key,
            "Data": json.loads(args.data_file.read())
        }
        postInteractionEventResponse = postInteractionEvent.post()
        print(json.dumps(postInteractionEventResponse.results))
