# Create a deployment

```
kubectl apply -f deployment.yml

```

# Check the deployment

```
kubectl get deployment
```

# Check the replicaset

```
kubectl get replicaset
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



# push my local image to docker hub 

## tag my image 

```
docker tag ajith:latest bharathikalai/ajith:latest
```

## Push the image to my docker hub

```
docker push bharathikalai/ajith:latest

```