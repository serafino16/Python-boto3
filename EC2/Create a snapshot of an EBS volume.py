import boto3

def create_snapshot(volume_id, description):
    ec2 = boto3.client('ec2')
    response = ec2.create_snapshot(VolumeId=volume_id, Description=description)
    print(f'Created snapshot: {response["SnapshotId"]}')


create_snapshot('volume-id', 'snapshot')
