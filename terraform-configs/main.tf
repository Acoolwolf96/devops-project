terraform {
  required_providers {
    minikube = {
        source = "scott-the-programmer/minikube"
        version = "0.6.0"
    }
  }
}


provider "minikube" {}

resource "minikube_cluster" "minikube_docker" {
    driver = "docker"
    cluster_name = "devops-project"
    addons = [
        "default-storageclass",
        "storage-provisioner",
    ]
  
}