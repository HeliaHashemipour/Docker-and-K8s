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
