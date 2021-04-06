This repo shows how a docker app can be converted to a Kubernetes (K8) app. 
--------
# Docker Test
In the main branch:
1. Download Docker
2. Run `docker-compose build` in the top-level directory
3. Run `docker-compose up` in the same directory
4. Open the server on `localhost:5000`
5. Open the microservice/client on `localhost:5001`

This small docker app sends content from the server to the client via HTTP request initiated by the client.


# Kubernetes Test
For the conversion to kubernetes, see the branch `k8_conversion`, and the open pull request to see a side-by-side comaprison. 
