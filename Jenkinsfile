pipeline {
  agent any
    options {
    buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
  }
  stages {
    stage('checkout') {
        steps {
            script {
                properties([pipelineTriggers([pollSCM('* * * * *')])])
              }
              git 'https://github.com/benneumen/Devops_Expers.git'
          }
    }

    stage('Start rest_app') {
        steps {
              sh 'nohup python3 rest_app.py &'
          }
    }

    stage('Start web_app') {
      steps {
        sh 'nohup python3 web_app.py &'
      }
    }

    stage('Run Backend test') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }

    stage('Run Frontend test') {
      steps {
        sh 'python3 frontend_testing.py'
      }
    }

    stage('Run Combined test') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }

    stage('Clean environment') {
      steps {
        sh 'python3 clean_environment.py'

      }
    }

  }
}