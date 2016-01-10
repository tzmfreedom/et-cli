# coding:utf-8
import argparse
import json
from commands import Commands

from . import __version__

def build_parser():    
    parser = argparse.ArgumentParser(
        description='ExactTarget Command Line Interface Tool.')
    parser.add_argument(
        '-v', '--version',
        action='version', version='%(prog)s ' + __version__)
    subparsers = parser.add_subparsers(help='sub-command help')

    # retrieve data extension
    retreive_parser = subparsers.add_parser(
        'retrieve_de', help='retrieve data extension rows.')
    retreive_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    retreive_parser.set_defaults(command_name='retrieve_de')

    # describe  all data extension
    describe_all_de_parser = subparsers.add_parser(
        'describe_all_de', help='describe all data extension.')
    describe_all_de_parser.set_defaults(command_name='describe_all_de')

    # describe fields
    describe_fields_parser = subparsers.add_parser(
        'describe_fields', help='describe data extension fields.')
    describe_fields_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    describe_fields_parser.set_defaults(command_name='describe_de')

    # retrieve subscriber
    retrieve_subs_parser = subparsers.add_parser(
        'retrieve_subs', help='retrieve subscribers.')
    retrieve_subs_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    retrieve_subs_parser.set_defaults(command_name='retrieve_subs')

    # retrieve sent event
    retrieve_sentevent_parser = subparsers.add_parser(
        'retrieve_sentevent', help='retrieve sent event.')
    retrieve_sentevent_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    retrieve_sentevent_parser.set_defaults(command_name='retrieve_sentevent')

    # retrieve open event
    retrieve_openevent_parser = subparsers.add_parser(
        'retrieve_openevent', help='retrieve open event.')
    retrieve_openevent_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    retrieve_openevent_parser.set_defaults(command_name='retrieve_openevent')

    # retrieve bounce event
    retrieve_bounceevent_parser = subparsers.add_parser(
        'retrieve_bounceevent', help='retrieve bounce event.')
    retrieve_bounceevent_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    retrieve_bounceevent_parser.set_defaults(command_name='retrieve_bounceevent')

    # configure
    configure_parser = subparsers.add_parser('configure', help='configuration')
    configure_parser.set_defaults(command_name='configure')

    # create data extesion
    create_de_row_parser = subparsers.add_parser(
        'create_de_row', help='create data extension row.')
    create_de_row_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='')
    create_de_row_parser.set_defaults(command_name='create_de_row')

    return parser


def main():
    commands = Commands()
    parser = build_parser()
    args = parser.parse_args()
    commands.authenticate()
    try:
        getattr(commands, args.command_name)(args)
    except AttributeError as e:
        print('[{}] command does not exist.'.format(args.command_name))

    
if __name__ == '__main__':
    main()
