pipeline {
    agent 'generic'
    stages {
        stage('Test code') {
            sh """
                pytest
            """
        }
    }
}