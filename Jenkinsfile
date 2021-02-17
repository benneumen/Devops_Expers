pipeline {
  agent any
  stages {
    stage('Run Backend_Server') {
      steps {
        sh 'nohup python clean_environment.py &'
      }
    }

  }
}
