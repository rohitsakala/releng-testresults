import json

from mock import mock
from six.moves.urllib import parse
import testtools

from testapiclient.cli import pods
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class PodTest(utils.TestCommand):
    def setUp(self):
        super(PodTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'pods')
        self.pod_json = {
            'role': 'community-ci',
            'name': 'test_pod',
            'details': '',
            'mode': 'metal'
        }
        self.pod_string = json.dumps(self.pod_json)


class PodGetTest(PodTest):

    def setUp(self):
        super(PodGetTest, self).setUp()
        self.pods_rsp = {'pods': [self.pod_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.pods_rsp)
        pod_get = pods.PodGet(self.app, mock.Mock())
        args = ['-name', 'dfs']
        verifies = [('name', 'dfs')]
        parsed_args = self.check_parser(pod_get, args, verifies)
        pod_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '?name=dfs',
            headers=clientmanager.ClientManager.headers)

    def test_get_all(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.pods_rsp)
        pod_get = pods.PodGet(self.app, mock.Mock())
        args = []
        verifies = []
        parsed_args = self.check_parser(pod_get, args, verifies)
        pod_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.pod_json)
        pod_get_one = pods.PodGetOne(self.app, mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(pod_get_one, args, verifies)
        pod_get_one.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '/def',
            headers=clientmanager.ClientManager.headers)


class PodCreateTest(PodTest):

    def setUp(self):
        super(PodCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(self.base_url, self.pod_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=self.succ_rsp)
        pod_create = pods.PodCreate(self.app, mock.Mock())
        args = [self.pod_string]
        verifies = [('pod', self.pod_json)]
        parsed_args = self.check_parser(pod_create, args, verifies)
        pod_create.take_action(parsed_args)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            pod_create = pods.PodCreate(self.app, mock.Mock())
            args = [self.pod_string]
            verifies = [('pod', self.pod_json)]
            parsed_args = self.check_parser(pod_create, args, verifies)
            pod_create.take_action(parsed_args)


class PodDeleteTest(PodTest):

    def setUp(self):
        super(PodDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        pod_delete = pods.PodDelete(self.app, mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(pod_delete, args, verifies)
        pod_delete.take_action(parsed_args)
        self.delete_mock.assert_called_once_with(
            self.base_url + '/def',
            data=None,
            headers=clientmanager.ClientManager.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            pod_delete = pods.PodDelete(self.app, mock.Mock())
            args = ['def']
            verifies = [('name', 'def')]
            parsed_args = self.check_parser(pod_delete, args, verifies)
            pod_delete.take_action(parsed_args)
