#!/usr/bin/env python

import amazon.ion.simpleion as ion
import os
import boto3
        
client = boto3.client('iot-data')

output_topic = os.environ['OutputTopic']

def function_handler(event, context): 
  return client.publish(topic = output_topic, qos = 0, payload = ion.dumps(event, binary=True))
