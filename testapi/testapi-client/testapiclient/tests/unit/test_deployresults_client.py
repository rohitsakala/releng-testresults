import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import deploy_results
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class DeployResultsClientTest(utils.TestCommand):
    def setUp(self):
        super(DeployResultsClientTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'deployresults')
        self.deployresult_json = {
            'project_name': 'functest',
            'scenario': 'test-scenario',
            'stop_date': '2018-04-09 13:44:53',
            'case_name': 'test-case',
            'build_tag': 'test-build',
            'version': 'test-version',
            'pod_name': 'test-pod',
            'criteria': 'test-criteria',
            'installer': 'test-installer',
            'start_date': '2018-04-09 13:44:53',
            'details': 'test-details'
        }
        self.deployresult_id = '5a6dc1089a07c80f3c9f8d62'
        self.deployresult_string = json.dumps(self.deployresult_json)
        self.deployresult_client = deploy_results.DeployResultsClient()


class DeployResultsClientGetTest(DeployResultsClientTest):

    def setUp(self):
        super(DeployResultsClientGetTest, self).setUp()
        self.deployresults_rsp = {'deployresults': [self.deployresult_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresults_rsp)
        self.deployresult_client.get()
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_search(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresults_rsp)
        self.deployresult_client.get(name='deployresult1')
        self.get_mock.assert_called_once_with(
            self.base_url + '?name=deployresult1',
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.deployresult_json)
        self.deployresult_client.get_one('2333')
        self.get_mock.assert_called_once_with(
            self.base_url + '/2333',
            headers=clientmanager.ClientManager.headers)


class DeployResultsClientCreateTest(DeployResultsClientTest):

    def setUp(self):
        super(DeployResultsClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(self.base_url, self.deployresult_id)
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=self.succ_rsp)
        self.deployresult_client.create(self.deployresult_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.deployresult_client.create(self.deployresult_json)
