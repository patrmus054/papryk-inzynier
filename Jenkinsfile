node {
	    // reference to maven
	    // ** NOTE: This 'maven-3.5.2' Maven tool must be configured in the Jenkins Global Configuration.   
	    def mvnHome = tool 'maven-3.6.3'
	
	    // holds reference to docker image
	    def dockerImage
	    // ip address of the docker private repository(nexus)
	 
	    def dockerImageTag = "pracainzynierka${env.BUILD_NUMBER}"

		def DOCKER_FILES_DIR = "./initial"
	    
	    stage('Clone Repo') { // for display purposes
	      // Get some code from a GitHub repository
	      git 'https://github.com/patrmus054/papryk-inzynier.git'
	      // Get the Maven tool.
	      // ** NOTE: This 'maven-3.5.2' Maven tool must be configured
	      // **       in the global configuration.           
	      mvnHome = tool 'maven-3.6.3'
	    }    
	  
	    stage('Build Project') {
	      // build project via maven
	      sh "'${mvnHome}/bin/mvn' clean install -f ./initial/pom.xml"
	    }
			
	    stage('Build Docker Image') {
	      // build docker image
	      dockerImage = docker.build("pracainzynierka:${env.BUILD_NUMBER}", "-f ${DOCKER_FILES_DIR}/${dockerfile} ${DOCKER_FILES_DIR}")
	    }
	   
	    stage('Deploy Docker Image'){
	      
	      // deploy docker image to nexus
			
	      echo "Docker Image Tag Name: ${dockerImageTag}"
		  
		  sh "docker stop pracainzynierka"
		  
		  sh "docker rm pracainzynierka"
		  
		  sh "docker run pracainzynierka:${env.BUILD_NUMBER} -p 2222:2222 "
		  
		  // docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
	      //    dockerImage.push("${env.BUILD_NUMBER}")
	      //      dockerImage.push("latest")
	      //  }
	      
	    }
}