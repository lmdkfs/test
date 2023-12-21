<<<<<<< HEAD
# Add Test from master
=======
<<<<<<< HEAD
>>>>>>> cd35baa (modify README from master)
# modify from branch-a

=======
# Add Test from master
<<<<<<< HEAD
>>>>>>> b7cd35a (modify README from master)
=======
# modify from branch-a

>>>>>>> 42a762e (modify readme from branch-a)
   ```python
   
   {
  "apiVersion": "apps/v1",
  "kind": "Deployment",
  "metadata": {
    "name": "richie-nginx-demo",
    "namespace": "o4eaahu3mqmfcqh82zdc",
    "labels": {
      "app": "nginx"
    }
  },
  "spec": {
    "replicas": 3,
    "selector": {
      "matchLabels": {
        "app": "nginx"
      }
    },
    "template": {
      "metadata": {
        "labels": {
          "app": "nginx"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:1.15.4",
            "ports": [
              {
                "containerPort": 80
              }
            ]
          }
        ]
      }
    }
  }
}
```
