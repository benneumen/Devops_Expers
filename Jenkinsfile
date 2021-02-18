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

  }
}