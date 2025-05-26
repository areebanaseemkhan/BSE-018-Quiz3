python
print("Hello from Python!")


* Add a *Jenkinsfile*:

groovy
pipeline {
    agent any
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 hello.py'
            }
        }
    }
}