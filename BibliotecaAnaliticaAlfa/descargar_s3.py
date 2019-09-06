# -*- coding: utf-8 -*-
"""
Created 2019

@author: martarto

Descarga archivos de S3 a local

Uso:
    
Descargar en el directorio local del Notebook de jupyter
    descargar_s3('landing-zone-analitica', 
                  'martin-analitica', 
                  'holamundojupyter4.csv', 
                  'holamundojupyter5.csv')
    
Descargar en directorio local del PC    
    descargar_s3('landing-zone-analitica', 
                  'martin-analitica', 
                  'holamundojupyter4.csv', 
                  'D:/Usuarios/martarto/Desktop/holamundojupyter5.csv')
"""

import boto3
from botocore.exceptions import NoCredentialsError


def descargar_s3(bucket, folder, s3_file_name, output_location):
    
    s3 = boto3.resource('s3')
    path = folder +'/'+ s3_file_name
    try:
        s3.meta.client.download_file(bucket, path, output_location) 
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False