import boto3
import os
dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get('SECTIONS_TABLE', 'iam-portafolio-sections-pdn')
table = dynamodb.Table(table_name)
