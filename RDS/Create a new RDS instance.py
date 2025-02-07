import boto3

def create_rds_instance(db_instance_identifier, db_instance_class, engine, master_username, master_user_password):
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        AllocatedStorage=20
    )
    print(f'Created RDS instance: {response["DBInstance"]["DBInstanceIdentifier"]}')

create_rds_instance('mydbinstance', 'db.t2.micro', 'mysql', 'admin', 'password')