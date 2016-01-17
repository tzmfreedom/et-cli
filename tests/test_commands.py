# -*- coding: utf-8 -*-
import unittest

import etcli.commands
import etcli.app
from etcli.commands import Commands
from mock import patch, Mock


class CommmandsTestCase(unittest.TestCase):

    @patch('etcli.commands.FuelSDK.ET_DataExtension_Column')
    @patch('etcli.commands.FuelSDK.ET_Client')
    def test_describe_de(self, ET_Client, ET_DataExtension_Column):
        instance = ET_DataExtension_Column.return_value
        response_mock = Mock()
        response_mock.results = [
            Mock(Name='TextField1'),
            Mock(Name='TextField2'),
            Mock(Name='TextField3'),
        ]
        instance.get.return_value = response_mock
        customer_key = 'hoge'

        args = etcli.app.build_parser().parse_args([
            'describe_fields',
            '-c',
            customer_key
        ])

        commands = Commands()
        commands.authenticate()
        results = commands.describe_de(args)
        ET_Client.assert_called_once_with(debug=False)
        ET_DataExtension_Column.assert_called_once_with()
        instance.get.assert_called_once_with()

        self.assertEquals(3, len(results))
        for i in range(0, len(results)):
            self.assertEquals(response_mock.results[i].Name, results[i]['Name'])

        self.assertEquals(customer_key, instance.search_filter['Value'])

if __name__ == '__main__':
    unittest.main()
