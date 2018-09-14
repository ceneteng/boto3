#!/bin/python

import boto3
import json

region = "us-east-1"
ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2', region_name=region)
vFilter = [{'Name':'tag:Name', 'Values':['*Dev']}]
vpcs = list(ec2.vpcs.filter(Filters=vFilter))
vIds = []
myIns = []
instances = ec2.instances.all()
for vpc in vpcs:
	
	for tag in vpc.tags:
	    if tag["Value"] == 'myDev':
		vIds.append(vpc.vpc_id)
print vIds

for instance in instances:
	if instance.vpc_id in vIds:
		print instance.tags
		instance.create_image(Name = instance.instance_id)
		myIns.append(instance.instance_id)

print myIns

#images = list(ec2.image.filter(Filters=[{'Name': 'owner-id', 'Values': ['896917285996']}]))

waitImg = client.get_waiter('image_available')
for ins in myIns:
	waitImg.wait(
		Filters = [{

			'Name': 'name',
			'Values': [
				ins, 
			]
		},
	],
		Owners=['896917285996'],
	)



	# for instance in instances:
		
	#         if instance.vpc_id in vIds:
	#                 instance.terminate()
				
