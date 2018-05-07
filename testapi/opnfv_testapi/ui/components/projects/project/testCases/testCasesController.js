/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function () {
    'use strict';

    angular
        .module('testapiApp')
        .controller('TestCasesController', TestCasesController);

        TestCasesController.$inject = [
        '$scope', '$http', '$filter', '$state', '$window', '$uibModal', 'testapiApiUrl','raiseAlert',
        'confirmModal', 'authenticate', '$timeout'
    ];

    /**
     * TestAPI Test cases Controller
     * This controller is for the tescases page where a user can browse
     * through testcases declared in TestAPI and perform the CRUD operations
     * in them.
     */
    function TestCasesController($scope, $http, $filter, $state, $window, $uibModal, testapiApiUrl,
        raiseAlert, confirmModal, authenticate, $timeout) {
        var ctrl = this;
        ctrl.loadDetails = loadDetails;
        ctrl.name = $state.params['name'];
        ctrl.requestUrl = testapiApiUrl + '/projects/' + ctrl.name +'/cases';

        ctrl.createTestCase = createTestCase;
        ctrl.openCreateModal = openCreateModal;
        ctrl.deleteTestCase = deleteTestCase;
        ctrl.openDeleteTestModal = openDeleteTestModal;
        ctrl.updateTestCase = updateTestCase;
        ctrl.openUpdateTestModal = openUpdateTestModal;
        ctrl.batchDelete = batchDelete;
        ctrl.openBatchDeleteModal = openBatchDeleteModal;
        ctrl.viewTestCase = viewTestCase;

        ctrl.checkBox = [];
        ctrl.checkBoxList = [];
        ctrl.toastError = toastError
        ctrl.toastSuccess = toastSuccess

        function toastError() {
            ctrl.showError = true
            $timeout(function(){ ctrl.showError = false;}, 3000);
        }

        function toastSuccess() {
            ctrl.showSuccess = true
            $timeout(function(){ ctrl.showSuccess = false;}, 3000);
        }

        /**
         * This will contact the TestAPI to create a new test case.
         */
        function createTestCase(name, testcase) {
            if(testcase.name != "" && testcase.name!=null){
                var testCase_url = ctrl.requestUrl;
                ctrl.testCasesRequest = $http.post(testCase_url, testcase)
                ctrl.testCasesRequest.success(function (data){
                        ctrl.success = "Testcase is successfully created."
                        loadDetails();
                        ctrl.toastSuccess()
                    })
                    .catch(function (data) {
                        ctrl.error = data.statusText;
                        ctrl.toastError();
                    });
                return ctrl.testCasesRequest;
            }
            else{
                ctrl.error = 'Name is missing.'
                ctrl.toastError();
            }
        }

        function viewTestCase(name, project_name){
            $state.go('testCase', {'name':name, 'project_name':project_name}, {reload: true});
        }

        /**
         * This will open the modal that will show the batch delete confirm
         * message
         */
        function openBatchDeleteModal() {
            var deleteObjects = []
            ctrl.checkBox.forEach(function(testcase, index){
                if(!ctrl.showError){
                    if(testcase){
                        deleteObjects.push(ctrl.data.testcases[index].name)
                    }
                }
              });
            confirmModal("Delete", 'testcases', ctrl.batchDelete, deleteObjects);
        }

        /**
         * This will  delete list of test cases.
         */
        function batchDelete(){
            var index;
            var checkedBox = [];
            ctrl.checkBox.forEach(function(testcase, index){
                if(!ctrl.showError){
                    if(testcase){
                        ctrl.deleteTestCase(ctrl.data.testcases[index].name);
                    }
                }
              });
            ctrl.checkBox = []
        }
        /**
         * This will contact the TestAPI to update an existing test case.
         */
        function updateTestCase(name, testCase) {
            if(testCase.name != ""){
                var testCase_url = ctrl.requestUrl + '/' + name;
                ctrl.testCasesRequest = $http.put(testCase_url, testCase)
                ctrl.testCasesRequest.success(function (data){
                        ctrl.success = "Test case is successfully updated"
                        loadDetails();
                        ctrl.toastSuccess();
                    })
                    .catch(function (data) {
                        ctrl.error = data.statusText;
                        ctrl.toastError()
                    });
                return ctrl.testCasesRequest;
            }
            else{
                ctrl.error = 'Name is missing.'
                ctrl.toastError()
            }
        }

        /**
         * This will contact the TestAPI to delete an existing test case.
        */
        function deleteTestCase(name) {
            ctrl.testCasesRequest =
            $http.delete(ctrl.requestUrl+"/"+name).success(function (data) {
                loadDetails();
                ctrl.success = "Test case is successfully deleted";
                ctrl.toastSuccess();
            }).catch(function (error) {
                ctrl.error = error.statusText;
                ctrl.toastError();
            });
        }

        /**
         * This will open the modal that will show the delete confirm
         * message
         */
        function openDeleteTestModal(name) {
            confirmModal("Delete",  'testcases', ctrl.deleteTestCase, name);
        }

        /**
         * This will open the modal that will show the Create
         * view
         */
        function openCreateModal(name){
                $uibModal.open({
                    templateUrl: 'testapi-ui/components/projects/project/testCases/modals/testCaseModal.html',
                    controller: 'TestCaseModalCtrl as TestCaseModalCtrl',
                    size: 'md',
                    resolve: {
                        data: function () {
                            return {
                                text: "Create",
                                successHandler: ctrl.createTestCase
                            };
                        }
                    }
                });
        }

        /**
         * This will open the modal that will show the update
         * view
         */
        function openUpdateTestModal(name){
            var testcase;
            var index;
            for(index in ctrl.data.testcases){
                if(ctrl.data.testcases[index].name==name){
                    testcase = ctrl.data.testcases[index]
                    continue
                }
            }
            $uibModal.open({
                templateUrl: 'testapi-ui/components/projects/project/testCases/modals/testCaseModal.html',
                controller: 'TestCaseModalCtrl as TestCaseModalCtrl',
                size: 'md',
                resolve: {
                    data: function () {
                        return {
                            text: "Update",
                            successHandler: ctrl.updateTestCase,
                            testCase: testcase
                        };
                    }
                }
            });
        }

        /**
         * This will contact the TestAPI to get a listing of declared test cases.
         */
        function loadDetails() {
            ctrl.testCasesReguest =
                $http.get(ctrl.requestUrl).success(function (data) {
                    ctrl.data = data;
                }).catch(function (error) {
                    ctrl.data = null;
                    ctrl.error = error.statusText;
                    ctrl.toastError()
                });
        }
        ctrl.loadDetails();
    }


    /**
     * TestAPI Modal instance Controller
     * This controller is for the modal where a user can create
     * test case or update the test case information.
     */
    angular.module('testapiApp').controller('TestCaseModalCtrl', TestCaseModalCtrl);
    TestCaseModalCtrl.$inject = ['$scope', '$uibModalInstance', 'data'];
    function TestCaseModalCtrl($scope, $uibModalInstance, data) {
        var ctrl = this;
        ctrl.confirm = confirm;
        ctrl.cancel = cancel;
        ctrl.data = angular.copy(data);

        ctrl.createRequirements = [
            {label: 'name', type: 'text', required: true},
            {label: 'description', type: 'textarea', required: false},
            {label: 'version', type: 'text', required: false},
            {label: 'tier', type: 'text', required: false},
            {label: 'tags', type: 'text', required: false},
            {label: 'run', type: 'text', required: false},
            {label: 'dependencies', type: 'text', required: false},
            {label: 'trust', type: 'text', required: false},
            {label: 'url', type: 'text', required: false},
            {label: 'blocking', type: 'text', required: false},
            {label: 'criteria', type: 'text', required: false},
            {label: 'domains', type: 'text', required: false},
            {label: 'ci_loop', type: 'text', required: false},
            {label: 'catalog_description', type: 'text', required: false}
        ];

        ctrl.testcase = {name : null, description : null,version : null, tier : null, tags : null,
                     run : null, dependencies : null, trust : null, url : null, blocking : null,
                 criteria : null, domains : null, ci_loop: null,  catalog_description : null};

        if(ctrl.data.text=="Update"){
            ctrl.testcase = ctrl.data.testCase
            delete ctrl.testcase._id;
            ctrl.name = ctrl.data.testCase.name
        }

        /**
         * Initiate confirmation and call the success handler with the
         * inputs.
         */
        function confirm() {
            if (angular.isDefined(ctrl.data.successHandler)) {
                if(ctrl.testcase.name){
                    ctrl.data.successHandler(ctrl.name, ctrl.testcase).success( function(){
                        $uibModalInstance.close();
                    })
                }
                else{
                    ctrl.data.successHandler(ctrl.name, ctrl.testcase)
                }
            }
        }

        /**
         * Close the confirm modal without initiating changes.
         */
        function cancel() {
            $uibModalInstance.dismiss('cancel');
        }
    }
})();
