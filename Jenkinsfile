pipeline {
  agent any
  stages {
    stage('Initiate Git ') {
      steps {
        git(url: 'https://github.com/benneumen/Devops_Expers.git', poll: true)
        echo 'Git successfully initiated'
      }
    }

    stage('Start rest_app') {
      parallel {
        stage('Start rest_app') {
          steps {
            sh 'nohup python3 rest_app.py &'
          }
        }

        stage('rest_app ERROR') {
          steps {
            echo 'Failed to start rest_app server'
          }
        }

      }
    }

    stage('Start web_app') {
      parallel {
        stage('Start web_app') {
          steps {
            sh 'nohup python3 web_app.py &'
          }
        }

        stage('web_app ERROR') {
          steps {
            echo 'Failed to start web_app server'
          }
        }

      }
    }

    stage('Run Backend test') {
      steps {
        sh 'python3 backend_testing.py'
      }
    }

    stage('Run Frontend test') {
      steps {
        sh 'python3 frontend_testing.py'
      }
    }

    stage('Run Combined test') {
      steps {
        sh 'python3 combined_testing.py'
      }
    }

    stage('Clean environment') {
      steps {
        sh 'python3 clean_environment.py'
      }
    }

  }
}