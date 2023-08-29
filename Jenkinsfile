pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/osa20/devops-project-first.git'
            }
        }
        stage('run backend server') {
            steps {
                script {
                    bat 'start/min python rest_app.py'
                }
            }
        }
        stage('run frontend server') {
            steps {
                script {
                    bat 'start/min python web_app.py'
                }
            }
        }
        stage('run backend testing') {
            steps {
                script {
                    bat 'backend_testing.py'
                }
            }
        }
        stage('run frontend testing') {
            steps {
                script {
                    bat 'frontend_testing.py'
                }
            }
        }
        stage('run clean environment') {
            steps {
                script {
                    bat 'clean_environment.py'
                }
            }
        }
    }
}