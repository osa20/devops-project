pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Code pull') {
            steps {
                git 'https://github.com/osa20/devops-project-first.git'
            }
        }
        stage('Install python packages') {
             steps {
                bat 'pip install --user -r requirements.txt'
            }
        }
        stage('Run backend server') {
            steps {
                script {
                    bat 'start/min python rest_app.py'
                }
            }
        }
        stage('Run frontend server') {
            steps {
                script {
                    bat 'start/min python web_app.py'
                }
            }
        }
        stage('Run backend testing') {
            steps {
                script {
                    bat 'python backend_testing.py'
                }
            }
        }
        stage('Run frontend testing') {
            steps {
                script {
                    bat 'python frontend_testing.py'
                }
            }
        }
        stage('Run combined testing') {
            steps {
                script {
                    bat 'python combined_testing.py'
                }
            }
        }
        stage('Run clean environment') {
            steps {
                script {
                    bat 'python clean_environment.py'
                }
            }
        }
    }
}