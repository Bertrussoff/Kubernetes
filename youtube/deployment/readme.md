# Create a deployment

```
kubectl apply -f deployment.yml

```

# Check the pod status
```
kubectl get pod -o wide
```

# login in minikube container

```
minikube ssh
```

# Curl command for application is running or not 
```
curl pod_private_ip:5000
```