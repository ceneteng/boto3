#!/usr/bin/python

import boto3

regions = 'us-east-1'

#instances = ec2.instances.filter(
#    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

#bScript = open("hw")
#myBash = bScript.read()


eConnect = boto3.client('ec2',region_name=regions)
ec2 = boto3.resource('ec2',region_name=regions)

response = eConnect.run_instances(KeyName='Mac',ImageId='ami-04681a1dbd79675a5', InstanceType='t2.micro',
 MaxCount=3, MinCount=3,
	NetworkInterfaces=[
        	{
            	'AssociatePublicIpAddress': True,
            	'DeviceIndex': 0,
            	'Groups': [
                'sg-0d1ea03c31dd340ad',
            	],
            	'SubnetId': 'subnet-03abf49d74f18618e'
        	},
    	    ],
	)


