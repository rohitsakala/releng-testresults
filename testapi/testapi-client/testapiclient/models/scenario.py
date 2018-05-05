class ScenarioCreateRequest:
    def __init__(self, name='', installers=[]):
        self.name = name
        self.installers = installers


class ScenarioInstallerCreateRequest:
    def __init__(self, installer='', versions=[]):
        self.installer = installer
        self.versions = versions


class ScenarioVersionCreateRequest:
    def __init__(self, version='', owner='', projects=[]):
        self.version = version
        self.owner = owner
        self.projects = projects


class ScenarioProjectCreateRequest:
    def __init__(self, project='', scores=[], trust_indicators=[], customs=[]):
        self.project = project
        self.scores = scores
        self.trust_indicators = trust_indicators
        self.customs = customs


class ScenarioScoreCreateRequest:
    def __init__(self, score='', date=''):
        self.score = score
        self.date = date


class ScenarioTICreateRequest:
    def __init__(self, status='', date=''):
        self.status = status
        self.date = date
