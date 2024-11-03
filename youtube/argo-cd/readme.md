# ArgoCD Installation Part 2 - Quick Start
Argo CD is a declarative continuous delivery tool for Kubernetes applications. It uses the GitOps style to create and manage Kubernetes clusters. When any changes are made to the application configuration in Git, Argo CD will compare it with the configurations of the running application and notify users to bring the desired and live state into sync.

Argo CD has been developed under the Cloud Native Computing Foundation’s (CNCF) Argo Project- a project, especially for Kubernetes application lifecycle management. The project also includes Argo Workflow, Argo Rollouts, and Argo Events.. Each solves a particular set of problems in the agile development process and make the Kubernetes application delivery scalable and secure.
### Upgrade Packages & Install Prerequisites

### Install ArgoCD
```sh
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
### Change Service to NodePort
Edit the service can change the service type from `ClusterIP` to `NodePort`
```sh
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}' 
```
### Fetch Password
```sh
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
# Deploy Demo Application
You can use the below repository to deploy a demo nginx application
```sh
https://github.com/dmancloud/argocd-tutorial
```
### Scale Replicaset 
```sh
kubectl scale --replicas=3 deployment nginx -n default
```
### Clean Up
```sh
kubectl delete -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl delete namespace argocd
```


#Cli install

```
VERSION=$(curl -s https://api.github.com/repos/argoproj/argo-cd/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') && \
curl -sSL https://github.com/argoproj/argo-cd/releases/download/${VERSION}/argocd-linux-amd64 -o argocd
```
```
chmod +x argocd
```

```
sudo mv argocd /usr/local/bin/
```

```
argocd version
```

# argocd login command

```
argocd login 192.168.49.2:32571 --username admin --password 86Gvvd28wqlxvgXw --insecure

```

# argo cd app command 

```
argocd app list

syncInterval: 10s


```


```
https://youtu.be/q4g7KJdFSn0?si=6dZ3J1vy9d1ZDaJh
```
