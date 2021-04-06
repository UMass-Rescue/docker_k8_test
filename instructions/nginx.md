# NGINX

I didn't get very far with adding NGINX to the current k8 setup. Here are some resources:

* [Kubernetes documentation](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
* [Helpful Medium article](https://awkwardferny.medium.com/getting-started-with-kubernetes-ingress-nginx-on-minikube-d75e58f52b6c)

## Steps so far
1. In minikube, start nginx with `minikube addons enable ingress`
2. Create an `ingress` object. The `ingress.yaml` file provides an initial template.
