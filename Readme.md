# Ansible to deploy AWS Cloudformation through Troposphere

This example code is used to show how to leverage [Ansible](ansible.com) to deploy an AWS CloudFormation stack that was described using the open source python library [troposphere](https://github.com/cloudtools/troposphere).

## Installation of prereqs

This code uses python 3.

To install the prerequisites using pip3.

`pip3 install -r requirements.txt`

## Execution

`ansible-playbook -i localhost, deploy-cloudformation.yaml -e 'ansible_python_interpreter=/usr/bin/python3' -vvv`

The script uses the AWS credentials from the environment, so make sure you have your AWS profile configured.