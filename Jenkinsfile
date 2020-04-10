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
                    python3 -m pytest
                """
            }
        }
    }
    post {
        always {
            sh """
                pip3 uninstall pytest -y
            """
        }
    }
}