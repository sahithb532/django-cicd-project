pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Migrate Database') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py migrate
                '''
            }
        }

        stage('Build Success') {
            steps {
                echo 'Deployment Successful'
            }
        }
    }
}
