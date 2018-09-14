#!/bin/python

import boto3
import json

region = "us-east-1"
ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2', region_name=region)
vFilter = [{'Name':'tag:Name', 'Values':['*Dev']}]
vpcs = list(ec2.vpcs.filter(Filters=vFilter))
vIds = []
iIds = []
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
		iIds.append(instance.instance_id)

images = list(ec2.image.filter(Filters=[{'Name': 'owner-id', 'Values': ['896917285996']}])
for i in iIds:
	ec2.image.wait_until_exists(
		Filters = [{

			'Name': 'name',
			'Values': [
				i, 

			]
		},
	],
		Owners=['896917285996'],
	)
	


# for instance in instances:
        
#         if instance.vpc_id in vIds:
#                 instance.terminate()
			
