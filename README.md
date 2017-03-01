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
