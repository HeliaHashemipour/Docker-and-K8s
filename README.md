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
To get the temperature info, it sends an HTTP GET to a server that its URL is set on `weather_url` environment variables. 
Additionally, `server_port` env variable is also set so that the server port is configurable.

A `Dockerfile` is also included on `2. WeatherServer` directory. In this step, we create an image and push to the Docker Hub using the commands mentioned in the previous section.

Last but not least, we can test the created image locally using the following command:
```text
docker run --rm --env weather_url="http://api.weatherstack.com/current?access_key=<ACCESS_KEY>&query=Tehran" -p 80:8080 <docker-id>/<image-name>:<tag>
```
In the preceding command:
- **--rm**: removes the container after the execution.
- **--env**: Sets the required environment variables which are `weather_url` and `server_port`. Since `server_port` is not set, the python code sets to the default value which is 8080.
- **-p**: Maps port with the structure `<HOST-PORT>:<CONTAINER-PORT>`. Therefore, it maps the port 8080 of the container to the 80 of the host.

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
In the preceding command, ``--dry-run=client`` flag means that we want to get a preview of the object instead of creating
it in our cluster. Additionally, `-o yaml` means that our output format is `yaml` and we store the content on the
`server-deployment.yaml` file.

There are two modifications that are made:
- **replicas: 2**: this means to create 2 pods.
Next, we apply the created deployment:
```text
kubectl apply -f server-deployment.yaml
```
We can get the status of our pods on our deployment using the following command:
```text
kubectl get deployments
```

One of the drawbacks of using pods directly is that their IP Address might change after each restart. Hence, we create a
server to automatically manages these two pods and distribute the incoming traffic over them.

To create the service, first we create the following content on `server-service.yaml`.

After the creation of the service, we apply it using the following command:
```text
kubectl apply -f server-service.yaml
```

## Section 4: Testing the system
