#!/usr/bin/python

regions = ['us-west-1','us-west-2','us-east-1']
import boto3

for reg in regions:
	ec2 = boto3.resource('ec2',region_name=reg)

	for volume in ec2.Volume.all():
		print(volume.id)
