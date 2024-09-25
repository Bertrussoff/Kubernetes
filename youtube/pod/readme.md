# Everything about  PODs

- You are learning or testing Kubernetes.
- You need a temporary Pod for debugging or small tasks.
- You don't need automatic restarts or scaling.


# Simple pod example

```
apiVersion: v1                   # Specifies the API version of the Kubernetes object.
kind: Pod                        # Defines the kind of Kubernetes object; in this case, it is a Pod.
metadata:                        # Metadata about the Pod.
  name: simple-pod              # The name of the Pod, which must be unique within the namespace.
spec:                            # The specification of the Pod.
  containers:                   # Defines the list of containers that will run in the Pod.
  - name: nginx                 # The name of the container; can be any name you choose.
    image: nginx                # The container image to use; in this case, it uses the official NGINX image.
    ports:                      # Defines the ports that the container exposes.
    - containerPort: 80        # Specifies that the container listens on port 80.
```


## Commands:

```
kubectl apply -f pod.yml
```

```
kubectl get pods
```


```
kubectl port-forward pod/simple-pod 8080:80
```

```
kubectl logs pod_name -f

```

```
kubectl describe pod pod_name

```