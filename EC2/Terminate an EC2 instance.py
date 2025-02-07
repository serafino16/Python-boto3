import boto3

def terminate_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f'Terminated instance: {instance_id}')


terminate_instance('')