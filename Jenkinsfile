pipeline {
    agent any
    environment {
        // no vale directo para usarla en el proyecto python debido a que la aplicacion python corre bajo contenedor docker y queda fuera del scope de Jenkins, por eso se debe agg en docker-compose.yml mediante sus environment variables
        PROGRAM = credentials('programidname') 
    }
    stages{
        stage('Build Maven'){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jhonleturne192005/PruebaApipythonflask']])
            }
        }
        stage('configuration env file'){ {
            steps {
                withCredentials([file(credentialsId: 'envfile', variable: 'ENV_FILE')]) {
                    sh 'cp "$ENV_FILE" .env'
                }
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