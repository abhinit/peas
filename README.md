# Peas
## Setup
We are using an Ubuntu 14.04 machine with 3.19.0-47-generic kernel on an HP Z820 workstation
### Requirements
- Docker
- Minikube

### Installation
#### Installing Docker
```Shell
$ sudo apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```
```Shell
$ curl -fsSL https://apt.dockerproject.org/gpg | sudo apt-key add -
```
```Shell
$ sudo add-apt-repository \
       "deb https://apt.dockerproject.org/repo/ \
       ubuntu-$(lsb_release -cs) \
       main"
```
```Shell
$ sudo apt-get update
```
```Shell
$ sudo apt-get -y install docker-engine
```

#### Installing Minikube
Minikube installation requires VirtualBox which can be downloaded and installed from http://download.virtualbox.org/virtualbox/5.1.14/virtualbox-5.1_5.1.14-112924~Ubuntu~trusty_amd64.deb

Next, we can go ahead and install Minikube

```Shell
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.16.0/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

To make it available directly from your shell

```Shell
sudo mv minikube /usr/local/bin
```

#### Starting docker and minikube

Starting the docker service
```Shell
sudo service docker start
```
Starting Minikube
```Shell
minikube start
```
Associating docker with minikube
```Shell
eval $(minikube docker-env --shell=sh)
```
To test minikube you can try:
```Shell
kubectl get pods
```
You show see an empty response

## Pea deployment

### File structure
- **dockerfile**: The dockerfile specifies the container definition for the pea.
```
NOTE: Don't forget to expose the server port in the dockerfile, else minikube won't be able to identify the port to watch.
```
- **deployment.yaml**: The deployment file contains the kubernetes deployment definition. Here you can specify the docker image to use (created using the aforementioned dockerfile) for the kubernetes pods, the replica set properties and other tags describing the deployment

- **action.py**: The action file contains the Mistral action definition file, in order to deploy the pea service as a Mistral action to be used in Mistral workflows (Peapods)

- **/app**: This is the container app folder which contains the server logic for the pea

### Deployment of pea

The pea deployment stage has 2 steps: *Creating a deployment* and *Exposing the deployment as a service*, they are done as follows:

```Shell
kubectl create -f deployment.yaml
```

```Shell
kubectl expose deployment pea-deployment --type=NodePort
```
The type NodePort makes the service available locally within the cluster and doesn't expose it to a public IP, for that, use the type LoadBalancer

### Testing the pea

You can test the normalization pea using the following command:

```Shell
 curl -H "Content-Type: application/json" -X POST -d "{\"array\":[1,2,5]}" <PEA ADDRESS>
```

The response should look like:

```Shell
{
  "result": [
    0.0, 
    0.25, 
    1.0
  ], 
  "status": "ok"
}

```
You can obtain the PEA ADDRESS as follows:

```Shell
minikube service pea-deployment --url
```
