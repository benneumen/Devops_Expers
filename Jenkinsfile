pipeline {
  agent any
  stages {
    stage('initiate git ') {
      steps {
        git(url: 'https://github.com/benneumen/Devops_Expers.git', poll: true)
      }
    }

    stage('Git initiated Msg') {
      steps {
        echo 'Git successfully initiated'
      }
    }

    stage('start rest_app server') {
      steps {
        sh 'nohup python rest_app.py &'
      }
    }

  }
}