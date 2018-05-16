.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) 2017 ZTE Corp.

=====================
TestAPI client import
=====================

**Python module to communicate with the TestAPI Server**

This project aims to provide a python module which can
communicate with the TestAPI Server. The user can use this client
to fetch/post/modify the resources on the TestAPI Server.

Usage
-----

Pod
^^^

GET
"""

Get a list of all the declared pods from the TestAPI server.

.. code-block:: shell

    from testapiclient.client import pods

    pod_client = pods.PodsClient()
    pod_client.get()

The user can filter the results by the name attribute. Backend will
use a regular expression to find the list of pods which are
related to given name.

.. code-block:: shell

    from testapiclient.client import pods

    pod_client = pods.PodsClient()
    pod_client.get(name='pod1')

.. NOTE::
  Response format: [{"_id": "", "creator": "", "role": "", "name": "",
  "details": "", "mode": "", "creation_date": ""}]


GET ONE
"""""""

Get a specific pod by its name.

.. code-block:: shell

    from testapiclient.client import pods

    pod_client = pods.PodsClient()
    pod_client.get_one('name')

.. NOTE::
  Response format: {"_id": "", "creator": "", "role": "", "name": "",
  "details": "", "mode": "", "creation_date": ""}

CREATE
""""""
This method used to create a project on the server.
The user should provide the user parameter and the password
parameter while initiating the PodsClient.

Input for the function :

  * pod-json : Json object of the project

.. NOTE::
  pod-json-schema - '{"role": "", "name": "", "details": "", "mode": ""}'

  *  role should be either "community-ci" or "production-ci"
  *  mode should be either "metal" or "virtual"

.. code-block:: shell

    from testapiclient.client import pods

    pod_client = pods.PodsClient(user='test', password='pass')
    pod_client.create({'name': 'test-api', 'mode':'metal',
                    'role':'community_ci', 'details':''})


Project
^^^^^^^

GET
"""

Get a list of all the declared projects from the TestAPI server.

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient()
    project_client.get()

User can filter the results by the name attribute. Backend will
use a regular expression to find the list of projects which are
related to given name.

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient()
    project_client.get(name='project1')

.. NOTE::
  Response format: [{"_id": "", "creator": "", "description": "",
  "name": "", "creation_date": ""}]

GET ONE
"""""""

Get a specific project by its name.

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient()
    project_client.get_one('name')

.. NOTE::
  Response format: {"_id": "", "creator": "", "description": "",
  "name": "", "creation_date": ""}

CREATE
""""""

This method used to create a project on the server.
The user should provide the user parameter and the password
parameter while initiating the ProjectsClient.

Input for the function :

  * project-json : Json object of the project

.. NOTE::
  project-json schema - '{"description": "", "name": ""}'

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.create({'name': 'functest', 'description':'sample text'}

UPDATE
""""""

This method used to update an existing project on the server.
The user should provide the user parameter and the password
parameter while initiating the ProjectsClient.

Input for the function :

  * project-name: name of the project which user want to update.
  * project-json: Json object of the project

.. NOTE::
  project-json schema - '{"description": "", "name": ""}'

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.update('functest', {'name': 'functest',
    'description':'updated text'})

DELETE
""""""

This method used to delete an existing project on the server.
The user should provide the user parameter and the password
parameter while initiating the ProjectsClient.

Input for the function :

  * project-name: name of the project which user want to delete.

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.delete('functest')


Testcase
^^^^^^^^

GET
"""

Get a list of all the declared testcases under a project
from the TestAPI server.

Input for the function :

  * project_name : Name of the project

.. code-block:: shell

    from testapiclient.client import testcases

    testcase_client = testcases.TestcasesClient()
    testcase_client.get(project_name='functest')


.. NOTE::
  Response format: [{ "project_name": "functest", "run": "",
  "description": "", "tags": "", "creation_date": "",
  "dependencies": "", "tier": "", "trust": "", "blocking": "",
  "name": "", "ci_loop": "", "url": "", "version": "",
  "criteria": "", "domains": "", "_id": "", "catalog_description": ""}]

GET ONE
"""""""

Get a specific testcase by its name and project name.

.. code-block:: shell

    from testapiclient.client import testcases

    testcase_client = testcases.TestcasesClient()
    testcase_client.get_one(project_name='functest', case_name='name')

.. NOTE::
  Response format: { "project_name": "functest", "run": "",
  "description": "", "tags": "", "creation_date": "",
  "dependencies": "", "tier": "", "trust": "", "blocking": "",
  "name": "", "ci_loop": "", "url": "", "version": "",
  "criteria": "", "domains": "", "_id": "", "catalog_description": ""}

CREATE
""""""

This method used to create a testcase on the server.
The user should provide the user parameter and the password
parameter while initiating the TestcasesClient.

Input for the function :
  * project_name : Project name
  * testcase_json : Json object of the testcase

.. NOTE::
  testcase_json schema - '{ "run": "", "description": "", "tags": "",
  "dependencies": "", "tier": "", "trust": "", "blocking": "",
  "name": "", "ci_loop": "", "url": "", "version": "",
  "criteria": "", "domains": "", "catalog_description": ""}'

.. code-block:: shell

    from testapiclient.client import testcases

    testcase_client = testcases.TestcasesClient(user='test', password='pass')
    testcase_client.create(project_name, testcase_json)

UPDATE
""""""

This method used to update an existing testcase on the server.
The user should provide the user parameter and the password
parameter while initiating the TestcasesClient.

Input for the function :
  * project_name : Project name
  * testcase_name: name of the testcase which user want to update.
  * testcase_json: Json object of the testcase

.. NOTE::
  testcase-json schema - '{ "run": "", "description": "", "tags": "",
  "dependencies": "", "tier": "", "trust": "", "blocking": "",
  "name": "", "ci_loop": "", "url": "", "version": "",
  "criteria": "", "domains": "", "catalog_description": ""}'

.. code-block:: shell

    from testapiclient.client import testcases

    testcase_client = testcases.TestcasesClient(user='test', password='pass')
    testcase_client.update(project_name, testcase_name, testcase_json)

DELETE
""""""

This method used to delete an existing testcase on the server.
The user should provide the user parameter and the password
parameter while initiating the TestcasesClient.

Input for the function :

  * project_name: name of the project
  * testcase_name: name of the testcase which user want to delete.

.. code-block:: shell

    from testapiclient.client import testcases

    testcase_client = testcases.TestcasesClient(user='test', password='pass')
    testcase_client.delete(project_name, testcase_name)


Result
^^^^^^^

GET
"""

Get a list of all the declared results from the TestAPI server.

.. code-block:: shell

    from testapiclient.client import results

    result_client = results.ResultsClient()
    result_client.get()

User can filter the results by using some attributes.

.. NOTE::
   List of search attributes.

   * case : Search results using tesetcase
   * build-tag : Search results using build tag
   * from : Search results using from date
   * last : Search results using last date
   * scenario : Search results using scenario
   * period : Search results using period
   * project : Search results using project
   * to : Search results using to
   * version : Search results using version
   * criteria : Search results using criteria
   * installer : Search results using installer
   * pod : Search results using pod
   * page : Search results using page

.. code-block:: shell

    from testapiclient.client import results

    result_client = results.ResultsClient()
    result_client.get(pod='pod1', project='project1')


.. NOTE::
  Response format: [{ "project_name": "", "scenario": "",
  "stop_date": "", "case_name": "", "build_tag": "",
  "version": "", "pod_name": "", "criteria": "",
  "installer": "", "start_date": "", "details": ""}]

GET ONE
"""""""

Get a specific result by its id.

.. code-block:: shell

    from testapiclient.client import results

    result_client = results.ResultsClient()
    result_client.get_one(result_id)

.. NOTE::
  Response format: { "project_name": "", "scenario": "",
  "stop_date": "", "case_name": "", "build_tag": "",
  "version": "", "pod_name": "", "criteria": "",
  "installer": "", "start_date": "", "details": ""}

CREATE
""""""

This method used to create a result on the server.
The user should provide a valid token to run this method.
Read testapi-client.rst to more details.

Input for the function :
  * result_json : Json object of the result

.. NOTE::
  result_json schema - '{ "project_name": "", "scenario": "",
  "stop_date": "", "case_name": "", "build_tag": "",
  "version": "", "pod_name": "", "criteria": "",
  "installer": "", "start_date": "", "details": ""}'

.. code-block:: shell

    from testapiclient.client import results

    result_client = results.ResultsClient()
    result_client.create(result_json)

DeployResult
^^^^^^^^^^^^

GET
"""

Get a list of all the declared deploy results from the TestAPI server.

.. code-block:: shell

    from testapiclient.client import deploy_results

    deploy_result_client = deploy_results.DeployResultsClient()
    deploy_result_client.get()

User can filter the deploy results by using some attributes.

.. NOTE::
   List of search attributes.

   * job-name : Search results using job
   * build_id : Search results using build id
   * from : Search results using from date
   * last : Search results using last date
   * scenario : Search results using scenario
   * period : Search results using period
   * to : Search results using to
   * version : Search results using version
   * criteria : Search results using criteria
   * installer : Search results using installer
   * pod_name : Search results using pod
   * page : Search results using page

.. code-block:: shell

    from testapiclient.client import deploy_results

    deploy_result_client = deploy_results.DeployResultsClient()
    deploy_result_client.get(scenario='scenario1', installer='installer1')


.. NOTE::
  Response format: [{"build_id": "", "upstream_build_id": "",
  "scenario": "", "stop_date": "", "start_date": "",
  "upstream_job_name": "", "version": "", "pod_name": "",
  "criteria": "", "installer": "", "_id": "", "job_name": "",
  "details": ""}]

GET ONE
"""""""

Get a specific deploy result by its id.

.. code-block:: shell

    from testapiclient.client import deploy_results

    deploy_result_client = deploy_results.DeployResultsClient()
    deploy_result_client.get_one(deploy_result_id)

.. NOTE::
  Response format: {"build_id": "", "upstream_build_id": "",
  "scenario": "", "stop_date": "", "start_date": "",
  "upstream_job_name": "", "version": "", "pod_name": "",
  "criteria": "", "installer": "", "_id": "", "job_name": "",
  "details": ""}

CREATE
""""""

This method used to create a deploy_result on the server.
The user should provide a valid token to run this method.
Read testapi-client.rst to more details.

Input for the function :
  * deploy_result_json : Json object of the deploy_result

.. NOTE::
  deploy_result_json schema - '{"build_id": "", "upstream_build_id": "",
  "scenario": "", "stop_date": "", "start_date": "",
  "upstream_job_name": "", "version": "", "pod_name": "",
  "criteria": "", "installer": "", "job_name": "",
  "details": ""}'

.. code-block:: shell

    from testapiclient.client import deploy_results

    deploy_result_client = deploy_results.DeployResultsClient()
    deploy_result_client.create(deploy_result_json)

Scenario
^^^^^^^^

GET
"""

Get a list of all the declared scenarios from the TestAPI server.

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient()
    scenario_client.get()

User can filter the scenarios by using some attributes.

.. NOTE::
   List of search attributes.

    * project : Search scenarios using project
    * installer : Search scenarios using project
    * version : Search scenarios using project
    * name: Search scenarios using project

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient()
    scenario_client.get(name='scenario1')

.. NOTE::
  Response format:  [{ "installers": [], "_id": "", "creation_date": "",
  "name": "", "creator": ""}]

GET ONE
"""""""

Get a specific scenario by its name.

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient()
    scenario_client.get_one('name')

.. NOTE::
  Response format: { "installers": [], "_id": "", "creation_date": "",
  "name": "", "creator": ""}

CREATE
""""""

This method used to create a scenario on the server.
The user should provide the user parameter and the password
parameter while initiating the ScenariosClient.

Input for the function :

  * scenario-json : Json object of the scenario

.. NOTE::
  scenario_json schema - '{ "installers": [],
  "name": ""}'

  See Installer for installer_schema

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient(user='test', password='pass')
    scenario_client.create(scenario_json)

UPDATE
""""""

This method used to update the name of an existing scenario on the server.
The user should provide the user parameter and the password
parameter while initiating the ScenariosClient.

Input for the function :

  * scenario-name: name of the scenario which user want to update.
  * scenario-json: Json object of the scenario

.. NOTE::
  * scenario_name
  * scenario_update_json schema - '{"name": ""}'

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient(user='test', password='pass')
    scenario_client.update(scenario_name, scenario_update_json)

DELETE
""""""

This method used to delete an existing scenario on the server.
The user should provide the user parameter and the password
parameter while initiating the ScenariosClient.

Input for the function :

  * scenario_name: name of the scenario which user want to delete.

.. code-block:: shell

    from testapiclient.client import scenarios

    scenario_client = scenarios.ScenariosClient(user='test', password='pass')
    scenario_client.delete('scenario_name')

Scenario Installer
^^^^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create an installer under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the InstallersClient.

Input for the function :
  * scenario_name
  * installer-json : Json object of the installer

.. NOTE::
  installer_json schema - '{ "versions": [],
  "installer": ""}'

  See version for version_schema

.. code-block:: shell

    from testapiclient.client import installers

    installer_client = installers.InstallersClient(user='test', password='pass')
    installer_client.create(scenario_name, installer_json)

UPDATE
""""""

This method used to update the all existing installers of a scenario
The user should provide the user parameter and the password
parameter while initiating the InstallersClient.

Input for the function :

  * scenario_name
  * installer-json: Json object of the installer

.. NOTE::
  * scenario_name
  * installer_json schema - [{ "versions": [], "installer": ""}]

.. code-block:: shell

    from testapiclient.client import installers

    installer_client = installers.InstallersClient(user='test', password='pass')
    installer_client.update(scenario_name, installer_update_json)

DELETE
""""""

This method used to delete  existing installers from a scenario.
on the server.
The user should provide the user parameter and the password
parameter while initiating the InstallersClient.

Input for the function :
  * scenario_name
  * installer_names: names of the installer which user want to delete.

.. code-block:: shell

    from testapiclient.client import installers

    installer_client = installers.InstallersClient(user='test', password='pass')
    installer_client.delete(scenario_name, installer_names)

Scenario Version
^^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create a version under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the VersionsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version-json : Json object of the version

.. NOTE::
  version_json schema - '{ "projects": [], "owner": "",
  "version": ""}'

  See version for version_schema

.. code-block:: shell

    from testapiclient.client import versions

    version_client = versions.VersionsClient(user='test', password='pass')
    version_client.create(scenario_name, installer_name, version_json)

UPDATE
""""""

This method used to update the all existing versions of a scenario
The user should provide the user parameter and the password
parameter while initiating the VersionsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version-json: Json object of the version

.. NOTE::
  * scenario_name
  * version_json schema - [{ "projects": [], "owner": "", "version": ""}]

.. code-block:: shell

    from testapiclient.client import versions

    version_client = versions.VersionsClient(user='test', password='pass')
    version_client.update(scenario_name, installer_name, version_update_json)

DELETE
""""""

This method used to delete  existing versions from a scenario.
on the server.
The user should provide the user parameter and the password
parameter while initiating the VersionsClient.

Input for the function :
  * scenario_name
  * installer_name
  * version_names: names of the version which user want to delete.

.. code-block:: shell

    from testapiclient.client import versions

    version_client = versions.VersionsClient(user='test', password='pass')
    version_client.delete(scenario_name, installer_name, version_names)

Scenario Project
^^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create a project under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the ProjectsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project-json : Json object of the project

.. NOTE::
  project_json schema - '{ "scores": [], "trust_indcators": [],
  "customs": [], "project": ""}'

  See project for project_schema

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.create(scenario_name, installer_name, version_name, project_json)

UPDATE
""""""

This method used to update the all existing projects of a scenario
The user should provide the user parameter and the password
parameter while initiating the ProjectsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project-json: Json object of the project

.. NOTE::
  * scenario_name
  * project_json schema - [{"scores": [], "trust_indcators": [], "customs": [], "project": ""}]

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.update(scenario_name, installer_name, version_name, project_update_json)

DELETE
""""""

This method used to delete existing projects from a scenario.
on the server.
The user should provide the user parameter and the password
parameter while initiating the ProjectsClient.

Input for the function :
  * scenario_name
  * installer_name
  * version_name
  * project_names: names of the project which user want to delete.

.. code-block:: shell

    from testapiclient.client import projects

    project_client = projects.ProjectsClient(user='test', password='pass')
    project_client.delete(scenario_name, installer_name, version_name, project_names)

Scenario Custom
^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create a custom under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the CustomsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project_name
  * custom : List of Customs

.. NOTE::
  * scenario_name
  * custom schema - ["List of Strings"]

  See custom for custom_schema

.. code-block:: shell

    from testapiclient.client import customs

    custom_client = customs.CustomsClient(user='test', password='pass')
    custom_client.create(scenario_name, installer_name, version_name,
    project_name, custom_json)

UPDATE
""""""

This method used to update the all existing customs of a scenario
The user should provide the user parameter and the password
parameter while initiating the CustomsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project_name
  * custom : List of Customs

.. NOTE::
  * scenario_name
  * custom schema - ["List of Strings"]

.. code-block:: shell

    from testapiclient.client import customs

    custom_client = customs.CustomsClient(user='test', password='pass')
    custom_client.update(scenario_name, installer_name, version_name,
    project_name custom)

DELETE
""""""

This method used to delete  existing customs from a scenario.
on the server.
The user should provide the user parameter and the password
parameter while initiating the CustomsClient.

Input for the function :
  * scenario_name
  * installer_name
  * version_name
  * project_name
  * custom: custom which user want to delete.

.. code-block:: shell

    from testapiclient.client import customs

    custom_client = customs.CustomsClient(user='test', password='pass')
    custom_client.delete(scenario_name, installer_name, version_name,
    project_name, customs)

Scenario Scores
^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create a score under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the ScoresClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project_name
  * score_json : Schema for the score

.. NOTE::
  * scenario_name
  * score_json schema - '{ "date": "", "score": ""}'

  See score for score_schema

.. code-block:: shell

    from testapiclient.client import scores

    score_client = scores.ScoresClient(user='test', password='pass')
    score_client.create(scenario_name, installer_name, version_name,
    project_name, score_json)

Scenario TrustIndicator
^^^^^^^^^^^^^^^^^^^^^^^

CREATE
""""""

This method used to create a trust indicator under a scenario
on the server. The user should provide the user parameter
and the password parameter while initiating the TrustIndicatorsClient.

Input for the function :

  * scenario_name
  * installer_name
  * version_name
  * project_name
  * trust_indicator_json : Schema for the trust_indicator

.. NOTE::
  * scenario_name
  * trust_indicator_json schema - '{ "date": "", "status": ""}'

  See trust_indicator for trust_indicator_schema

.. code-block:: shell

    from testapiclient.client import trust_indicators

    trust_indicator_client = trust_indicators.TrustIndicatorsClient(user='test', password='pass')
    trust_indicator_client.create(scenario_name, installer_name, version_name,
    project_name, trust_indicator_json)