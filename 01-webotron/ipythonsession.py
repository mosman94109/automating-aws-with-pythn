# coding: utf-8
import boto3
get_ipython().run_line_magic('cat', '~/.aws/config')
session = boto3.Session
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
