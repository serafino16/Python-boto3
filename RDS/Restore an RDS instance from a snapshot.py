import boto3

def restore_rds_instance_from_snapshot(snapshot_identifier, db_instance_identifier):
    rds = boto3.client('rds')
    response = rds.restore_db_instance_from_db_snapshot(
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass='db.t2.micro'
    )
    print(f'Restored RDS instance: {response["DBInstance"]["DBInstanceIdentifier"]}')

restore_rds_instance_from_snapshot('snapshot', 'instance')