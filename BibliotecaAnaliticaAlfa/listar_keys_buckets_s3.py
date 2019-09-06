# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 07:33:45 2019

@author: martarto


Lista detalla Keys de lo que esta dentro de un Bucket
Rutas completas de archivos

Uso:
    listar_keys_buckets_s3('landing-zone-analitica')

"""


import boto3 

def listar_keys_buckets_s3(zone_s3):
    
    client_s3 = boto3.client('s3')  
    for key in client_s3.list_objects(Bucket='landing-zone-analitica')['Contents']:
        print(key['Key'])
#Generalizado:
#bucket.get_subresource('landing-zone-analitica')