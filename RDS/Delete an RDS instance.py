import boto3

def delete_rds_instance(db_instance_identifier):
    rds = boto3.client('rds')
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        SkipFinalSnapshot=True
    )
    print(f'Deleted RDS instance: {response["DBInstance"]["DBInstanceIdentifier"]}')

delete_rds_instance('mydbinstance')