pipeline {
  agent any
  stages {
    stage('Pull Git') {
      steps {
        git(url: 'https://github.com/benneumen/Devops_Expers.git', branch: 'master')
      }
    }

    stage('Run Backend_Server') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

  }
}