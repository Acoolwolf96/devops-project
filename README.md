# DevOps Project Pipeline

## Overview
This is a simple Python Flask web application packaged as a Docker container and deployed to Kubernetes with a Helm chart. The repository also includes Argo CD application configuration for GitOps-style deployment and Terraform configuration to provision a local Minikube cluster.

The app serves a simple webpage at the root route (`/`). It is designed as a lightweight demo for containerization, Helm-based Kubernetes deployment, and GitOps deployment with Argo CD.

## Repository Structure

- `app.py` - Flask application source code.
- `Dockerfile` - Builds a container image for the Flask app.
- `argocd-app.yaml` - Argo CD `Application` manifest that syncs the Helm chart from this repository.
- `devops-project-app/` - Helm chart for deploying the application into Kubernetes.
  - `Chart.yaml` - Helm chart metadata.
  - `values.yaml` - Default chart values.
  - `templates/` - Kubernetes manifest templates for Deployment, Service, Ingress, ServiceAccount, HPA, and notes.
- `terraform-configs/` - Terraform configuration for provisioning a local Minikube cluster.
  - `main.tf` - Defines the Minikube provider and a local Minikube cluster resource.
  - `provider.tf` - Terraform provider configuration.
  - `backend.tf` - Terraform backend config.
  - `variables.tf` - Terraform variables.
  - `argocd.tf` - Argo CD-related or supporting infrastructure config.


## Docker Image

The `Dockerfile` builds the app using `python:3.12-slim`, installs `flask`, and launches the app on port `5000`.

Build and run locally:

```bash
docker build -t devops-project:latest .
docker run -p 5000:5000 devops-project:latest
```

## Helm Chart

The Helm chart in `devops-project-app/` deploys the Flask app to Kubernetes.


### Templates

- `templates/deployment.yaml` - Creates a Deployment with configurable replicas, image, port, probes, resources, and pod settings.
- `templates/service.yaml` - Exposes the app as a Kubernetes `Service`.

## GitOps with Argo CD

`argocd-app.yaml` defines an Argo CD `Application` that tracks this repository and deploys the Helm chart from `devops-project-app`.

This enables Argo CD to automatically reconcile the deployed application with the Git repository state.

## Terraform Infrastructure

The `terraform-configs/` directory contains Terraform definitions for a local Minikube cluster.

### `main.tf`

- Uses the `scott-the-programmer/minikube` Terraform provider.
- Creates a Minikube cluster named `devops-project` using the Docker driver.
- Enables addons: `default-storageclass` and `storage-provisioner`.

This setup is useful for local Kubernetes development and testing.


### Prerequisites

- Docker
- Kubernetes cluster or Minikube
- Helm
- Terraform
- Argo CD


### Deploy to Kubernetes with Helm

From the repository root:

```bash
helm install devops-project ./devops-project-app
```

If the chart was already installed:

```bash
helm upgrade devops-project ./devops-project-app
```

### Use Terraform to provision Minikube

From `terraform-configs/`:

```bash
cd terraform-configs
terraform init
terraform apply
```

### Deploy with Argo CD

Apply the Argo CD application manifest:

```bash
kubectl apply -f argocd-app.yaml
```

Then sync or monitor the application in the Argo CD UI.

## Notes

- The chart uses a default `ClusterIP` service and does not enable ingress by default.
- The application is intentionally minimal and suited for learning containerization, Helm deployment, and GitOps workflows.
- The Argo CD manifest is configured for automated sync with pruning and self-healing.

