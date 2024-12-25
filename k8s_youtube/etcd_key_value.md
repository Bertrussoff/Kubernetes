# Cert path

```

cd /var/lib/minikube/certs/etcd

```


CA cert
Server cert
Server key


# Install etcd client


```
sudo apt-get update -y
sudo apt-get install -y etcd-client
```


# View the key of my whole registory
```
ETCDCTL_API=3 etcdctl --cacert ca.crt --cert server.crt --key server.key --endpoints https://127.0.0.1:2379 get /registry/ --prefix --keys-only
```

# View the specfic pod key and value

```
ETCDCTL_API=3 etcdctl --cacert ca.crt --cert server.crt --key server.key --endpoints https://127.0.0.1:2379 get /registry/pods/kube-system/kube-proxy-dmcxp
```