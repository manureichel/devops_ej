pipeline {
    environment {
        registry = "manureichel/devops_ej"
        registryCredential = 'dockerhub_id'
        dockerImage = "${registry}:${BUILD_NUMBER}"
        containerName = "my_app_container"
        discord_webhook = credentials('discord_webhook')
    }
    agent any
    stages {
        stage('Build') {
            steps {
                sh """
                    buildah bud -t ${dockerImage} .
                """
            }
            post {
                success {
                    sendDiscordNotification("finalizó correctamente")
                }
                failure {
                    sendDiscordNotification("finalizó con errores")
                }
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId:registryCredential, passwordVariable:"dockerpass", usernameVariable:"dockeruser")]){
                    sh "buildah push --tls-verify=false --creds=${dockeruser}:${dockerpass} ${dockerImage} docker://docker.io/${dockerImage}"
                }
            }
            post {
                success {
                    sendDiscordNotification("finalizó correctamente")
                }
                failure {
                    sendDiscordNotification("finalizó con errores")
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
            post {
                success {
                    sendDiscordNotification("finalizó correctamente")
                }
                failure {
                    sendDiscordNotification("finalizó con errores")
                }
            }
    }
}

def sendDiscordNotification(msg) {
    discordSend description: "El stage ${STAGE_NAME} ${msg}", 
                result: currentBuild.currentResult, 
                title: JOB_NAME, 
                webhookURL: env.DISCORD_WEBHOOK
}