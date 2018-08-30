#!/usr/bin/python

regions = ['us-west-1','us-west-2','us-east-1']
import boto3
import json

ec2 = boto3.client('ec2',region_name='us-east-1')

for instance in ec2.Instance.all():
	if ec2.state == stopped:
		print instance.instance_id
