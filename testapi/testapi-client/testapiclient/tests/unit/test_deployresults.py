import json

from mock import mock
from six.moves.urllib import parse
import testtools

from testapiclient.cli import deployresults
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class DeployresultTest(utils.TestCommand):
    def setUp(self):
        super(DeployresultTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'deployresults')
        self.deployresult_json = {
            'job_name': 'daisy-deploy',
            'scenario': 'test-scenario',
            'stop_date': '2018-04-09 13:44:53',
            'upstream_job_name': 'test-job',
            'build_id': 'test-build',
            'version': 'test-version',
            'pod_name': 'test-pod',
            'criteria': 'test-criteria',
            'installer': 'test-installer',
            'start_date': '2018-04-09 13:44:53',
            'details': 'test-details',
            'upstream_build_id': 'test-stream'
        }
        self.deployresult_string = json.dumps(self.deployresult_json)


class DeployresultGetTest(DeployresultTest):

    def setUp(self):
        super(DeployresultGetTest, self).setUp()
        self.deployresults_rsp = {'deployresults': [self.deployresult_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresults_rsp)
        deployresult_get = deployresults.DeployresultGet(
            self.app, mock.Mock())
        args = ['-job-name', 'dfs']
        verifies = [('job_name', 'dfs')]
        parsed_args = self.check_parser(deployresult_get, args, verifies)
        deployresult_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '?job_name=dfs',
            headers=clientmanager.ClientManager.headers)

    def test_get_all(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresults_rsp)
        deployresult_get = deployresults.DeployresultGet(
            self.app, mock.Mock())
        args = []
        verifies = []
        parsed_args = self.check_parser(deployresult_get, args, verifies)
        deployresult_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresult_json)
        deployresult_get_one = deployresults.DeployresultGetOne(
            self.app, mock.Mock())
        args = ['def']
        verifies = [('deployresult_id', 'def')]
        parsed_args = self.check_parser(
            deployresult_get_one, args, verifies)
        deployresult_get_one.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '/def',
            headers=clientmanager.ClientManager.headers)


class DeployresultCreateTest(DeployresultTest):

    def setUp(self):
        super(DeployresultCreateTest, self).setUp()

    def test_create_success(self):
        succ_rsp = {
            'href': '{}/{}'.format(self.base_url,
                                   self.deployresult_json.get('project_name'))
        }
        self.post_mock.return_value = fakes.FakeResponse(data=succ_rsp)
        deployresult_create = deployresults.DeployresultCreate(
            self.app, mock.Mock())
        args = [self.deployresult_string]
        verifies = [('deployresult', self.deployresult_json)]
        parsed_args = self.check_parser(deployresult_create, args, verifies)
        deployresult_create.take_action(parsed_args)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            deployresult_create = deployresults.DeployresultCreate(
                self.app, mock.Mock())
            args = [self.deployresult_string]
            verifies = [('deployresult', self.deployresult_json)]
            parsed_args = self.check_parser(
                deployresult_create, args, verifies)
            deployresult_create.take_action(parsed_args)
