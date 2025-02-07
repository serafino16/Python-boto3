import boto3

def modify_rds_instance(db_instance_identifier, new_db_instance_class):
    rds = boto3.client('rds')
    response = rds.modify_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass=new_db_instance_class,
        ApplyImmediately=True
    )
    print(f'Modified RDS instance: {response["DBInstance"]["DBInstanceIdentifier"]}')


modify_rds_instance('instance', 'db.t2.small')