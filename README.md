# Docker-and-K8s

This repository is about the first assignment of the cloud computing course.

> Instructor: [Dr. S. A. Javadi](https://scholar.google.com/citations?user=Va7RTUsAAAAJ&hl=en)

> Semester: Fall 2022
## Section 1: Docker Hub

This section creates a Dockerfile that has an alpine linux distribution with curl installed.

To make an image from this Dockerfile, using the
following command:

```text
docker build -t <image-name>:<tag> .   =>   docker build -t new-alpine:1.0 .
```

Next, before pushing to the DockerHub, we change the tag with the following command:

```text
docker tag <image-name>:<tag> <docker-id>/<image-name>:<tag>   =>   docker tag new-alpine:1.0 heliahashemipour/new-alpine:1.0
```

`<docker-id>` is the docker ID of the DockerHub account. 

for pushing into Docker Hub, we can enter the following command:  
```text
docker image push <docker-id>/<image-name>:<tag>   =>   docker image push heliahashemipour/new-alpine:1.0 
```
To test the created image, download your image from Dockerhub‫.‬

```text
docker image pull <docker-id>/<image-name>:<tag>   =>   ddocker image pull heliahashemipour/new-alpine:1.0
```
Bring up a container from it. Then send a curl request to google.com.
```text
docker run -it --rm <docker-id>/<image-name>:<tag>   =>   docker run -it --rm heliahashemipour/new-alpine:1.0
```
## Section 2: Coin Server

In this section, a simple HTTP REST server is implemented with flask. 
```json
{
  "name": "<COIN NAME>",
  "price": "<COIN PRICE>",
}
```


Last but not least, we can test the created image locally using the following command:
```text
docker run --rm --network flask -v :/data --name redis redis redis-server 
```
```text
docker run --it -e SERVER_PORT="80" -e COIN_NAME="bitcoin" -e CACHE_EXPIRE_TIME="300" -p 80:80 --network flask --name coin-price coin-server:1.0 
```

## Section 3: Kubernetes
First, we create a ConfigMap called `server-config.yaml` 
To apply the config on our cluster ConfigMaps, we enter the following command:
```text
kubectl apply -f server-config.yaml
```
We can get the list of config maps using the following command:
```text
kubectl get configmaps
```

Following the creation of the config map, we need to create a deployment to run our pods. So we create it using the following command:
```text
kubectl create deployment <deployment-name> --image=<image-name> --dry-run=client -o yaml > server-deployment.yaml
```

Next, we apply the created deployment:
```text
kubectl apply -f server-deployment.yaml
```
We can get the status of our pods on our deployment using the following command:
```text
kubectl get deployments
```
To create the service, first we create the following content on `server-service.yaml`.

After the creation of the service, we apply it using the following command:
```text
kubectl apply -f server-service.yaml
```
we create this files for redis server,as well.

## Section 4: Testing the system
this part is for testing. what we have done in previous sections.
