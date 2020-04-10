pipeline {
    agent {
        label 'generic'
    }
    stages {
        stage('Test code') {
            steps {
                sh """
                    pytest
                """
            }
        }
    }
}