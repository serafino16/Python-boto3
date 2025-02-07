import boto3

def start_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id])
    print(f'Started instance: {instance_id}')


start_instance('')