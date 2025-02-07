import boto3

def create_rds_snapshot(db_instance_identifier, snapshot_identifier):
    rds = boto3.client('rds')
    response = rds.create_db_snapshot(
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceIdentifier=db_instance_identifier
    )
    print(f'Created snapshot: {response["DBSnapshot"]["DBSnapshotIdentifier"]}')


create_rds_snapshot('instance', 'snapshot')