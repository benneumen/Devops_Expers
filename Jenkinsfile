pipeline {
  agent any
  stages {
    stage('Create txt file') {
      steps {
        sh 'python --version'
        sh '''python Create_text_file.py
'''
      }
    }

    stage('Read text file ') {
      steps {
        sh 'python Read_text_file.py'
      }
    }

  }
}