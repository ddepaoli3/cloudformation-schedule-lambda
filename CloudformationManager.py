#!/usr/bin/env python

from boto3 import Session
import boto3
import datetime
import os
import json

class CloudFormationManager(Session):
    '''
    Class use to personal manage of cloudformation resources.
    It is inheritance from Session
    '''
    def __init__(self, *args, **kwargs):
        '''
        Init class. Take argument from Session boto3 class
        (http://boto3.readthedocs.io/en/latest/reference/core/session.html)
        '''
        super(CloudFormationManager, self).__init__(*args, **kwargs)
        self.session = boto3.Session(**kwargs)
        self.cloudformation_client = self.session.client(service_name='cloudformation')

    def get_all_stacks(self, **kwargs):
        '''
        Get a list of all stacks

        Args:
            arguments defined in http://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html#CloudFormation.Client.describe_stacks

        Returns:
            List of stacks
        '''
        output_list = []
        response = self.cloudformation_client.describe_stacks(**kwargs)
        for stack in response["Stacks"]:
            output_list.append(stack)
        return output_list

    def create_stack_from_local_file(self, template_file, parameters_file, stack_name):
        if os.path.exists(template_file):
            with open(template_file, 'rb') as f:
               try:
                   template_string = f.read()
               except :
                   raise Exception("Error in file {}".format(template_file))
        else:
            Exception("File {} not found".format(parameters_file))
        if os.path.exists(parameters_file):
            with open(parameters_file, 'rb') as f:
               try:
                   parameters_list = json.load(f)
               except :
                   raise Exception("Error in file {}".format(parameters_file))
        else:
            raise Exception("File {} not found".format(parameters_file))

        output = self.cloudformation_client.create_stack(TemplateBody=template_string, Parameters=parameters_list, StackName=stack_name, Capabilities=['CAPABILITY_IAM'])
        return output