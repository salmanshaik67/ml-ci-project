pipeline {
    agent any

    stages {
        stage('Debug Python Environment') {
            steps {
                bat 'echo === Checking Python and Pip ==='
                bat 'where python'
                bat 'python --version'
                bat 'where pip'
                bat 'pip --version'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'echo === Installing Python Requirements ==='
                bat 'python -m pip install --upgrade pip setuptools wheel'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                bat 'python predict_failures.py'
            }
        }

        stage('Predict Likely Failures') {
            steps {
                bat 'python flag_likely_failures.py'
            }
        }

        stage('Run Sanity Tests') {
            steps {
                bat 'pytest sanity_tests.py'
            }
        }
    }
}
