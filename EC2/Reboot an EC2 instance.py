import boto3

def reboot_instance(instance_id):
    ec2 = boto3.client('ec2')
    ec2.reboot_instances(InstanceIds=[instance_id])
    print(f'Rebooted instance: {instance_id}')

# Example usage
reboot_instance('')