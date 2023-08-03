Blue-Green Deployment: Python App
blue/green deployment is a deployment strategy in which you create two separate, but identical environments. One environment (blue) is running the current application version and one environment (green) is running the new application version. Using a blue/green deployment strategy increases application availability and reduces deployment risk by simplifying the rollback process if a deployment fails. Once testing has been completed on the green environment, live application traffic is directed to the green environment and the blue environment is deprecated.

Workflow of the project:

checkout code from github

build a docker image

login to dockerhub

docker tag and push the created image to dockerhub

logout from dockerhub

Deployment to Kubernetes
Installation: Manual
Install docker in your system. Refer the official documentation for installing docker here: https://docs.docker.com/engine/install/ubuntu/
Install minikube in your system. Refer the official documentation for installing minikube here: https://minikube.sigs.k8s.io/docs/start/
Build the docker image for blue: Initial version of the project
docker build -t ebinvarghese/jokeapp-blue:latest .
Build the docker image for green: New version of the project
docker build -t ebinvarghese/jokeapp-green:latest .
Push the docker image to dockerhub: 
docker push ebinvarghese/jokeapp-blue:latest 
docker push ebinvarghese/jokeapp-green:latest
Deploy the blue app: 
kubectl apply -f jokeapp-blue/deployment.yaml 
kubectl apply -f jokeapp-blue/service.yaml
Deploy the green app: 
kubectl apply -f jokeapp-green/deployment.yaml 
kubectl apply -f jokeapp-green/service.yaml
Check the service list to see the link to the deployed apps: minikube service list
Now to redirect the traffic from blue to green, edit the service file and update the selector to jokeapp-green: 
selector: 
    app: jokeapp-green
Refresh the blue page to see the update
Installation: By using Jenkins and Argo (Automation)
Install argo. You can refer the official documentation here: https://argo-cd.readthedocs.io/en/stable/getting_started/
configure the pipeline for the live site with Jenkinsfile-live
configure the pipeline for the test site with Jenkinsfile-test
build the project and the following will be happen: 
image for jokeapp-blue and jokeapp-green will be created 
The image will be pushed to the dockerhub 
The application will be deployed to k8s cluster by Argo
Now to redirect the traffic from blue to green, update the service file with jokeapp-green selector: selector: 
    app: jokeapp-green
Refresh the live site's page and see the update
Notes:
I have used the environment variable for the TAG as Date+Buildnumber. You can create as per your requirements.
Dockerhub login credentials needs to be configured in Jenkins.
Needs to authenticate the jenkins user to use minikube.
If any doubts, ping me in whatsapp: +91 9495885325