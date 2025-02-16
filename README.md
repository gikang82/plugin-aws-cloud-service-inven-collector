# plugin-aws-cloud-service-inven-collector

![AWS Cloud Services](https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-cloudservice.svg)
**Plugin to collect AWS Cloud Services**

> SpaceONE's [plugin-aws-cloud-service-inven-collector](https://github.com/spaceone-dev/plugin-aws-cloud-services) is a convenient tool to get cloud service data from AWS.


Find us also at [Dockerhub](https://hub.docker.com/repository/docker/spaceone/plugin-aws-cloud-service-inven-collector)
> Latest stable version : 1.13.5

Please contact us if you need any further information. (<support@spaceone.dev>)

---

## Collecting Contents

* Table of Contents
    * [API Gateway](/src/spaceone/inventory/connector/aws_api_gateway_connector/README.md)
        * API (REST API / Websocket)
    * [Auto Scaling Group](/src/spaceone/inventory/connector/aws_auto_scaling_connector/README.md)
        * Auto Scaling Group
        * Launch Configuration
        * Launch Template
    * [Cloud Front](/src/spaceone/inventory/connector/aws_cloud_front_connector/README.md)
        * Distribution
    * [Cloud Trail](/src/spaceone/inventory/connector/aws_cloud_trail_connector/README.md)
        * Trail
    * [Direct Connect](/src/spaceone/inventory/connector/aws_direct_connect_connector/README.md)
        * Connection
        * Direct Connect Gateway
        * Virtual Private Gateway
        * LAG
    * [DocumentDB](/src/spaceone/inventory/connector/aws_documentdb_connector/README.md)
        * Cluster
        * Subnet Group
        * Parameter Group
    * [DynamoDB](/src/spaceone/inventory/connector/aws_dynamodb_connector/README.md)
        * Table
    * [EBS](/src/spaceone/inventory/connector/aws_ebs_connector/README.md)
        * Volume
        * Snapshot
    * [EC2](/src/spaceone/inventory/connector/aws_ec2_connector/README.md)
        * Security Group
        * AMI
    * [ECR](/src/spaceone/inventory/connector/aws_ecr_connector/README.md)
        * Repository
    * [ECS](/src/spaceone/inventory/connector/aws_ecs_connector/README.md)
        * Cluster
    * [EFS](/src/spaceone/inventory/connector/aws_efs_connector/README.md)
        * Filesystem
    * [EIP](/src/spaceone/inventory/connector/aws_eip_connector/README.md)
        * EIP
    * [EKS](/src/spaceone/inventory/connector/aws_eks_connector/README.md)
        * Cluster
        * Node Group
    * [ElastiCache](/src/spaceone/inventory/connector/aws_elasticache_connector/README.md)
        * Memcached
        * Redis
    * [ELB](/src/spaceone/inventory/connector/aws_elb_connector/README.md)
        * Load Balancer
        * Target Group
    * [IAM](/src/spaceone/inventory/connector/aws_iam_connector/README.md)
        * Group
        * User
        * Role
        * Policy
        * Identity Provider
    * [Kinesis Datastream](/src/spaceone/inventory/connector/aws_iam_connector/README.md)
        * Data stream
    * [Kinesis Firehose](/src/spaceone/inventory/connector/aws_iam_connector/README.md)
        * Delivery stream
    * [KMS](/src/spaceone/inventory/connector/aws_kms_connector/README.md)
        * Key
    * [Lambda](/src/spaceone/inventory/connector/aws_lambda_connector/README.md)
        * Function
        * Layer
    * [MSK](/src/spaceone/inventory/connector/aws_msk_connector/README.md)
        * Cluster
        * Cluster Configuration
    * [RDS](/src/spaceone/inventory/connector/aws_rds_connector/README.md)
        * Database
        * Instance
        * Snapshot
        * Subnet Group
        * Option Group
    * [Redshift](/src/spaceone/inventory/connector/aws_redshift_connector/README.md)
        * Cluster
    * [Route53](/src/spaceone/inventory/connector/aws_route53_connector/README.md)
        * Hosted Zone
    * [S3](/src/spaceone/inventory/connector/aws_s3_connector/README.md)
        * Bucket
    * [Secrets Manager](/src/spaceone/inventory/connector/aws_secrets_manager_connector/README.md)
        * Secret
    * [SNS](/src/spaceone/inventory/connector/aws_sns_connector/README.md)
        * Topic
    * [SQS](/src/spaceone/inventory/connector/aws_sqs_connector/README.md)
        * Queue
    * [VPC](/src/spaceone/inventory/connector/aws_vpc_connector/README.md)
        * VPC
        * Subnet
        * Route Table
        * Internet Gateway
        * Egress only internet Gateway
        * NAT Gateway
        * Peer Connection
        * Network ACL
        * Endpoint
        * Transit Gateway
        * Customer Gateway
        * VPN Connection
        * VPN Gateway

---

## AWS Service Endpoint (in use)

 There is an endpoints used to collect AWS resources information.
AWS endpoint is a URL consisting of a region and a service code. 
<pre>
https://[service-code].[region-code].amazonaws.com
</pre>

We use hundreds of endpoints because we collect information from a lots of regions and services.  

### Region list

Below is the AWS region information.
The regions we collect are not all regions supported by AWS. Exactly, we target the regions results returned by [describe_regions()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_regions) of AWS ec2 client.

|No.|Region name|Region Code|
|---|------|---|
|1|US East (Ohio)|us-east-2|
|2|US East (N. Virginia)|us-east-1|
|3|US West (N. California)|us-west-1|
|4|US West (Oregon)|us-west-2|
|5|Asia Pacific (Mumbai)|ap-south-1|
|6|Asia Pacific (Osaka)|ap-northeast-3|
|7|Asia Pacific (Seoul)|ap-northeast-2|
|8|Asia Pacific (Singapore)|ap-southeast-1|
|9|Asia Pacific (Sydney)|ap-southeast-2|
|10|Asia Pacific (Tokyo)|ap-northeast-1|
|11|Canada (Central)|ca-central-1|
|12|Europe (Frankfurt)|eu-central-1|
|13|Europe (Ireland)|eu-west-1|
|14|Europe (London)|eu-west-2|
|15|Europe (Paris)|eu-west-3|
|16|Europe (Stockholm)|eu-north-1|
|17|South America (São Paulo)|sa-east-1|



### Service list

The following is a list of services being collected and service code information.

|No.|Service name|Service Code|
|---|------|---|
|1|AWS Certifcate Manager|acm|
|2|API Gateway (REST API)|apigateway|
|3|API Gateway V2 (Websocket)|apigatewayv2|
|4|Auto Scaling Group|autoscaling|
|5|CloudFront|cloudfront|
|6|CloudTrail|cloudtrail|
|7|Direct Connect|directconnect|
|8|DocumentDB|docdb|
|9|DynamoDB|dynamodb|
|10|Elastic Block Store (EBS)|ebs|
|11|EC2 (SecurityGroup, AMI, EIP)|ec2|
|12|Elastic Container Registry (ECR)|ecr|
|13|Elastic Container Service (ECS)|ecs|
|14|Elastic File System (EFS)|efs|
|15|Elastic Kubernetes Service (EKS)|eks|
|16|Elasticache|elasticache|
|17|Elastic Load Balancer (ELB)|elbv2|
|18|Identity Access Management (IAM)|iam|
|19|Kinesis Data Stream|kinesis|
|20|Kinesis Firehose|firehose|
|21|Key Management System (KMS)|kms|
|22|Lambda|lambda|
|21|Managed Streaming for Apache Kafka (MSK)|msk|
|22|Relational Database Service (RDS)|rds|
|23|Redshift|redshift|
|24|Route53|route53|
|25|Simple Cloud Storage (S3)|s3|
|26|Secrets Manager|secretsmanager|
|27|Simple Notification Service (SNS)|sns|
|28|Simple Queue Service (SQS)|sqs|
|29|Virtual Private Cloud (VPC)|vpc|

---

## Authentication Overview

Registered service account on SpaceONE must have certain permissions to collect cloud service data Please, set
authentication privilege for followings:

<pre>
<code>
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "acm:Describe*",
                "acm:List*",
                "apigateway:GET",
                "application-autoscaling:Describe*",
                "autoscaling:Describe*",
                "cloudfront:List*",
                "cloudtrail:Describe*",
                "cloudtrail:Get*",
                "cloudtrail:List*",
                "cloudwatch:Describe*",
                "cloudwatch:Get*",
                "cloudwatch:List*",
                "directconnect:Describe*",
                "dynamodb:Describe*",
                "dynamodb:List*",
                "ec2:Describe*",
                "ecr:Describe*",
                "ecr:List*",
                "ecs:Describe*",
                "ecs:List*",
                "eks:Describe*",
                "eks:List*",
                "elasticache:Describe*",
                "elasticache:List*",
                "elasticfilesystem:Describe*",
                "elasticloadbalancing:Describe*",
                "firehose:Describe*",
                "firehose:List*",
                "health:Describe*",
                "iam:Get*",
                "iam:List*",
                "kafka:Describe*",
                "kafka:List*",
                "kinesis:Describe*",
                "kinesis:List*",
                "kms:Describe*",
                "kms:Get*",
                "kms:List*",
                "lambda:List*",
                "lambda:Get*",
                "rds:Describe*",
                "rds:List*",
                "redshift:Describe*",
                "route53:List*",
                "s3:Get*",
                "s3:List*",
                "secretsmanager:List*",
                "sns:Get*",
                "sns:List*",
                "sqs:Get*",
                "sqs:List*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
</code>
</pre>


---
## Options

### Cloud Service Type : Specify what to collect

If cloud_service_types is added to the list elements in options, only the specified cloud service type is collected.
By default, if cloud_service_types is not specified in options, all services are collected.

The cloud_service_types items that can be specified are as follows.

<pre>
<code>
{
    "cloud_service_types": [
        'IAM',          
        'DynamoDB',     
        'Lambda',       
        'CloudFront',
        'RDS',
        'Route53',
        'S3',
        'AutoScalingGroup',
        'ElastiCache',
        'APIGateway',
        'DirectConnect',
        'EFS',
        'DocumentDB',
        'ECS',
        'Redshift',
        'EKS',
        'SQS',
        'KMS',
        'ECR',
        'CloudTrail',
        'SNS',
        'SecretsManager',
        'ELB',
        'EIP',
        'EBS',
        'VPC',
        'EC2',
        'ACM',
        'KinesisDataStream',
        'KinesisFirehose',
        'MSK'
    ]
}
</code>
</pre>

How to update plugin information using spacectl is as follows.
First, create a yaml file to set options.

<pre>
<code>
> cat update_collector.yaml
---
collector_id: collector-xxxxxxx
options:
  cloud_service_types:
    - EC2
    - RDS
    - ELB
</code>
</pre>

Update plugin through spacectl command with the created yaml file.

<pre><code>
> spacectl exec update_plugin inventory.Collector -f update_collector.yaml
</code></pre>


## Release Note

### Ver 1.13.1-3
* Fix some bugs..!

### Ver 1.13
* Add feature to specify the Cloud Service Type and collect it.

### Ver 1.12
* Separated to setting the parameter and collecting resources.
* Fix some bug

### Ver 1.11.10
* Remove region_name filter in secret_data
* Fix some bug

### Ver 1.11.9
* (Fix bug) Modify get bucket location for S3 (set the default region when bucket was located is us-east-1)

### Ver 1.11.7
* Add attached instances information in Security Groups
* Add Target Groups, Instances information in Load Balancer

### Ver 1.11.6
* Add exceptions for S3 collecting logic

### Ver 1.11

* Add is_optional in Cloud Service Type metadata for Dynamic Tables
* (Fix Bug) Modify region_code for EKS Cluster

### Ver 1.10

* Add name field each cloud services for standardization


### Ver 1.9.3

* (Fix Bug) Modify node_count, shard_count in ElastiCache
* (Fix Bug) Modify unexpected region code in EKS Node Group
* (Fix Bug) Modify RDS Filter action
* Add search matched launch template to Auto Scaling Group through mixed instance policy info

### Ver 1.9.2

* Add Load Balancers in Auto Scaling Group
    * Group: Auto Scaling Group
    * Name : LoadBalaners
* Add related Auto Scaling Group ARNs in EKS

### Ver 1.9.1

* Add Node Group in EKS
    * Group: EKS
    * Name : NodeGroup

### Ver 1.9

* Add to supported Cloud Service
    * ElastiCache
        * Memcached
        * Redis

* Add related Launch Template detail data in Auto Scaling Group information
* Add releated ELB ARNs in Auto Scaling Group
* Add lifecycle(Spot or Scheduled) information in Auto Scaling Group's instances
* Fix bug, etc.

### Ver 1.8

* Add to supported Cloud Service
    * Amazon MSK (Managed Streaming for Apache)
        * Cluster
        * Cluster Configuration

    * Kinesis Data Stream
        * Data Stream

    * Kinesis Data Firehose
        * Delivery Stream

    * Amazon Certificate Manager (ACM)
        * Certificate
    
