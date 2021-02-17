pipeline {
  agent any
  stages {
    stage('Run Backend_Server') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

    stage('Run Web_Server') {
      steps {
        sh 'nohup python web_app.py &'
      }
    }

    stage('Shutting down Both servers') {
      steps {
        sh 'python clean_environment.py'
      }
    }

  }
}