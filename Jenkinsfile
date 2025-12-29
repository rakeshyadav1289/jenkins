pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your repository
                git ''
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the image using the Dockerfile
                sh 'docker build -t flask-docker-app .'
            }
        }

        stage('Run Container') {
            steps {
                // Stop and remove existing container if running to prevent port conflicts
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                // Run the new container
                sh 'docker run -d -p 5000:5000 --name flask-container flask-docker-app'
            }
        }
    }
}
