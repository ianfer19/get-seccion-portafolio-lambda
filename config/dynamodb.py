import boto3
import os
dynamodb = boto3.resource("dynamodb")
table = os.environ.get('SECTIONS_TABLE', 'iam-portafolio-sections-pdn')
