pipeline {
    environment {
        registry = "manureichel/devops_ej"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning from Github') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/manureichel/devops_ej.git'
            }
        }
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Run Container') {
            steps{
                sh "docker rm -f devops_ej"
                sh "docker run -d -p 3000:80 --name devops_ej $registry:$BUILD_NUMBER"
                sh "docker ps -f name=devops_ej"
                }
            }
        stage('Deploy image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker rmi ${registry}:${BUILD_NUMBER}"
            }
        }
    }
}
