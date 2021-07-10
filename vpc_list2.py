# Python Code to list all my VPC's....'''''
import boto3
client = boto3.client('ec2', region_name="eu-central-1", aws_access_key_id = "AKIAVCKCW4AJHRTOOFXR", aws_secret_access_key = "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")

response = client.describe_vpcs()
#print (response['Vpcs'])
for i in response['Vpcs']:
	print (i['CidrBlock'], i['VpcId'])
