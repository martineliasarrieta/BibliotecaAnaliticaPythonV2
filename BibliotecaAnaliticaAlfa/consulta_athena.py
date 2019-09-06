# -*- coding: utf-8 -*-
"""
Created on 2019

@author: martarto

Función que realiza una consutla SQL a AWS athena, devuelve en 
dataframe una tabla.

Ejemplo de uso: 
consulta_athena('Group-Analitica', 
               'landing-zone-analitica', 
               'temp/athena/output',
               'dbtest01martin-analitica', 
               'SELECT * 
               FROM "dbtest01martin-analitica"."test01martin_analitica"'
               )    



"""

import boto3
import pandas as pd
import io
import re
import time

def consulta_athena(workgroup, bucket, path, database, query):
    
   
    client_athena = boto3.client('athena')
    client_s3     = boto3.client('s3')
    
    response = client_athena.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': database
            },
            ResultConfiguration={
                'OutputLocation': 's3://' + bucket + '/' + path
            },
            WorkGroup= workgroup
        )
    
    execution = response
    execution_id = execution['QueryExecutionId']
    state = 'RUNNING'
    max_execution = 5
    while (max_execution > 0 and state in ['RUNNING']):
        
        max_execution = max_execution - 1
        response2 = client_athena.get_query_execution(QueryExecutionId = execution_id)
    
        if 'QueryExecution' in response2 and \
                'Status' in response2['QueryExecution'] and \
                'State' in response2['QueryExecution']['Status']:
            state = response2['QueryExecution']['Status']['State']
            if state == 'FAILED':
                return False
            elif state == 'SUCCEEDED':
                s3_path = response2['QueryExecution']['ResultConfiguration']['OutputLocation']
                filename = re.findall('.*\/(.*)', s3_path)[0]
                #return filename
                s3_filename = filename
        time.sleep(1)
    s3_filename = filename        
            
    
    obj = client_s3.get_object(Bucket=bucket,
                              Key=path + '/' + s3_filename
                                )
    
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))  
    
    print('La cosulta se guardo en s3://'+bucket+'/'+path, ' nombrado con el codigo ', s3_filename)
    
    return df
   
   