// For linux

// pipeline {
//     agent any
//     stages {
//         stage('Install Requirements') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }
//         stage('Train ML Model') {
//             steps {
//                 sh 'python predict_failures.py'
//             }
//         }
//         stage('Predict Likely Failures') {
//             steps {
//                 sh 'python flag_likely_failures.py'
//             }
//         }
//         stage('Run Sanity Tests') {
//             steps {
//                 sh 'pytest sanity_tests.py'
//             }
//         }
//     }
// }

// For windows

pipeline {
    agent any
    stages {
        stage('Install Requirements') {
            steps {
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

