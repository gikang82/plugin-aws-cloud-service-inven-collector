import time
import logging
from typing import List

import boto3

from spaceone.inventory.connector.aws_secrets_manager_connector.schema.data import Secret
from spaceone.inventory.connector.aws_secrets_manager_connector.schema.resource import SecretResource, \
    SecretResponse
from spaceone.inventory.connector.aws_secrets_manager_connector.schema.service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.libs.connector import SchematicAWSConnector


_LOGGER = logging.getLogger(__name__)


class SecretsManagerConnector(SchematicAWSConnector):
    service_name = 'secretsmanager'
    cloud_service_group = 'SecretsManager'
    cloud_service_type = 'Secret'

    def get_resources(self) -> List[SecretResource]:
        _LOGGER.debug("[get_resources] START: Secrets Manager")
        resources = []
        start_time = time.time()

        collect_resource = {
            'request_method': self.request_data,
            'resource': SecretResource,
            'response_schema': SecretResponse
        }

        # init cloud service type
        for cst in CLOUD_SERVICE_TYPES:
            resources.append(cst)

        # merge data
        for region_name in self.region_names:
            self.reset_region(region_name)
            resources.extend(self.collect_data_by_region(self.service_name, region_name, collect_resource))

        _LOGGER.debug(f'[get_resources] FINISHED: Secrets Manager ({time.time() - start_time} sec)')
        return resources

    def request_data(self, region_name) -> List[Secret]:
        paginator = self.client.get_paginator('list_secrets')
        response_iterator = paginator.paginate(
            PaginationConfig={
                'MaxItems': 10000,
                'PageSize': 50,
            }
        )

        for data in response_iterator:
            for raw in data.get('SecretList', []):
                try:
                    raw['region_name'] = region_name
                    raw['account_id'] = self.account_id

                    secret_vo = Secret(raw, strict=False)
                    yield {
                        'data': secret_vo,
                        'name': secret_vo.name,
                        'account': self.account_id
                    }
                    
                except Exception as e:
                    resource_id = raw.get('ARN', '')
                    error_resource_response = self.generate_error(region_name, resource_id, e)
                    yield {'data': error_resource_response}
