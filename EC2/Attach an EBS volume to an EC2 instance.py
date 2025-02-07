import boto3

def attach_volume(instance_id, volume_id, device):
    ec2 = boto3.client('ec2')
    ec2.attach_volume(InstanceId=instance_id, VolumeId=volume_id, Device=device)
    print(f'Attached volume: {volume_id} to instance: {instance_id}')


attach_volume('instance-id', 'volume-id', 'volume')