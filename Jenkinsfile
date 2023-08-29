pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Checkout Git Repo') {
            steps {
                git 'https://github.com/osa20/devops-project-first.git'
            }
        }
        stage('Install Python Packages') {
            steps {
                bat 'pip install --user -r requirements.txt'
            }
        }
        stage('Run Backend Server') {
            steps {
                script {
                    bat 'start/min python rest_app.py'
                }
            }
        }
        stage('Run Frontend Server') {
            steps {
                script {
                    bat 'start/min python web_app.py'
                }
            }
        }
        stage('Run Backend Testing') {
            steps {
                script {
                    bat 'python backend_testing.py'
                }
            }
        }
        stage('Run Frontend Testing') {
            steps {
                script {
                    bat 'python frontend_testing.py'
                }
            }
        }
        stage('Run Clean Environment') {
            steps {
                script {
                    bat 'python clean_environment.py'
                }
            }
        }
    }
}