# Commands for config map

```
kubectl apply -f configmap.yml
```

```
kubectl get cm

```

```
kubectl exec -it <pod-name> -- /bin/sh
echo $WELCOME_MESSAGE

```


# Secrets

```
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret          # Name of the Secret
              key: db_password   

```

# base64

```
echo -n "secretPassword" | base64
```

# External encrypted

## External Key Management Systems (KMS)
### Kubernetes can be configured to use an external KMS (Key Management System) for encrypting Secrets.
#### Common KMS providers include:
1. AWS KMS: For managing keys in AWS.
2. Google Cloud KMS: For managing encryption keys in GCP.
3. Azure Key Vault: For managing keys in Azure.

