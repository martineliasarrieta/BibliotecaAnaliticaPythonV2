# -*- coding: utf-8 -*-
"""
Created on 2019

@author: martarto

Funcion que carga un archivo local a AWS S3

Uso: 
    cargar_s3('D:/Usuarios/martarto/Desktop/holamundo.csv', 
                  'landing-zone-analitica', 
                  'martin-analitica','holamundo.csv')
    
Desde Jupyter, para subir archivo en la misma ubicación del notebook
de trabajo:
    cargar_s3('holamundo.csv', 
               'landing-zone-analitica', 
               'martin-analitica','holamundojupyter3.csv')
"""

import boto3
from botocore.exceptions import NoCredentialsError


def cargar_s3(local_file, bucket_name, folder, s3_file_name):
    s3 = boto3.resource('s3')
    path = folder +'/'+ s3_file_name

    try:
        s3.meta.client.upload_file(local_file, bucket_name, path)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

