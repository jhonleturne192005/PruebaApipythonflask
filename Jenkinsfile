pipeline {
    agent any
    environment {
        PROGRAM = credentials('programidname')
    }
    stages{
        stage('Build Maven'){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jhonleturne192005/PruebaApipythonflask']])
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker compose build'
                    sh 'docker compose up'
                }
            }
        }
    }
}