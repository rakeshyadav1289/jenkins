pipeline{
    agent rakesh
    
    stages {
        // git clone stage
        stage("this is git clone stage") {
            steps{
                echo "I going to git clone"
                git branch: 'main', url: 'https://github.com/rakeshyadav1289/jenkins.git'
            }
        }
        
        stage("building docker images") {
            steps{
                echo "building docker images using Dockerfile"
                sh 'docker build -t flask-docker-app .'
                
            }
        }
        
        stage("depolye Docker images using images") {
            steps{
                echo "Runing docker contianer "
                // stop docker container if docker already runing
                sh 'docker stop flask-container || true && docker rm flask-container || true'
                // if docker container not running then run docker container
                sh 'docker run -d -p 5000:5000 --name flask-container flask-docker-app'
                
            }
        }
      
    }
}
