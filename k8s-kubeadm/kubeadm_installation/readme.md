# Verify this doc  for kubeadm installation

```
https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/


```

# install docker 

```
sudo apt install docker.io

# init the kubeadm
```
kubeadm init
```


```

# give the permission

```
sudo chmod 644 /etc/kubernetes/admin.conf
```


# Installing Calico CNI Plugin
```
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

# get the node

```
kubectl get node
```


# Pod schedule on control plane

```
kubectl taint nodes --all node-role.kubernetes.io/control-plane:NoSchedule-

```