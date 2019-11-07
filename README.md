# kubernetes-ingress

With minikube running locally, spin up the deployments first, then the services, then the ingress controller.
Navigate to {minikube ip}/meow to see the first hello-world, then {minikube ip}/meow2 for the second.

[To install minikube locally.](https://kubernetes.io/docs/tasks/tools/install-minikube/).

[to install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

Spinning up a resource:

`$ kubectl apply -f hello_world_deployment.yaml`
