from cliff import command
from testapiclient import url_parse


class Command(command.Command):
    def get_parser(self, prog_name):
        parser = super(Command, self).get_parser(prog_name)
        parser.add_argument('-u',
                            type=str,
                            help='Username for authentication')
        parser.add_argument('-p',
                            type=str,
                            help='Password for authentication')

        return parser


class Lister(command.Command):

    @staticmethod
    def filter_by_name(url, parsed_args):
        def query_url():
            return url_parse.query_join(url, name=parsed_args.name)

        return query_url() if parsed_args.name else url


class ShowOne(command.Command):
    pass
