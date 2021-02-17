pipeline {
  agent any
  stages {
    stage('Create txt file') {
      steps {
        sh '''\'python.exe Create_text_file.py\'
'''
      }
    }

    stage('Read text file ') {
      steps {
        sh '''f = open("/Users/benn/Desktop/text_file.txt", "r" )
print(f.read())'''
      }
    }

  }
}