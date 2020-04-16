from kubernetes import client
from kubernetes.client.rest import ApiException

import json

class K8sAPI(object):

    def __init__(self, kubeconfig_token: str, k8s_host: str):

        configuration = client.Configuration()
        token=kubeconfig_token
        configuration.host = k8s_host
        configuration.api_key = {
            "authorization": "Bearer " + token
        }
        # api_client = client.BatchV1Api(client.ApiClient(configuration))
        configuration.verify_ssl = False
        self.apiClient = client.ApiClient(configuration)


    def create_deployment_object(self, deployment_name: str, **kwargs: dict):
        """
        Configureate Deployment template container
        :return:
        """

        # Configureate Pod template container
        container = client.V1Container(
            name=kwargs['spec']['template']['spec']['containers'][0]['name'],
            image=kwargs['spec']['template']['spec']['containers'][0]['image'],
            ports=[client.V1ContainerPort(container_port=80)])

        # Create and configureate a spec section
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels=kwargs['spec']['template']['metadata']['labels']),
            spec=client.V1PodSpec(containers=[container])
        )
        print()
        # Create the specification of deployment
        spec = client.V1DeploymentSpec(
            replicas=kwargs['spec']['replicas'],
            template=template,
            selector=kwargs['spec']['selector']
        )

        # Instantiate the deployment object
        deployment = client.V1Deployment(
            api_version='apps/v1',
            kind='Deployment',
            metadata=client.V1ObjectMeta(name=deployment_name),
            spec=spec
        )
        return deployment

    def create_deployment(self, namespace, deployment):
        # Create deployment
        api_client = client.AppsV1Api(self.apiClient)
        try:
            api_response = api_client.create_namespaced_deployment(
                namespace='o4eaahu3mqmfcqh82zdc',
                body=deployment,

            )

            print("Deployment created. status=%s" % str(api_response.status))
        except ApiException as e:
            print("Excetion when calling Apps V1Api -> create_namespaced_deployment:%s \n" % e.body)
            error_body = json.loads(e.body)
            print(error_body.get("message"))

    def create_ingress(self, namespace, name):
        api_client = client.NetworkingV1beta1Api()
        # api_client.create_namespaced_ing  ress()
    #
    # def create_namespace(self, namespace: str):
    #     api_client = client.
    #     api_client
