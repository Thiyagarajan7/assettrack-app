pipeline {
    agent any

    environment {
        REGISTRY = "192.168.3.236/assettrack"
        HARBOR_CREDS = credentials('harbor-creds')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Thiyagarajan7/assettrack-app.git'
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                echo $HARBOR_CREDS_PSW | docker login 192.168.3.236 \
                -u $HARBOR_CREDS_USR --password-stdin
                '''
            }
        }

        stage('Build Base Image') {
            steps {
                sh '''
                docker build -t $REGISTRY/base:latest -f docker/base.Dockerfile .
                docker push $REGISTRY/base:latest
                '''
            }
        }

        stage('Build Services') {
            steps {
                script {
                    def services = ["api","agent","collector","processor","webapp"]
                    for (svc in services) {
                        sh """
                        docker build -t $REGISTRY/${svc}:v1 -f docker/${svc}.Dockerfile .
                        docker push $REGISTRY/${svc}:v1
                        """
                    }
                }
            }
        }
    }
}
