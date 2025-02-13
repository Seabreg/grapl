import time
import boto3

table_names = [
    'process_history_table',
    'file_history_table',
    'node_id_retry_table'
]


for table_name in table_names:
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    table_description = dynamodb.describe_table(TableName=table_name)

    print(table_description['Table'])

    # delete table

    try:
        dynamodb.delete_table(TableName=table_name)
    except Exception as e:
        print('failed to delete')

    time.sleep(8)

    try:
        dynamodb.create_table(
            TableName=table_name,
            AttributeDefinitions=table_description['Table']['AttributeDefinitions'],

            BillingMode='PAY_PER_REQUEST',

            KeySchema=table_description['Table']['KeySchema'],

        )
    except:
        time.sleep(5)
        dynamodb.create_table(
            TableName=table_name,
            AttributeDefinitions=table_description['Table']['AttributeDefinitions'],

            BillingMode='PAY_PER_REQUEST',

            KeySchema=table_description['Table']['KeySchema'],

        )
