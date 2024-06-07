pipeline {
    environment {
        registry = "manureichel/devops_ej"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps{
                sh "docker rm -f devops_ej"
                sh "docker run -d -p 3000:80 --name devops_ej $registry:$BUILD_NUMBER"
                sh "docker ps -f name=devops_ej"
                }
            }
    }
}
