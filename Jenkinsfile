pipeline {
    agent {
        docker {
            image 'python:3.7.0'

        }
    }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m pip install -r lemudim1/requirements.txt --user"
                }
            }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    dir("lemudim1/classmanager"){
                        sh "python manage.py test"
                    }
                }
            }
        }
    }
