# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:21:31 2019

@author: martarto

Función que lista los buckets existentes en AWS S3

Uso: listar_bucket_s3()

"""

def listar_buckets_s3():

    import boto3
    client = boto3.client('s3')

    response = client.list_buckets()

            # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print (f'  {bucket["Name"]}')