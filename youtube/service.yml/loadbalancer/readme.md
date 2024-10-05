## Command 


## Creat the eks cluser in aws

```
eksctl create cluster --name demo-cluster-1 --region ap-south-1 --fargate
```


## UPdate kubeconfig in your local

```
aws eks update-kubeconfig --name demo-cluster-1 --region ap-south-1
```

## Crete the fargate

```
 eksctl create fargateprofile \
    --cluster demo-cluster-1 \
    --region ap-south-1 \
    --name service-sample-app \
    --namespace service-name-space

```







