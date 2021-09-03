# Docker 

## 1. gRPC server image
Clone this [repo](https://github.com/ipa-rar/gRPC-servers/tree/main/demo_simple_communication) and then use these commands.

Build docker image
```
docker build -t simple_server_app -f docker/Dockerfile .
```
Run the docker image
```
docker run simple_server_app
```

## 2. gRPC-ROS client image
Build docker image
```
docker build -t grpc_client_app -f docker/Dockerfile-client .
```

Run the docker image
```
docker run grpc_client_app
```

## Full system launch

```
docker-compose up
```