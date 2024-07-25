pipeline {
    agent any

    environment {
        DOCKER_REPO = 'your-docker-repo'
        IMAGE_NAME = 'your-app-name'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REPO}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://your-registry-url', 'your-registry-credentials-id') {
                        docker.image("${DOCKER_REPO}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                        docker.image("${DOCKER_REPO}/${IMAGE_NAME}:${IMAGE_TAG}").push('latest')
                    }
                }
            }
        }
    }
