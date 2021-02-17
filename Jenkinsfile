pipeline {
  agent any
  stages {
    stage('Create txt file') {
      steps {
        sh '''with open(\'/Users/benn/Desktop/text_file.txt\', \'w\') as f:
    data = \'some data to be written to the file\'
    f.write(data)'''
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