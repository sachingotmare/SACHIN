# Python Code to list all my EBS Vol
import boto3
client = boto3.client('ec2', region_name="eu-east-1", aws_access_key_id = "AKIARWDEXATL7BGBB5Y2", aws_secret_access_key = "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")
response = client.describe_volumes()
#print (response['Volumes'])

for i in response['Volumes']:
	#print (i['Attachments'])
	for j in i['Attachments']:
		print (j['InstanceId'], j['State'], j['VolumeId'])