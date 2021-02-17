pipeline {
  agent any
  stages {
    stage('Run Backend_Server') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

  }
}