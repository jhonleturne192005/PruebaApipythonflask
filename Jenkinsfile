pipeline {
    agent any
    stages{
        stage('Build Maven'){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jhonleturne192005/apiproductest']])
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker compose build'
                    sh 'docker compose up -d'
                }
            }
        }
    }
}