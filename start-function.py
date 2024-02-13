import boto3
region = 'ap-northeast-2'
instances = ['instance-id']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
  ec2.start_instances(InstanceIds=instances)
  print('started your instances: ' + str(instances))