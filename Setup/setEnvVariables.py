#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:49:58 2023

@author: naman
"""

import pandas as pd
import os
userName = os.getenv('aws_UserName')
df = pd.read_csv('Desktop/{}_accessKeys.csv'.format(userName))

os.environ['region_name'] = 'us-east-2'
os.environ['aws_access_key_id'] = df['Access key ID'][0]
os.environ['aws_secret_access_key'] = df['Secret access key'][0]