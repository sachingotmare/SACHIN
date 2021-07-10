# Python Code to list all my IAM users

import boto3
client = boto3.client('iam', aws_access_key_id = "AKIARWDEXATL7BGBB5Y2", aws_secret_access_key = "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")

response = client.list_users()
#print (response['Users'])

for i in response['Users']:
	print (i['UserName'], i['CreateDate'])