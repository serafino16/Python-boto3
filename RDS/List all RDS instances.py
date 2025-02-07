import boto3

def list_rds_instances():
    rds = boto3.client('rds')
    response = rds.describe_db_instances()
    for db_instance in response['DBInstances']:
        print(db_instance['DBInstanceIdentifier'], db_instance['DBInstanceClass'], db_instance['Engine'])


list_rds_instances()