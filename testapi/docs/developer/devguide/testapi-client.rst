.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) 2017 ZTE Corp.

==============
TestAPI client
==============

TestAPIClient is a command-line client for TestAPI that
brings the command set for pod, project, testcase, results,
deploy result and scenario together in a single shell with a uniform command
structure.


Installation
------------

User can install this client from the source.

.. code-block:: shell

  python install testapi/testapi-client/setup.py install

After the installation, user has to set the environment variables

.. code-block:: shell

   source  testapi/testapi-client/etc/client.creds


Authentication Process
----------------------

User needs to provide the username and the password with the testapi
command.

.. code-block:: shell

    $ testapi -u [username] -p [password]
    (testapi) pod create


or

.. code-block:: shell

    testapi pode create -u [username] -p [password] [pod-schema]

First one, user can continue the progress after the authentication.
cli will create a new session to handle the request.

In second one, cli won't create a session. one time command.

Token is also used for the authorization purpose. User has to obtain the
valid token from the TestAPI comminity and set it in the following file
: **testapi/testapi-client/etc/client.creds**

.. code-block:: shell

   source  testapi/testapi-client/etc/client.creds


Command Structure
-----------------

TestAPIClient follows a common command Structure.

.. code-block:: shell

    testapi [resource-name] [function] [-u] [username] [-p] [password]
    [command-arguments]

.. NOTE::
  resource-name : include first order parent name and resource name.

  example:
  scenario installer, scenario version, scenario project, scenario custom,
  scenario trustindicator, scenario score, pod , project, testcase, result,
  deployresult and scenario.

.. NOTE::
  -u and -p are optional commands. The user can decide on them.

There are many arguments for each commands. User can get them using
help command in the cli.

.. code-block:: shell

  pod create --help/-h

Pod
^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi pod create [-u] [username] [-p] [password] [pod-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) pod create [pod-schema]

.. NOTE::
  pod-schema - '{"role": "", "name": "", "details": "", "mode": ""}'

Get
"""

Authentication is not required

.. code-block:: shell

    testapi pod get [-name] [key-word]

.. NOTE::
   -name is not mandatory. The user can use the -name option to reduce the
   search result otherwise they will get the details about all pods.

Get one
"""""""

Authentication is not required

.. code-block:: shell

    testapi pod getone [name-keyword]

.. NOTE::
   name-keyword is mandatory.


Delete
""""""

Authentication is required

.. code-block:: shell

    testapi pod delete [-u] [username] [-p] [password] [pod-name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) pod delete [pod-name]

.. NOTE::
   pod-name is mandatory.


Project
^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi project create [-u] [username] [-p] [password] [project-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) project create [project-schema]

.. NOTE::
  project-schema - '{"description": "", "name": ""}'


Get
"""

Authentication is not required

.. code-block:: shell

    testapi project get [-name] [key-word]

.. NOTE::
   -name is not mandatory. The user can use the -name option to reduce the
   search result otherwise they will get the details about all projects.

Get one
"""""""

Authentication is not required

.. code-block:: shell

    testapi project getone [name-keyword]

.. NOTE::
   name-keyword is mandatory.

Update
""""""

Authentication required

.. code-block:: shell

    testapi project put [-u] [username] [-p] [password] [project-name]
    [project-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) project put [project-name] [project-schema]

.. NOTE::
  project-schema - '{"name": "", "description": ""}'

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi project delete [-u] [username] [-p] [password] [project-name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) project delete [project-name]

.. NOTE::
   project-name is mandatory.

Testcase
^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi testcase create [-u] [username] [-p] [password]
    [--project-name] [testcase-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) testcase create [--project-name] [testcase-schema]

.. NOTE::
  testcase-schema - '{"run": "", "name": "", "ci_loop": "", "tags": "",
  "url": "", "catalog_description": "", "tier": "",
  "dependencies": "", "version": "", "criteria": "",
  "domains": "", "trust": "", "blocking": "",
  "description": ""}'


Get
"""

Authentication is not required

.. code-block:: shell

    testapi testcase get [--project-name]

.. NOTE::
   --project-name is mandatory.

Get one
"""""""

Authentication is not required

.. code-block:: shell

    testapi testcase getone [--project-name] [name]

.. NOTE::
   name and project-name are mandatory.

Update
""""""

Authentication required

.. code-block:: shell

    testapi testcase put [-u] [username] [-p] [password] [--project-name]
    [name] [testcase-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) testcase put [--project-name] [name] [testcase-schema]

.. NOTE::
  testcase-schema - '{"run": "", "name": "", "ci_loop": "", "tags": "",
  "url": "", "catalog_description": "", "tier": "",
  "dependencies": "", "version": "", "criteria": "",
  "domains": "", "trust": "", "blocking": "",
  "description": ""}


Result
^^^^^^^

Create
""""""

Token is required. Set token as an environment variable.

.. code-block:: shell

    testapi result create [-u] [username] [-p] [password] [result-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) result create [result-schema]

.. NOTE::
  result-schema - '{"project_name": "", "scenario": "", "stop_date": "",
  "case_name": "", "build_tag": "", "version": "",
  "pod_name": "", "criteria": "", "installer": "",
  "start_date": "", "details": ""}'


Get
"""

Authentication is not required

.. code-block:: shell

    testapi result get [-cli-arguments] [arguments-value]

.. NOTE::
   List of commandline arguments

   * -case : Search results using tesetcase
   * -build-tag : Search results using build tag
   * -from : Search results using from date
   * -last : Search results using last date
   * -scenario : Search results using scenario
   * -period : Search results using period
   * -project : Search results using project
   * -to : Search results using to
   * ---version : Search results using version
   * -criteria : Search results using criteria
   * -installer : Search results using installer
   * -pod : Search results using pod
   * -page : Search results using page

Get one
"""""""

Token is required. Set token as an environment variable.

.. code-block:: shell

    testapi result getone [result_id]

.. NOTE::
   result_id is mandatory.

Deploy Result
^^^^^^^^^^^^^

Create
""""""

Token is required. Set token as an environment variable.


.. code-block:: shell

    testapi deployresult [-u] [username] [-p] [password]
    [--project-name] [deployresult-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) deployresult create [deployresult-schema]

.. NOTE::
  deployresult-schema - '{"run": "", "name": "", "ci_loop": "", "tags": "",
  "url": "", "catalog_description": "", "tier": "",
  "dependencies": "", "version": "", "criteria": "",
  "domains": "", "trust": "", "blocking": "",
  "description": ""}'


Get
"""

Authentication is not required

.. code-block:: shell

    testapi deployresult get [-cli-arguments] [arguments-value]

.. NOTE::
   List of command line arguments

   * -job-name : Search results using job
   * -build-id : Search results using build id
   * -from : Search results using from date
   * -last : Search results using last date
   * -scenario : Search results using scenario
   * -period : Search results using period
   * -to : Search results using to
   * ---version : Search results using version
   * -criteria : Search results using criteria
   * -installer : Search results using installer
   * -pod-name : Search results using pod
   * -page : Search results using page

Get one
"""""""

Authentication is not required

.. code-block:: shell

    testapi deployresult getone [deployresult_id]

.. NOTE::
   deployresult_id is mandatory.


Scenario
^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario create [-u] [username] [-p] [password] [scenario-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario create [scenario-schema]

.. NOTE::
  scenario-schema - '{"name": "", "installers": []}'


Get
"""

Authentication is not required

.. code-block:: shell

    testapi scenario get [-name] [key-word]

.. NOTE::

 user can use some attributes to reduce the search results. These are not
 mandatory.

   * -name : Backend will use regular expression to search.
   * -project : Search using project name
   * -installer : Search using installer name
   * -version : Search using version name

Get one
"""""""

Authentication is not required

.. code-block:: shell

    testapi scenario getone [name-keyword]

.. NOTE::
   name-keyword is mandatory.

Update
""""""

Authentication required

.. code-block:: shell

    testapi scenario put [-u] [username] [-p] [password] [scenario-name]
    [scenario-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario put [scenario-name] [scenario-schema]

.. NOTE::
  scenario-schema - '{"name": "", "installers": []}'

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi scenario delete [-u] [username] [-p] [password] [scenario-name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario delete [scenario-name]

.. NOTE::
   scenario-name is mandatory.

Scenario installer
^^^^^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario installer create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] [installer-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario installer create --scenario-name [scenario-name]
    [installer-schema]

.. NOTE::
  installer-schema - '{"installer": "", "versions": []}'

Update
""""""

Authentication required

.. code-block:: shell

    testapi scenario installer put [-u] [username] [-p] [password]
    --scenario-name [scenario-name] [installer-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario put --scenario-name [scenario-name] [installer-schema]

.. NOTE::
  scenario-schema - '{"installer": "", "installers": []}'

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi scenario delete [-u] [username] [-p] [password] --scenario-name
    [scenario-name] [name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario delete --scenario-name [scenario-name] [name]

Scenario version
^^^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario version create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] [version-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario installer create --scenario-name [scenario-name]
    --installer [installer] [version-schema]

.. NOTE::
  installer-schema - '{"version": "", "owner": "", "projects": []}'

Update
""""""

Authentication required

.. code-block:: shell

    testapi scenario installer put [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] [version-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario installer put --scenario-name [scenario-name]
    --installer [installer] [installer-schema]

.. NOTE::
  scenario-schema - '{"version": "","owner": "", "projects": []}'

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi scenario installer delete [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] [name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario installer delete  --scenario-name [scenario-name]
    --installer [installer] [name]

Scenario Project
^^^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario project create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer]
    ---version [version] [project-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario project create --scenario-name [scenario-name]
    --installer [installer] ---version [version] [project-schema]

.. NOTE::
  installer-schema - '{"scores": [],"customs": [], "trust_indicators": [],
  project:""}'

Update
""""""

Authentication required

.. code-block:: shell

    testapi scenario project put [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] ---version
    [version] [project-schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario project put --scenario-name [scenario-name] --installer
    [installer] ---version [version] [project-schema]

.. NOTE::
  scenario-schema - '{"scores": [],"customs": [], "trust_indicators": [],
  project:""}'

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi scenario project delete [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] ---version
    [version] [name]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario project delete  --scenario-name [scenario-name]
    --installer [installer] ---version [version] [name]

Scenario Customs
^^^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario custom create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer]
    ---version [version] --project [project] [customs]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario custom create --scenario-name [scenario-name]
    --installer [installer] ---version [version] --project [project] [customs]

.. NOTE::

  customs : Space sperated strings

Update
""""""

Authentication required

.. code-block:: shell

    testapi scenario custom put [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] ---version
    [version] --project [project] [customs]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario custom put --scenario-name [scenario-name] --installer
    [installer] ---version [version] --project [project] [customs]

.. NOTE::

  customs : Space sperated strings

Delete
""""""

Authentication is required

.. code-block:: shell

    testapi scenario custom delete [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer] ---version
    [version] --project [project] [customs]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario custom delete  --scenario-name [scenario-name]
    --installer [installer] ---version [version] --project [project]
    [customs]

.. NOTE::

  customs : Space sperated strings

Scenario Score
^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario score create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer]
    ---version [version] --project [project] [score_schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario score create --scenario-name [scenario-name]
    --installer [installer] ---version [version] --project [project]
    [score_schema]

.. NOTE::

  score_schema : '{"score": "", "date": ""}'

Scenario TrustIndicators
^^^^^^^^^^^^^^^^^^^^^^^^

Create
""""""

Authentication required

.. code-block:: shell

    testapi scenario trustindicator create [-u] [username] [-p] [password]
    --scenario-name [scenario-name] --installer [installer]
    ---version [version] --project [project] [trustindicator_schema]

or

.. code-block:: shell

    $ testapi [-u] [username] [-p] [password]
    (testapi) scenario trustindicator create --scenario-name [scenario-name]
    --installer [installer] ---version [version] --project [project]
    [trustindicator_schema]

.. NOTE::

  trustindicator_schema : '{"status": "", "date": ""}'