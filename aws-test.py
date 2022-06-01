import boto3
from logging import getLogger
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

#from logging import getLoggerしてlogger.errorって感じで使うらしい
logger = getLogger(__name__)

#dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
#table = dynamodb.Table('test')
#response = table.put_item(
#    Item = {
#        'test1':'1',
#        'test2':'2',
#    }
#)

#print(response)

class Kintore:
    """Encapsulates an Amazon DynamoDB table of movie data."""
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        self.table = None

    def create_table(self, table_name):
        """
        Creates an Amazon DynamoDB table that can be used to store movie data.
        The table uses the release year of the movie as the partition key and the
        title as the sort key.

        :param table_name: The name of the table to create.
        :return: The newly created table.
        """
        try:
            self.table = self.dyn_resource.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'Day', 'KeyType': 'HASH'},  # Partition key
                    {'AttributeName': 'Where', 'KeyType': 'RANGE'}  # Sort key
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'Day', 'AttributeType': 'S'},
                    {'AttributeName': 'Where', 'AttributeType': 'N'}
                ],
                ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})
            self.table.wait_until_exists()
        except ClientError as err:
            logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return self.table

    def add_movie(self, Day, Where, Type, Weight, Reps):
        """
        Adds a movie to the table.
        :param title: The title of the movie.
        :param year: The release year of the movie.
        :param plot: The plot summary of the movie.
        :param rating: The quality rating of the movie.
        """
        try:
            self.table.put_item(
                Item={
                    'Day': Day,
                    'Where': where,
                    'info': {'Type': Type, 'Weight': Weight, 'Reps': Reps}})
        except ClientError as err:
            logger.error(
                "Couldn't add movie %s to table %s. Here's why: %s: %s",
                title, self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise

dynamodb=Kintore(boto3.resource('dynamodb',region_name='us-east-1'))
#Kintore.create_table(dynamodb,'TrainingRecord')
Kintore.add_movie(dynamodb,20220601,Legs,Normal,0,0)#ここうまくいっていない