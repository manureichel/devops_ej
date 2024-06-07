pipeline {
    environment {
        registry = "manureichel/devops_ej"
        registryCredential = 'dockerhub_id'
        dockerImage = "${registry}:${BUILD_NUMBER}"
        containerName = "my_app_container"
    }
    agent any
    stages {
        stage('Building image with Buildah') {
            steps {
                sh """
                    buildah bud -t ${dockerImage} .
                """
            }
        }
        stage('Push Image with Buildah') {
            steps {
                withCredentials([usernamePassword(credentialsId:registryCredential, passwordVariable:"dockerpass", usernameVariable:"dockeruser")]){
                    sh "buildah push --tls-verify=false --creds=${dockeruser}:${dockerpass} ${dockerImage} docker://docker.io/${dockerImage}"
                }
            }
        }
        stage('Deploy') {
            steps{
                sh "docker rm -f devops_ej"
                sh "docker run -d -p 3000:80 --name devops_ej ${dockerImage}"
                sh "docker ps -f name=devops_ej"
                }
            }
    }
}