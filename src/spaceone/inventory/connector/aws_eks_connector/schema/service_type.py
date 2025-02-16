import os
from spaceone.inventory.libs.common_parser import *
from spaceone.inventory.libs.schema.dynamic_widget import ChartWidget, CardWidget
from spaceone.inventory.libs.schema.dynamic_field import TextDyField, EnumDyField, SearchField, ListDyField
from spaceone.inventory.libs.schema.resource import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

current_dir = os.path.abspath(os.path.dirname(__file__))

"""
CLUSTER
"""
total_count_conf = os.path.join(current_dir, 'widget/total_count.yaml')
count_by_region_conf = os.path.join(current_dir, 'widget/count_by_region.yaml')
count_by_account_conf = os.path.join(current_dir, 'widget/count_by_account.yaml')

cst_eks_cluster = CloudServiceTypeResource()
cst_eks_cluster.name = 'Cluster'
cst_eks_cluster.provider = 'aws'
cst_eks_cluster.group = 'EKS'
cst_eks_cluster.labels = ['Container', 'Compute']
cst_eks_cluster.is_primary = True
cst_eks_cluster.is_major = True
cst_eks_cluster.service_code = 'AmazonEKS'
cst_eks_cluster.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Elastic-Kubernetes-Service.svg',
}

cst_eks_cluster._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'name'),
        TextDyField.data_source('Version', 'data.version'),
        EnumDyField.data_source('Status', 'data.status', default_state={
            'safe': ['ACTIVE'],
            'warning': ['CREATING', 'DELETING', 'UPDATING'],
            'alert': ['FAILED']
        }),
        TextDyField.data_source('ARN', 'data.arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Role ARN', 'data.role_arn', options={
            'is_optional': True
        }),
        TextDyField.data_source('Endpoint', 'data.endpoint', options={
            'is_optional': True
        }),
        ListDyField.data_source('Node Group ARNs', 'data.node_groups', options={
            'delimiter': 'nodegroup_arn',
            'is_optional': True
        }),
        ListDyField.data_source('Node Group names', 'data.node_groups', options={
            'delimiter': 'nodegroup_name',
            'is_optional': True
        }),
        ListDyField.data_source('Node Role ARNs', 'data.node_groups', options={
            'delimiter': 'node_role',
            'is_optional': True
        }),
        TextDyField.data_source('VPC ID', 'data.resources_vpc_config.vpc_id', options={
            'is_optional': True
        }),
        ListDyField.data_source('Subnets', 'data.resources_vpc_config.subnet_ids', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        ListDyField.data_source('Public Access CIDRs', 'data.resources_vpc_config.public_access_cidrs', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        TextDyField.data_source('Cluster Security Group ID', 'data.resources_vpc_config.cluster_security_group_id', options={
            'is_optional': True
        }),
        TextDyField.data_source('Endpoint Public Access', 'data.resources_vpc_config.endpoint_public_access', options={
            'is_optional': True
        }),
        TextDyField.data_source('Endpoint Private Access', 'data.resources_vpc_config.endpoint_private_access', options={
            'is_optional': True
        }),
        ListDyField.data_source('Cluster Logging Enabled', 'data.logging.cluster_logging', options={
            'delimiter': 'enabled',
            'is_optional': True
        }),
        TextDyField.data_source('OIDC issuer', 'data.identity.oidc.issuer', options={
            'is_optional': True
        }),
        TextDyField.data_source('Platform Version', 'data.platform_version', options={
            'is_optional': True
        })
    ],
    search=[
        SearchField.set(name='Cluster Name', key='name'),
        SearchField.set(name='ARN', key='data.arn'),
        SearchField.set(name='Status', key='data.status',
                        enums={
                            'ACTIVE': {'label': 'ACTIVE', 'icon': {'color': 'green.500'}},
                            'CREATING': {'label': 'CREATING', 'icon': {'color': 'yellow.500'}},
                            'UPDATING': {'label': 'UPDATING', 'icon': {'color': 'yellow.500'}},
                            'DELETING': {'label': 'DELETING', 'icon': {'color': 'yellow.500'}},
                            'FAILED': {'label': 'FAILED', 'icon': {'color': 'red.500'}},
                        }),
        SearchField.set(name='Cluster Version', key='data.version'),
        SearchField.set(name='Cluster Endpoint', key='data.endpoint')
    ],
    widget=[
        CardWidget.set(**get_data_from_yaml(total_count_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_region_conf)),
        ChartWidget.set(**get_data_from_yaml(count_by_account_conf)),
    ]
)


"""
NODE GROUP
"""
cst_eks_nodegrp = CloudServiceTypeResource()
cst_eks_nodegrp.name = 'NodeGroup'
cst_eks_nodegrp.provider = 'aws'
cst_eks_nodegrp.group = 'EKS'
cst_eks_nodegrp.labels = ['Container', 'Compute']
cst_eks_nodegrp.service_code = 'AmazonEKS'
cst_eks_nodegrp.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-Elastic-Kubernetes-Service.svg',
}

cst_eks_nodegrp._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Node Group Name', 'name'),
        TextDyField.data_source('EKS Cluster Name', 'data.cluster_name'),
        TextDyField.data_source('Version', 'data.version'),
        EnumDyField.data_source('Status', 'data.status', default_state={
            'safe': ['ACTIVE'],
            'warning': ['CREATING', 'UPDATING', 'DELETING'],
            'alert': ['CREATE_FAILED', 'DELETE_FAILED', 'DEGRADED'],
        }),
        ListDyField.data_source('Instance Types', 'data.instance_types', options={
            'delimiter': '<br>'
        }),
        TextDyField.data_source('ARN', 'data.nodegroup_arn', options={
            'is_optional': True
        }),
        ListDyField.data_source('Auto Scaling Group ARN', 'data.resources.auto_scaling_groups', options={
            'delimiter': '<br>',
            'sub_key': 'arn',
            'is_optional': True
        }),
        ListDyField.data_source('Auto Scaling Group Name', 'data.resources.auto_scaling_groups', options={
            'delimiter': '<br>',
            'sub_key': 'name',
            'is_optional': True
        }),
        TextDyField.data_source('Scaling Config: Desired Size', 'data.scaling_config.desired_size', options={
            'is_optional': True
        }),
        TextDyField.data_source('Scaling Config: Min Size', 'data.scaling_config.min_size', options={
            'is_optional': True
        }),
        TextDyField.data_source('Scaling Config: Max Size', 'data.scaling_config.max_size', options={
            'is_optional': True
        }),
        ListDyField.data_source('Subnets', 'data.subnets', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        ListDyField.data_source('Instance Types', 'data.instance_types', options={
            'delimiter': '<br>',
            'is_optional': True
        }),
        TextDyField.data_source('Remote Access Security Group', 'data.resources.remote_access_security_group', options={
            'is_optional': True
        }),
        TextDyField.data_source('AMI Type', 'data.ami_type', options={
            'is_optional': True
        }),
        TextDyField.data_source('Disk Size', 'data.disk_size', options={
            'is_optional': True
        }),
        TextDyField.data_source('Node Role ARN', 'data.node_role', options={
            'is_optional': True
        }),
        TextDyField.data_source('EC2 SSH Key', 'data.remote_access.ec2_ssh_key', options={
            'is_optional': True
        }),
        TextDyField.data_source('Release Version', 'data.release_version', options={
            'is_optional': True
        })
    ],
    search=[
        SearchField.set(name='Node Group ARN', key='data.nodegroup_arn'),
        SearchField.set(name='Status', key='data.status'),
        SearchField.set(name='EKS Cluster Name', key='data.cluster_name'),
        SearchField.set(name='EKS Cluster ARN', key='data.cluster_arn'),
        SearchField.set(name='Version', key='data.version'),
        SearchField.set(name='Instance Type', key='data.instance_types'),
        SearchField.set(name='Subnet', key='data.subnets'),
        SearchField.set(name='Node Role', key='data.node_role'),
        SearchField.set(name='Disk Size', key='data.disk_size', data_type='integer'),
        SearchField.set(name='Modification Time', key='data.modified_at', data_type='datetime'),
    ]
)


CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_eks_cluster}),
    CloudServiceTypeResponse({'resource': cst_eks_nodegrp}),

]
