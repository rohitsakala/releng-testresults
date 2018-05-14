import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class InstallerClientTest(utils.TestCommand):
    def setUp(self):
        super(InstallerClientTest, self).setUp()
        self.scenario_name = 'scenrio1'
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/installers'.format(self.scenario_name))
        self.installer_json = {
            'versions': [],
            'installer': 'test-installer',
        }
        self.installer_client = scenarios.InstallersClient()
        self.installer_string = json.dumps(self.installer_json)


class InstallerClientCreateTest(InstallerClientTest):

    def setUp(self):
        super(InstallerClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.installer_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.installer_client.create(self.scenario_name, self.installer_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.installer_client.create(
                self.scenario_name, self.installer_json)


class InstallerClientDeleteTest(InstallerClientTest):

    def setUp(self):
        super(InstallerClientDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        self.installer_client.delete(self.scenario_name, 'def')
        self.delete_mock.assert_called_once_with(
            self.base_url,
            data=json.dumps(['def']),
            headers=clientmanager.ClientManager.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            self.installer_client.delete(self.scenario_name, 'def')


class InstallerClientUpdateTest(InstallerClientTest):

    def setUp(self):
        super(InstallerClientUpdateTest, self).setUp()

    def test_update_success(self):
        self.put_mock.return_value = fakes.FakeResponse()
        self.installer_client.update(
            self.scenario_name,
            self.installer_json)
        self.put_mock.assert_called_once_with(
            self.base_url,
            data=self.installer_string,
            headers=clientmanager.ClientManager.headers)

    def test_update_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            self.installer_client.update('def', self.installer_json)
