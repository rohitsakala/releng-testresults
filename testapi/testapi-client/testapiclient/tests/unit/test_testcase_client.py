import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import testcases
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class TestcaseClientTest(utils.TestCommand):
    def setUp(self):
        super(TestcaseClientTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'projects/{}/cases')
        self.project_name = 'functest'
        self.testcase_json = {
            'run': '',
            'name': 'test-case',
            'ci_loop': '',
            'tags': '',
            'url': '',
            'blocking': '',
            'domains': '',
            'dependencies': '',
            'version': '',
            'criteria': '',
            'tier': '',
            'trust': '',
            'catalog_description': '',
            'description': ''
        }
        self.testcase_client = testcases.TestcasesClient()
        self.testcase_string = json.dumps(self.testcase_json)


class TestcaseClientGetTest(TestcaseClientTest):

    def setUp(self):
        super(TestcaseClientGetTest, self).setUp()
        self.testcases_rsp = {'testcases': [self.testcase_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.testcases_rsp)
        self.testcase_client.get(self.project_name)
        self.get_mock.assert_called_once_with(
            self.base_url.format(self.project_name),
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(
            data=self.testcase_json)
        self.testcase_client.get_one(self.project_name, 'def')
        self.get_mock.assert_called_once_with(
            self.base_url.format(self.project_name) + '/def',
            headers=clientmanager.ClientManager.headers)


class TestcaseClientCreateTest(TestcaseClientTest):

    def setUp(self):
        super(TestcaseClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.testcase_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.testcase_client.create(self.project_name, self.testcase_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.testcase_client.create(self.project_name, self.testcase_json)


class TestcaseClientDeleteTest(TestcaseClientTest):

    def setUp(self):
        super(TestcaseClientDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        self.testcase_client.delete(self.project_name, 'def')
        self.delete_mock.assert_called_once_with(
            self.base_url.format(self.project_name) + '/def',
            data=None,
            headers=clientmanager.ClientManager.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            self.testcase_client.delete(self.project_name, 'def')


class TestcaseClientUpdateTest(TestcaseClientTest):

    def setUp(self):
        super(TestcaseClientUpdateTest, self).setUp()

    def test_update_success(self):
        self.put_mock.return_value = fakes.FakeResponse()
        self.testcase_client.update(
            self.project_name, 'def', self.testcase_json)
        self.put_mock.assert_called_once_with(
            self.base_url.format(self.project_name) + '/def',
            data=self.testcase_string,
            headers=clientmanager.ClientManager.headers)

    def test_update_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            self.testcase_client.update(
                self.project_name, 'def', self.testcase_json)
