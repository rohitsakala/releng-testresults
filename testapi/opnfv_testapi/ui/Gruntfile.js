
module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);
    require('grunt-protractor-coverage')(grunt);
    grunt.loadNpmTasks('grunt-shell-spawn');
    grunt.loadNpmTasks('grunt-wait');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-convert');
    grunt.initConfig({
        convert: {
            options: {
              explicitArray: false,
            },
            json2xml: {
                options: {
                    xml: {
                      header: true
                    }
                  },
              src: ['../tests/UI/coverage/coverage.json'],
                  dest: '../tests/UI/coverage/coverage.xml'
            }
        },
        connect: {
            server: {
                options: {
                    port: 8000,
                    base: './',
                    middleware: function(connect, options, middlewares) {
                        middlewares.unshift(function(req, res, next) {
                            if (req.method.toUpperCase() == 'POST' || req.method.toUpperCase() == "PUT" ||
                                req.method.toUpperCase() == "DELETE")
                                {
                                    req.method='GET';
                                }
                            return next();
                        });
                        return middlewares;
                    }
                }
            }
        },
        copy: {
            assets: {
              expand: true,
              cwd: '../../3rd_party/static/testapi-ui/assets',
              src: '**',
              dest: 'testapi-ui/assets',
            },
            components: {
                expand: true,
                cwd: 'components',
                src: '**',
                dest: 'testapi-ui/components',
            },
            shared: {
                expand: true,
                cwd: 'shared',
                src: '**',
                dest: 'testapi-ui/shared',
            },
            filesPng: {
                expand: true,
                src: '*.png',
                dest: 'testapi-ui/',
            },
            filesIco: {
                expand: true,
                src: '*.ico',
                dest: 'testapi-ui/',
            },
            filesJs: {
                expand: true,
                src: 'app.js',
                dest: 'testapi-ui/',
            },
            filesJson: {
                expand: true,
                src: 'config.json',
                dest: 'testapi-ui/',
            }
        },
        wait: {
            default: {
                options: {
                    delay: 3000
                }
            }
        },
        shell: {
            updateSelenium: {
                command: 'node_modules/protractor/bin/webdriver-manager update',
                options: {
                      async: false
                }
            },
            startSelenium: {
                command: 'node_modules/protractor/bin/webdriver-manager start',
                options: {
                  async: true
                }
            },
            deleteFiles: {
                command: 'rm -r testapi-ui',
                options: {
                  async: false
                }
            },
            options: {
                stdout: false,
                stderr: false
            }
        },
        instrument: {
            files: ['components/**/*.js'],
            options: {
                lazy: false,
                basePath: "./testapi-ui/"
            }
        },
        karma: {
            unit: {
                configFile: 'karma.conf.js'
            }
        },
        protractor_coverage: {
            options: {
                keepAlive: false,
                noColor: false,
                coverageDir: '../tests/UI/coverage',
                args: {
                    specs: [
                            '../tests/UI/e2e/homeControllerSpec.js',
                            '../tests/UI/e2e/podsControllerSpec.js',
                            '../tests/UI/e2e/projectsControllerSpec.js',
                            '../tests/UI/e2e/testCasesControllerSpec.js',
                            '../tests/UI/e2e/resultsControllerSpec.js',
                            '../tests/UI/e2e/scenariosControllerSpec.js',
                            '../tests/UI/e2e/scenarioControllerSpec.js',
                            '../tests/UI/e2e/deployResultsControllerSpec.js',
                            '../tests/UI/e2e/authenticateFalseSpec.js'
                        ]
                }
            },
            local: {
                options: {
                    configFile: 'protractor-conf.js'
                }
            }
        },
        makeReport: {
            src: '../tests/UI/coverage/*.json',
            options: {
               	dir: '../tests/UI/coverage'
            }
        }
    });
    grunt.registerTask('test', [
        'karma:unit'
    ]);

    grunt.registerTask('forceOn', 'turns the --force option ON',
    function() {
      if ( !grunt.option( 'force' ) ) {
        grunt.config.set('forceStatus', true);
        grunt.option( 'force', true );
      }
    });

  grunt.registerTask('forceOff', 'turns the --force option Off',
    function() {
      if ( grunt.config.get('forceStatus') ) {
        grunt.option( 'force', false );
      }
    });

    grunt.registerTask('e2e', [
        'copy:assets',
        'copy:components',
        'copy:shared',
        'copy:filesPng',
        'copy:filesIco',
        'copy:filesJs',
        'copy:filesJson',
        'instrument',
        'connect',
        'shell:updateSelenium',
        'shell:startSelenium',
        'wait:default',
        'forceOn',
        'protractor_coverage',
        'forceOff',
        'makeReport',
        'convert',
        'shell:deleteFiles'
    ]);
}
