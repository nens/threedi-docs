node(3di) {
    stage('Checkout') {
        checkout scm
    }
    stage('Build') {
        sh "docker-compose down --volumes --remove-orphans"
        sh "docker-compose build"
    }
    stage('Cleanup') {
        sh "docker-compose down --volumes"
    }
}
