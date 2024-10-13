# Prometheus architecture


![alt text](image.png)


# Commands

## install heml chart

```
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

```

## add prometheus to the helm chart repo 

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

## install prometheus

```
helm install prometheus prometheus-community/prometheus
```

## check the promotheus pod

```
helm install prometheus prometheus-community/prometheus

```

## check the prometheus pod and service

```
kubectl get svc
kubectl get pods
```

## add node port ip to the prometheus pod 
```
kubectl patch svc prometheus-server -p '{"spec": {"type": "NodePort", "ports": [{"port": 80, "nodePort": 30080}]}}'
```


## promql

```
count(kube_pod_status_phase{phase="Running"})
```