#!/usr/bin/env python

import os
import sys
import datetime
from datetime import datetime, timedelta
from CloudformationManager import CloudFormationManager

region = 'eu-west-1'
use_iam_role = False

try:
    if use_iam_role:
        cf_manager = CloudFormationManager()
    else:
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
        cf_manager = CloudFormationManager(aws_secret_access_key=aws_secret_access_key, aws_access_key_id=aws_access_key_id, region_name=region)
except Exception as e:
    print "Set AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID env or set IAM role to instance that execute this script"
    sys.exit(-1)

def main():
    pass

def create_stack():
    try:
        out = cf_manager.create_stack_from_local_file(
            template_file='template-file.yml', 
            parameters_file='parameters-file.json',
            stack_name="stack-create-with-boto3")
        print out
    except Exception as e:
        print e


if __name__ == '__main__':
    cf_manager.cloudformation_client.delete_stack(StackName="stack-create-with-boto3")
