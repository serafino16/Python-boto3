import boto3

def restore_volume(snapshot_id, availability_zone):
    ec2 = boto3.client('ec2')
    response = ec2.create_volume(SnapshotId=snapshot_id, AvailabilityZone=availability_zone)
    print(f'Restored volume: {response["VolumeId"]}')


restore_volume('snapshot-id', 'availability-zone')