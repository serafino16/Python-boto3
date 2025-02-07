import boto3

def describe_rds_instance(db_instance_identifier):
    rds = boto3.client('rds')
    response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
    print(response['DBInstances'][0])

describe_rds_instance('')