node {
	     
	    def mvnHome = tool 'maven-3.6.3'
	    def dockerImage
	    def dockerImageTag = "pracainzynierka${env.BUILD_NUMBER}"
	    
	    stage('Clone Repo') { 
	      git 'https://github.com/patrmus054/papryk-inzynier.git'
         
	      mvnHome = tool 'maven-3.6.3'
	    }    
	  
	    stage('Build Project') {
            sh "cd gs-rest-service"
	      sh "'${mvnHome}/bin/mvn' clean install"
	    }
			
	    stage('Build Docker Image') {
	      dockerImage = docker.build("pracainzynierka:${env.BUILD_NUMBER}")
	    }
	   
	    stage('Deploy Docker Image'){
	      echo "Docker Image Tag Name: ${dockerImageTag}"
		  sh "docker stop pracainzynierka"
		  sh "docker rm pracainzynierka"
		  sh "docker run --name pracainzynierka -d -p 2222:2222 pracainzynierka:${env.BUILD_NUMBER}"
	    }
}