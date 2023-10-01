pipeline {
    environment {
    registry = "osas23"
    registryCredential = 'docker_hub'
    dockerimage = ''
    }
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/osa20/devops-project.git'
            }
        }

        stage('Install python packages') {
             steps {
                script {
                    if (isUnix()) {
                        //Unix/MacOS/Linux Environment
                        sh 'pip install --user -r requirements.txt'
                    }
                    else {
                        //Windows Environment
                        bat 'pip install --user -r requirements.txt'
                    }
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
//         stage('Build and push image') {
//             steps {
//                 script {
//                     dockerimage = docker.build registry + "$BUILD_NUMBER"
//                     docker.withRegistry('', registryCredential) {
//                         dockerimage.push()
//                     }
//                 }
//             }
//             post {
//                 always {
//                     bat "docker rmi $BUILD_NUMBER"
//                 }
//             }
//         }
//         stage('Set version') {
//             steps {
//                 script {
//                     if (isUnix()) {
//                          sh "echo IMAGE_TAG=${BUILD_NUMBER}>.env"
//                     }
//                     else {
//                         bat "echo IMAGE_TAG=${BUILD_NUMBER}>.env"
//                     }
//                 }
//             }
//         }
        stage('Run containers') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker-compose build"
                        sh "docker-compose up -d"
                    }
                    else {
                        bat "docker-compose build"
                        bat "docker-compose up -d"
                    }
                }
            }
        }
        stage('Delete local images and containers') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker-compose down"
                        sh "docker-compose down --rmi all"
                    }
                    else {
                        sh "docker-compose down"
                        bat "docker-compose down --rmi all"
                    }
                }
            }
        }
    }
}