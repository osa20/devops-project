pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
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
                if (isUnix()) {
                    //Linux Environment
                    sh 'pip install --user -r requirements.txt'
                }
                else {
                    //Windows Environment
                    bat 'pip install --user -r requirements.txt'
                }
            }
        }
        stage('Run backend server') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'nohup python rest_app.py &'
                    }
                    else {
                        bat 'start/min python rest_app.py'
                    }
                }
            }
        }
        stage('Run frontend server') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'nohup python web_app.py &'
                    }
                    else {
                        bat 'start/min python web_app.py'
                    }
                }
            }
        }
        stage('Run backend testing') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python backend_testing.py'
                    }
                    else {
                        bat 'python backend_testing.py'
                    }
                }
            }
        }
        stage('Run frontend testing') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python frontend_testing.py'
                    }
                    else {
                        bat 'python frontend_testing.py'
                    }
                }
            }
        }
        stage('Run combined testing') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python combined_testing.py'
                    }
                    else {
                        bat 'python combined_testing.py'
                    }
                }
            }
        }
        stage('Run clean environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python clean_environment.py'
                    }
                    else {
                        bat 'python clean_environment.py'
                    }
                }
            }
        }
    }
}