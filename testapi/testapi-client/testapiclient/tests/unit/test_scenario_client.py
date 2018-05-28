import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class ScenarioClientTest(utils.TestCommand):
    def setUp(self):
        super(ScenarioClientTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'scenarios')
        self.scenario_json = {
            "installers": [],
            "name": "test_scenario"
        }
        self.scenario_client = scenarios.ScenariosClient()
        self.scenario_string = json.dumps(self.scenario_json)


class ScenarioClientGetTest(ScenarioClientTest):

    def setUp(self):
        super(ScenarioClientGetTest, self).setUp()
        self.scenarios_rsp = {'scenarios': [self.scenario_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.scenarios_rsp)
        self.scenario_client.get()
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.scenario_json)
        self.scenario_client.get_one('def')
        self.get_mock.assert_called_once_with(
            self.base_url + '/def',
            headers=clientmanager.ClientManager.headers)


class ScenarioClientCreateTest(ScenarioClientTest):

    def setUp(self):
        super(ScenarioClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.scenario_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.scenario_client.create(self.scenario_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.scenario_client.create(self.scenario_json)


class ScenarioClientDeleteTest(ScenarioClientTest):

    def setUp(self):
        super(ScenarioClientDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        self.scenario_client.delete('def')
        self.delete_mock.assert_called_once_with(
            self.base_url + '/def',
            data=None,
            headers=clientmanager.ClientManager.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            self.scenario_client.delete('def')


class ScenarioClientUpdateTest(ScenarioClientTest):

    def setUp(self):
        super(ScenarioClientUpdateTest, self).setUp()

    def test_update_success(self):
        self.put_mock.return_value = fakes.FakeResponse()
        self.scenario_client.update(
            'def', self.scenario_json)
        self.put_mock.assert_called_once_with(
            self.base_url + '/def',
            data=self.scenario_string,
            headers=clientmanager.ClientManager.headers)

    def test_update_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            self.scenario_client.update('def', self.scenario_json)
