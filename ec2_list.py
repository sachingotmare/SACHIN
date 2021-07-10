# Python Code to list all my Ec2 Instances
import boto3
import csv 

def any_name(writer):
	client = boto3.client('ec2', region_name="eu-central-1", aws_access_key_id = "AKIAVCKCW4AJHRTOOFXR", aws_secret_access_key = "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")
	empty_dict = {}
	response = client.describe_instances()
	#print (response['Reservations'])
	for i in response['Reservations']:
		#print(i['Instances'])
		for j in i['Instances']:

			empty_dict["AMI_ID"] = j['ImageId']
			empty_dict["INSTANCE_ID"] = j['InstanceId']
			empty_dict["INSTANCE_TYPE"] = j['InstanceType']
			empty_dict["KEY_NAME"] = j['KeyName']
			writer.writerow(empty_dict)
	print ("CSV Excel format Output Generated Successfully")

def main():
	fieldnames = ["AMI_ID","INSTANCE_ID","INSTANCE_TYPE","KEY_NAME"]
	file_name = "empty_dict.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		any_name(writer)	
main()		