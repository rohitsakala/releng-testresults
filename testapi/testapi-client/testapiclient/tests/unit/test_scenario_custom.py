

from mock import mock
from six.moves.urllib import parse

from testapiclient.cli import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class CustomTest(utils.TestCommand):
    def setUp(self):
        super(CustomTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'scenarios/{}/customs')
        self.scenario_name = 's1'
        self.custom_input = 'custom'
        self.custom_parsed = ['custom']


class CustomCreateTest(CustomTest):

    def setUp(self):
        super(CustomCreateTest, self).setUp()

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=None)
        custom_create = scenarios.CustomCreate(self.app, mock.Mock())
        args = [
            '--scenario-name', 's1', '--installer', 'i1', '--version',
            'v1', '--project', 'p1', self.custom_input]
        verifies = [
            ('scenario_name', 's1'),
            ('installer', 'i1'),
            ('version', 'v1'),
            ('project', 'p1'),
            ('custom', self.custom_parsed)]
        parsed_args = self.check_parser(custom_create, args, verifies)
        custom_create.take_action(parsed_args)
        self.post_mock.assert_called_once()


class CustomDeleteTest(CustomTest):

    def setUp(self):
        super(CustomDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse(data=None)
        custom_delete = scenarios.CustomDelete(self.app, mock.Mock())
        args = [
            '--scenario-name', 's1', '--installer', 'i1',
            '--version', 'v1', '--project', 'p1', 'def']
        verifies = [
            ('scenario_name', 's1'),
            ('installer', 'i1'),
            ('version', 'v1'),
            ('project', 'p1'),
            ('name', ['def'])]
        parsed_args = self.check_parser(custom_delete, args, verifies)
        custom_delete.take_action(parsed_args)
        kall = self.delete_mock.call_args
        args, kwargs = kall
        self.assert_url(
            args[0],
            self.base_url + '?version=v1&project=p1&installer=i1')


class CustomPutTest(CustomTest):

    def setUp(self):
        super(CustomPutTest, self).setUp()

    def test_put_success(self):
        self.put_mock.return_value = fakes.FakeResponse(
            data=None)
        custom_put = scenarios.CustomPut(self.app, mock.Mock())
        args = [
            '--scenario-name', 's1', '--installer', 'i1', '--version', 'v1',
            '--project', 'p1', self.custom_input]
        verifies = [
            ('scenario_name', 's1'),
            ('installer', 'i1'),
            ('version', 'v1'),
            ('project', 'p1'),
            ('custom', self.custom_parsed)]
        parsed_args = self.check_parser(custom_put, args, verifies)
        custom_put.take_action(parsed_args)
        self.put_mock.assert_called_once()
