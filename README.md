This repo shows how a docker app can be converted to a Kubernetes (K8) app. 
The Docker version is in the `main` branch.
The K8 version is in the `k8_conversion` branch. 
See [this pull request](https://github.com/UMass-Rescue/docker_k8_test/pull/1/files) for a side-by-side comparison.

--------
# Docker Test
To run this app, 
1. Make sure you are on the `main` branch
2. [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
3. Run `docker-compose build`
4. Run `docker-compose up`
5. Open the server on `localhost:5000`
6. Open the microservice/client on `localhost:5001`

This small docker app sends content from the server to the client via HTTP request initiated by the client. Try it out by typing something in the server window, and refreshing the client window!  

To stop this app, type `Ctrl + C` in the command line.
