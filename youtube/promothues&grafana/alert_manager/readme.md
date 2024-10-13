```
kubectl create configmap prometheus-alert-rules --from-file=alert-rules.yml -n default
```

```
kubectl edit deployment <prometheus-deployment-name> -n <namespace>

```

# volume session

```
volumes:
- name: alert-rules
  configMap:
    name: prometheus-alert-rules
```

# container session 

```
volumeMounts:
- name: alert-rules
  mountPath: /etc/prometheus/rules
  subPath: alert-rules.yml
```

# update  prometheus.yml file 

```
rule_files:
  - "/etc/prometheus/rules/alert-rules.yml"
```

# recreate the pod

```
kubectl delete pod <prometheus-server-pod-name> -n <namespace>

```