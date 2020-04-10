pipeline {
    agent {
        label 'generic'
    }
    stages {
        stage("Set up machine") {
            steps {
                sh """
                    pip install pytest
                """
            }
        }
        stage('Test code') {
            steps {
                sh """
                    python -m pytest
                """
            }
        }
    }
    post {
        always {
            sh """
                pip uninstall pytest -y
            """
        }
    }
}