# coding:utf-8
import argparse
import sys
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
    describe_fields_parser.set_defaults(command_name='describe_de_command')

    # retrieve subscriber
    retrieve_subs_parser = subparsers.add_parser(
        'retrieve_subs', help='retrieve subscribers.')
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
        type=str, default=None, help='')
    create_de_row_parser.add_argument(
        '-n', '--name',
        type=str, default=None, help='')
    create_de_row_parser.add_argument(
        '-a', '--attribute_file',
        nargs='?', type=argparse.FileType('r'),
        const=sys.stdin, required=True, help='Attributes')
    create_de_row_parser.set_defaults(command_name='create_de_row')

    # triggered send
    triggered_send_parser = subparsers.add_parser(
        'triggered_send', help='Triggered Send.')
    triggered_send_parser.add_argument(
        '-c', '--customer_key',
        type=str, required=True, help='Subscriber Key')
    triggered_send_parser.add_argument(
        '-s', '--subscriber_key',
        type=str, required=True, help='Subscriber')
    triggered_send_parser.add_argument(
        '-e', '--email',
        type=str, required=True, help='EmailAddress')
    triggered_send_parser.add_argument(
        '-a', '--attribute_file',
        nargs='?', type=argparse.FileType('r'),
        const=sys.stdin, default=None, help='Attributes')
    triggered_send_parser.set_defaults(command_name='triggered_send')

    # push message
    push_message_parser = subparsers.add_parser(
        'push_message', help='Push message.')
    push_message_parser.add_argument(
        '-m', '--message_id',
        type=str, required=True, help='Push message id')
    push_message_parser.add_argument(
        '-s', '--subscriber_keys',
        type=str, nargs='*', default=[], help='Subscriber list')
    push_message_parser.add_argument(
        '-d', '--device_tokens',
        type=str, nargs='*', default=[], help='Device token list')
    push_message_parser.add_argument(
        '-o', '--is_override', action='store_true', help='Is override message')
    push_message_parser.add_argument(
        '-a', '--additional_params', help='Additional parameters')
    push_message_parser.set_defaults(command_name='push_message')

    # fire event
    fire_event_parser = subparsers.add_parser(
        'fire_event', help='Fire event for interaction.')
    fire_event_parser.add_argument(
        '-e', '--event_definition_key',
        type=str, required=True, help='Event definition key')
    fire_event_parser.add_argument(
        '-s', '--subscriber_key',
        type=str, required=True, help='Subscriber Key')
    fire_event_parser.add_argument(
        '-d', '--data_file',
        type=argparse.FileType('r'),
        default=sys.stdin, help='Event data')
    fire_event_parser.set_defaults(command_name='fire_event')

    return parser


def validate(parser):
    args = parser.parse_args()
    if (
        args.command_name == 'push_message' and
        len(args.subscriber_keys) == 0 and
        len(args.device_tokens) == 0
    ):
        parser.error('At least one of the arguments --subscriber_keys --device_tokens is required')

    if (
        args.command_name == 'create_de_row' and
        args.customer_key is None and
        args.name is None
    ):
        parser.error('At least one of the arguments --customer_key --name is required')
    return args


def main():
    parser = build_parser()
    args = validate(parser)

    commands = Commands()
    commands.authenticate()
    try:
        getattr(commands, args.command_name)(args)
    except AttributeError:
        print('[{}] command does not exist.'.format(args.command_name))


if __name__ == '__main__':
    main()
