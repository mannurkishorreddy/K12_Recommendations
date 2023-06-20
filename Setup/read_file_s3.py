#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:46:37 2023

@author: naman
"""

import boto3
import io
import pandas as pd
import os

session = boto3.Session(region_name = os.getenv('region_name'),
                        aws_access_key_id = os.getenv('aws_access_key_id'),
                        aws_secret_access_key = os.getenv('aws_secret_access_key'))

bucket = 'data-mining-project-learning-equality'

s3 = session.resource('s3')

obj = s3.Object(bucket , 'learning-equality-curriculum-recommendations/topics.csv')
file_content = obj.get()['Body'].read().decode('utf-8')
topics = pd.read_csv(io.StringIO(file_content))

obj = s3.Object(bucket , 'learning-equality-curriculum-recommendations/correlations.csv')
file_content = obj.get()['Body'].read().decode('utf-8')
correlations = pd.read_csv(io.StringIO(file_content))

obj = s3.Object(bucket , 'learning-equality-curriculum-recommendations/sample_submission.csv')
file_content = obj.get()['Body'].read().decode('utf-8')
sample_submission = pd.read_csv(io.StringIO(file_content))


obj = s3.Object(bucket , 'learning-equality-curriculum-recommendations/content.csv')
file_content = obj.get()['Body'].read().decode('utf-8')
content = pd.read_csv(io.StringIO(file_content))
