pipeline {
    agent any

    environment {
        REG = "192.168.3.236/assettrack"
    }

    stages {

        stage('Login Harbor') {
            steps {
                sh 'docker login 192.168.3.236 -u admin -p Harbor12345'
            }
        }

        stage('Build Base') {
            steps {
                sh '''
                docker build -t $REG/base:latest -f docker/base.Dockerfile .
                docker push $REG/base:latest
                '''
            }
        }

        stage('Build Services') {
            steps {
                script {
                    def services = ["api","agent","collector","processor","webapp"]
                    for (s in services) {
                        sh """
                        docker build -t $REG/${s}:v1 -f docker/${s}.Dockerfile .
                        docker push $REG/${s}:v1
                        """
                    }
                }
            }
        }
    }
}
