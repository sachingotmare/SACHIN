# Python Code to list all my S3

import boto3

client = boto3.client('S3', aws_access_key_id = "AKIARWDEXATL7BGBB5Y2", aws_secret_access_key = "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")

response = client.list_buckets()
#print (response['Buckets'])

for i in response['Buckets']:
	print (i['Name'], i['CreationDate'])