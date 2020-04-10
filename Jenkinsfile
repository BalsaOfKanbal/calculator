pipeline {
    agent 'generic'
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