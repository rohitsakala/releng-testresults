import json

from testapiclient.client import base
from testapiclient.utils import urlparse


class ScenariosClient(base.Client):
    resource = 'scenarios'

    def __init__(self, **kwargs):
        super(ScenariosClient, self).__init__(**kwargs)

    def create(self, scenario_req):
        return self.clientmanager.post(self.url, scenario_req)

    def get(self, **queries):
        if queries:
            return json.dumps(
                self.clientmanager.get(
                    urlparse.query_join(self.url, **queries))['scenarios'])
        else:
            return json.dumps(
                self.clientmanager.get(self.url)['scenarios'])

    def get_one(self, scenario_name):
        return json.dumps(
            self.clientmanager.get(
                urlparse.path_join(
                    self.url, scenario_name)))

    def delete(self, scenario_name):
        return self.clientmanager.delete(
            urlparse.path_join(
                self.url, scenario_name))

    def update(self, scenario_name, scenario_req):
        return self.clientmanager.put(
            urlparse.path_join(
                self.url, scenario_name), scenario_req)


class InstallersClient(base.Client):
    resource = 'scenarios/{}/installers'

    def __init__(self, **kwargs):
        super(InstallersClient, self).__init__(**kwargs)

    def delete(self, scenario_name, name):
        return self.clientmanager.delete(
            self.url.format(scenario_name), [name])

    def update(self, scenario_name, installer_req):
        return self.clientmanager.put(
            self.url.format(scenario_name), installer_req)

    def create(self, scenario_name, installer_req):
        return self.clientmanager.post(
            self.url.format(scenario_name), installer_req)


class VersionsClient(base.Client):
    resource = 'scenarios/{}/versions'

    def __init__(self, **kwargs):
        super(VersionsClient, self).__init__(**kwargs)

    def delete(self, scenario_name, installer, name):
        queries = {'installer': installer}
        return self.clientmanager.delete(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), name)

    def update(self, scenario_name, installer, version_req):
        queries = {'installer': installer}
        return self.clientmanager.put(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), version_req)

    def create(self, scenario_name, installer, version_req):
        queries = {'installer': installer}
        return self.clientmanager.post(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), version_req)


class VersionsOwnerClient(base.Client):
    resource = 'scenarios/{}/owner'

    def __init__(self, **kwargs):
        super(VersionsOwnerClient, self).__init__(**kwargs)

    def update(self, scenario_name, installer, version, owner):
        queries = {'installer': installer, 'version': version}
        return self.clientmanager.put(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), owner)


class ProjectsClient(base.Client):
    resource = 'scenarios/{}/projects'

    def __init__(self, **kwargs):
        super(ProjectsClient, self).__init__(**kwargs)

    def delete(self, scenario_name, installer, version, name):
        queries = {'installer': installer, 'version': version}
        return self.clientmanager.delete(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), name)

    def update(self, scenario_name, installer, version, project_req):
        queries = {'installer': installer, 'version': version}
        return self.clientmanager.put(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), project_req)

    def create(self, scenario_name, installer, version, project_req):
        queries = {'installer': installer, 'version': version}
        return self.clientmanager.post(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), project_req)


class TrustIndicatorsClient(base.Client):
    resource = 'scenarios/{}/trust_indicators'

    def __init__(self, **kwargs):
        super(TrustIndicatorsClient, self).__init__(**kwargs)

    def create(self, scenario_name, installer, version, project, trust_in_req):
        queries = {
            'installer': installer, 'version': version, 'project': project}
        return self.clientmanager.post(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), trust_in_req)


class ScoresClient(base.Client):
    resource = 'scenarios/{}/scores'

    def __init__(self, **kwargs):
        super(ScoresClient, self).__init__(**kwargs)

    def create(self, scenario_name, installer, version, project, scores_req):
        queries = {
            'installer': installer, 'version': version, 'project': project}
        return self.clientmanager.post(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), scores_req)


class CustomsClient(base.Client):
    resource = 'scenarios/{}/customs'

    def __init__(self, **kwargs):
        super(CustomsClient, self).__init__(**kwargs)

    def delete(self, scenario_name, installer, version, project, customs):
        queries = {
            'installer': installer, 'version': version, 'project': project}
        return self.clientmanager.delete(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), customs)

    def update(self, scenario_name, installer, version, project, customs):
        queries = {
            'installer': installer, 'version': version, 'project': project}
        return self.clientmanager.put(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), customs)

    def create(self, scenario_name, installer, version, project, customs):
        queries = {
            'installer': installer, 'version': version, 'project': project}
        return self.clientmanager.post(
            urlparse.query_join(
                self.url.format(scenario_name), **queries), customs)
