pipeline {
    agent {
        label 'generic'
    }
    stages {
        stage("Set up machine") {
            steps {
                sh """
                    pip3 install pytest
                """
            }
        }
        stage('Test code') {
            steps {
                sh """
                    pytest
                """
            }
        }
    }
    post {
        always {
            sh """
                pip3 remove pytest
            """
        }
    }
}