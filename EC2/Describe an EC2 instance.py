import boto3

def describe_instance(instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[instance_id])
    print(response['Reservations'][0]['Instances'][0])


describe_instance('')