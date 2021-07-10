# Python Code to list all my EBS Vol
import boto3
client = boto3.client('ec2', region_name="eu-central-1", aws_access_key_id = "AKIAVCKCW4AJHRTOOFXR", aws_secret_access_key = "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")

response = client.describe_volumes()
#print (response['Volumes'])

for i in response['Volumes']:
#	print (i['Attachments'])
	for j in i['Attachments']:
		print (j['InstanceId'], j['State'], j['VolumeId'])