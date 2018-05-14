import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class ProjectClientTest(utils.TestCommand):
    def setUp(self):
        super(ProjectClientTest, self).setUp()
        self.scenario_name = 'scenrio1'
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/projects'.format(self.scenario_name))
        self.project_json = {
            'trust_indicators': [],
            'project': 'test-project',
            'scores': [],
            'customs': []
        }
        self.installer_name = 'installer'
        self.version_name = 'version'
        self.project_client = scenarios.ProjectsClient()
        self.project_string = json.dumps(self.project_json)


class ProjectClientCreateTest(ProjectClientTest):

    def setUp(self):
        super(ProjectClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.project_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.project_client.create(
            self.scenario_name, self.installer_name,
            self.version_name, self.project_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.project_client.create(
                self.scenario_name, self.installer_name,
                self.version_name, self.project_json)


class ProjectClientDeleteTest(ProjectClientTest):

    def setUp(self):
        super(ProjectClientDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        self.project_client.delete(
            self.scenario_name, self.installer_name,
            self.version_name, 'def')
        kall = self.delete_mock.call_args
        args, kwargs = kall
        self.assert_url(
            args[0],
            self.base_url + '?installer=installer&version=version')

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            self.project_client.delete(
                self.scenario_name, self.installer_name,
                self.version_name, 'def')


class ProjectClientUpdateTest(ProjectClientTest):

    def setUp(self):
        super(ProjectClientUpdateTest, self).setUp()

    def test_update_success(self):
        self.put_mock.return_value = fakes.FakeResponse()
        self.project_client.update(
            self.scenario_name,
            self.installer_name,
            self.version_name,
            self.project_json)
        kall = self.put_mock.call_args
        args, kwargs = kall
        self.assert_url(
            args[0],
            self.base_url + '?installer=installer&version=version')

    def test_update_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            self.project_client.update(
                self.scenario_name,
                self.installer_name,
                self.version_name,
                self.project_json)
