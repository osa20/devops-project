pipeline {
    agent any
    triggers {
        pollSCM('H/30 * * * *')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
//     environment {
//         registry = "osas23"
//         registryCredential = 'docker_hub'
//         dockerimage = ''
//     }

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
        stage('Run a local MySQL Container') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --name mysql -v C:/Users/osame/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3309:3306 -d mysql:8.0.33'
                    }
                    else {
                        bat 'docker run --name mysql -v C:/Users/osame/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=mysql -e MYSQL_DATABASE=mydb -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3309:3306 -d mysql:8.0.33'
                    }
                }
            }
        }
        stage('Create database table and populate it') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python db_connector.py'
                    }
                    else {
                        bat 'python db_connector.py'
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
        stage('Delete local MySQL container and image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker stop mysql"
                        sh "docker rm mysql"
                        sh "docker rmi mysql:8.0.33"
                    }
                    else {
                        bat "docker stop mysql"
                        bat "docker rm mysql"
                        bat "docker rmi mysql:8.0.33"
                    }
                }
            }
        }
        stage('Build docker-compose images') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker-compose build"
                    }
                    else {
                        bat "docker-compose build"
                    }
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker login"
                    }
                    else {
                        bat "docker login"
                    }
                }
            }
        }
        stage('Push docker-compose images to Docker Hub') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker tag project_third-rest_app osas23/rest_app"
                        sh "docker tag project_third-backend_testing_app osas23/backend_testing_app"
                        sh "docker push osas23/rest_app"
                        sh "docker push osas23/backend_testing_app"
                    }
                    else {
                        bat "docker tag project_third-rest_app osas23/rest_app"
                        bat "docker tag project_third-backend_testing_app osas23/backend_testing_app"
                        bat "docker push osas23/rest_app"
                        bat "docker push osas23/backend_testing_app"
                    }
                }
            }
            post {
                always {
                    sh 'docker logout'
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
                        sh "docker-compose up -d"
                    }
                    else {
                        bat "docker-compose build"
                    }
                }
            }
        }
//         stage('Delete local images and containers') {
//             steps {
//                 script {
//                     if (isUnix()) {
//                         sh "docker-compose stop"
//                         sh "docker-compose down"
//                         sh "docker-compose down --rmi all -v --remove-orphans"
//                     }
//                     else {
//                         bat "docker-compose stop"
//                         bat "docker-compose down"
//                         bat "docker-compose down --rmi all -v --remove-orphans"
//                     }
//                 }
//             }
//         }
    }
}