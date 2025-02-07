import boto3

def list_rds_snapshots():
    rds = boto3.client('rds')
    response = rds.describe_db_snapshots()
    for snapshot in response['DBSnapshots']:
        print(snapshot['DBSnapshotIdentifier'], snapshot['DBInstanceIdentifier'], snapshot['SnapshotCreateTime'])


list_rds_snapshots()