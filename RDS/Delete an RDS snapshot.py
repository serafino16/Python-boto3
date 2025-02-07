import boto3

def delete_rds_snapshot(snapshot_identifier):
    rds = boto3.client('rds')
    response = rds.delete_db_snapshot(DBSnapshotIdentifier=snapshot_identifier)
    print(f'Deleted snapshot: {response["DBSnapshot"]["DBSnapshotIdentifier"]}')


delete_rds_snapshot('snapshot')