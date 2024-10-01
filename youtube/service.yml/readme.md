# Command

## Create the deployment.yml

```
kubectl apply -f deployment.yml
```

## Create the service.yml

```
kubectl apply -f service.yml
```

## list the service

```
kubectl get service -o wide

```
## list the pod

```

kubectl get pod -o wide
```

## pod log view

```
kubectl logs <pod name> -f

```
