import unittest

import etcli.commands
import etcli.app
from mock import patch, Mock


class ParserError(Exception):
    pass

class ParserTestCase(unittest.TestCase):

    customer_key = 'some_customer_key'

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_subcommand_error(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, [])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_describe_de_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['describe_fields'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_describe_de_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['describe_fields', '-c'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_describe_de_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['describe_fields', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_de_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_de'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_de_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_de', '-c'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_de_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['retrieve_de', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_describe_all_de_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['describe_all_de'])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_subs_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['retrieve_subs'])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_sentevent_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_sentevent'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_sentevent_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_sentevent', '-c'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_sentevent_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['retrieve_sentevent', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_openevent_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_openevent'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_openevent_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_openevent', '-c'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_openevent_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['retrieve_openevent', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_bounceevent_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_bounceevent'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_bounceevent_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['retrieve_bounceevent', '-c'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_retrieve_bounceevent_success(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['retrieve_bounceevent', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_create_de_row_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['create_de_row'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_create_de_row_success1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['create_de_row', '-a', '-c', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_create_de_row_success2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['create_de_row', '-a', '-n', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_create_de_row_success3(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['create_de_row', '-a', '-c', self.customer_key, '-n', self.customer_key])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_triggered_send_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['triggered_send'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_triggered_send_error2(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['triggered_send', '-c', self.customer_key])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_triggered_send_error3(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, [
            'triggered_send',
            '-c', self.customer_key,
            '-e', self.customer_key])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_triggered_send_success1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args([
            'triggered_send',
            '-c', self.customer_key,
            '-e', self.customer_key,
            '-s', self.customer_key,
        ])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_push_message_row_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['push_message'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_push_message_success1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['push_message', '-m', self.customer_key, '-s', ['aaa','bbb']])
        arg_error.assert_not_called()

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_fire_event_error1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        self.assertRaises(ParserError, parser.parse_args, ['fire_event'])
        self.assertEquals(1, arg_error.call_count)

    @patch('etcli.app.argparse.ArgumentParser.error')
    def test_fire_event_success1(self, arg_error):
        arg_error.side_effect = ParserError('')
        parser = etcli.app.build_parser()
        parser.parse_args(['fire_event', '-e', self.customer_key, '-s', self.customer_key])
        arg_error.assert_not_called()