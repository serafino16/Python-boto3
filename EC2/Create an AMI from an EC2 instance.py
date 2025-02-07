import boto3

def create_ami(instance_id, name):
    ec2 = boto3.client('ec2')
    response = ec2.create_image(InstanceId=instance_id, Name=name)
    print(f'Created AMI: {response["ImageId"]}')


create_ami('instance-id', 'ami-name')