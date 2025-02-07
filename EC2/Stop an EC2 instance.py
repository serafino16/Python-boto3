import boto3

def stop_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopped instance: {instance_id}')


stop_instance('')