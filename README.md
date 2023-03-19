# The diabetes ml model API  


## Overview
Development considerations:  

1. Unit and Integration tested api  
2. Pathing and environment management via tox and poetry  
3. CI coordinated via Circleci yaml config - runs the app, performs formatting checks and linting, runs tests with semantic versioning, and pushes the new container to ECR and updates the contatiner in ECS   



## Maintainability  
### tox  
 venv management and test command line tool  
 Using Tox we can (on multiple operating systems):  
 - Eliminate PYTHONPATH challenges when running scripts/tests  
 - Streamline model training, model publishing  

on the CLI:  

tox run -e test_app  
tox run -e run  
tox run -e checks  

these are easiy integrated into the CI pipeline  

### Security and privacy
External package index (GemFury is used for convenience, S3 can be used but requires additional set up i.e. SSL certificate)  

CircleCI is used for CI/CD pipeline construction and monitoring, a service that integrates will with common version control repositories, secrets are managed by this service  

AWS - users user groups and roles are configured via AWS IAM  

## Infrastructure - API
**ECR**: A private container repository hosted on AWS, options to manage lifecycles, and access configuration via KMS and IAM.
**ECS**: Fargate - a managed serverless and elastically scaling compute service that runs containers in the ECR 

## TODO
Infrastructure as code templating with terraform  
Static IP with a network load balancer
