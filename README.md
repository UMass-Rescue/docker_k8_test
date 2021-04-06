This repo shows how a docker app can be converted to a Kubernetes (k8) app. The Docker version is in the main branch. The k8 version is in the k8_conversion branch. See [this pull request](https://github.com/UMass-Rescue/docker_k8_test/pull/1/files) for a side-by-side comparison.

--------
# Kubernetes Test
To run this app:
1. Make sure you are on the `k8_conversion` branch
2. [Download `kubectl`](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-kubectl/)(this is the command line tool for k8)
3. [Download `minikube`](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/) (this is for local development and testing)
4. Run `minikube start` 
5. Run  `sh start_k8.sh`
6. Run `minikube service server` to open the server
7. Run `minikube service client` to open the microservice/client

This small k8 app also sends content from the server to the client via HTTP request initiated by the client. Try it out by typing something in the server window, and refreshing the client window! 

To stop this app:
1. Run `sh stop_k8.sh`
2. Run `minkube stop`

**See `instructions/k8Conversion.md` for instructions on conversion and `instructions/nginx.md` for what I have learned about NGINX** 
