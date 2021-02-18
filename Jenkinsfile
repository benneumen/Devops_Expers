pipeline {
  agent any
  stages {
    stage('Initiate Git ') {
      steps {
        git(url: 'https://github.com/benneumen/Devops_Expers.git', poll: true)
      }
    }

    stage('Git initiated Msg') {
      steps {
        echo 'Git successfully initiated'
      }
    }

    stage('Start rest_app') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

    stage('Start web_app') {
      steps {
        sh 'nohup python web_app.py &'
      }
    }

    stage('Terminate both servers') {
      steps {
        sh 'python clean_environment.py'
      }
    }

  }
}