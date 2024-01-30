"""A Python Pulumi program"""

import pulumi
import pulumi_kubernetes as k8s

# Define a transformation function
def ignore_all(obj):
    obj.opts.ignore_changes=['*']

# Instantiate a Helm Release for NGINX, applying the transformation
nginx_release = k8s.helm.v3.Release(
    'nginx-ingress',
    chart="nginx-ingress",
    version="1.24.4",
    namespace="test-namespace",
    repository_opts=k8s.helm.v3.RepositoryOptsArgs(
        repo="https://charts.helm.sh/stable",
    ),
    opts=pulumi.ResourceOptions(
        transformations=[ignore_all]
    )
)

# Export the release name
pulumi.export('release_name', nginx_release.name)
