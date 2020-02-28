Digitalocean cluster

Install kubectl binary with curl on macOS
https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-macos

curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"

Install Homebrew

https://brew.sh/


Install Docker
https://hub.docker.com/editions/community/docker-ce-desktop-windows





Digitalocean API CLI tool
doctl 

cd D:\code\walthertimmer.nl\digitalocean


gebruik docker image gemaakt door anderen

alleen kubectl belangrijk


kubectl run ghost --image=ghost --port=2368 

#status
kubectl get pods

kubectl expose deployment ghost --type="NodePort"
#service "ghost" exposed



service = loadbalancer
deployment = ghost image
volume = vaste storage 