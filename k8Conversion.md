This repo shows how a docker app can be converted to a Kubernetes (k8) app. The Docker version is in the main branch. The k8 version is in the k8_conversion branch. See this pull request for a side-by-side comparison.

--------
# Kubernetes Conversion
To convert from Docker in the `main` branch to k8 in the `k8_conversion` branch, I did the following:

## Generating k8 yaml files
1. [Download `kompose`](https://kompose.io/installation/)
2. [Download `kubectl`](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-kubectl/)(this is the command line tool for k8)
3. [Download `minikube`](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/) (this is for local development and testing)
4. Remove references to `volumes` in the `docker-compose.yml` file.
5. Run  `kompose convert` in the top level directory. 

K8 files should be generated.
For each docker `Service`, kompose generates:
* A `deployment` object, which manages a stateless pod.
* A `service` object, which directs traffic to the associated pod.

## Adding Persistent Volume Claims (PVC) to the app
1. Create a `.yml` file of type `PersistentVolumeClaim`. In this app, it is named `pvc.yml`. This file creates a volume *claim*. When accessed by a pod, a volume is dynamically created.
2. In the `deployment` file of the pod you want to connect to the volume claim, add the volume under:
    * the `spec` section
    * the `spec/containers/VolumeMounts` section. 
    See `server-deployment.yaml` for how this is done. 
    
    Now you have configured the k8 PVC. For more information on a Persistent Volume vs a Persistent Volume Claim, see https://docs.openshift.com/enterprise/3.1/dev_guide/persistent_volumes.html. 

## Pointing minikube to the local Docker Directory
For local development, you will have local docker images, that are not in DockerHub. By default, minikube tries to access images from DockerHub. To change this do the following:
1. Run `eval $(minikube -p minikube docker-env)`
2. Re-build docker images in the directory of the `Dockerfile` with `docker build . -t my-image` e.g. for this app, in the `server` folder, I ran `docker build . -t server`.
3. The final build name is returned to you in the command line. Add this in the `deployment` file, under `spec/containers/image`. e.g. in the `server-deployment.yaml` this is `server:latest`, which is the local docker build.

Now minikube points to the local docker directory.

**Run the app as specified in the `README.md` in the `k8_conversion` branch.** 
