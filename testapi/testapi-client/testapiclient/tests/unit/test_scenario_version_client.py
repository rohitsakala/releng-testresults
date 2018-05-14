import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class VersionClientTest(utils.TestCommand):
    def setUp(self):
        super(VersionClientTest, self).setUp()
        self.scenario_name = 'scenrio1'
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/versions'.format(self.scenario_name))
        self.version_json = {
            'projects': [],
            'version': 'test-version',
            'owner': 'test_owner'
        }
        self.installer_name = 'installer'
        self.version_client = scenarios.VersionsClient()
        self.version_string = json.dumps(self.version_json)


class VersionClientCreateTest(VersionClientTest):

    def setUp(self):
        super(VersionClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.version_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.version_client.create(
            self.scenario_name, self.installer_name, self.version_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.version_client.create(
                self.scenario_name, self.installer_name, self.version_json)


class VersionClientDeleteTest(VersionClientTest):

    def setUp(self):
        super(VersionClientDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        self.version_client.delete(
            self.scenario_name, self.installer_name, 'def')
        kall = self.delete_mock.call_args
        args, kwargs = kall
        self.assert_url(
            args[0],
            self.base_url + '?installer=installer')

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            self.version_client.delete(
                self.scenario_name, self.installer_name, 'def')


class VersionClientUpdateTest(VersionClientTest):

    def setUp(self):
        super(VersionClientUpdateTest, self).setUp()

    def test_update_success(self):
        self.put_mock.return_value = fakes.FakeResponse()
        self.version_client.update(
            self.scenario_name,
            self.installer_name,
            self.version_json)
        self.put_mock.assert_called_once_with(
            self.base_url + '?installer=installer',
            data=self.version_string,
            headers=clientmanager.ClientManager.headers)

    def test_update_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            self.version_client.update(
                self.scenario_name,
                self.installer_name,
                self.version_json)
