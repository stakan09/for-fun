import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb.Table('test')
response = table.put_item(
    Item = {
        'test1':'1',
        'test2':'2',
    }
)

print(response)