import json
import boto3
import os
import uuid
from urllib.parse import urlparse

def lambda_handler(event, context):
    # Initialize clients
    s3_client = boto3.client('s3')
    transcribe_client = boto3.client('transcribe')
    
    try:
        # Get the source bucket and file key from the event
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # Generate a unique job name
        job_name = f'transcription-{str(uuid.uuid4())}'
        
        # Create the S3 URI for the audio file
        s3_uri = f's3://{source_bucket}/{file_key}'
        
        # Start transcription job
        response = transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': s3_uri},
            MediaFormat='webm',  # Adjust based on your audio format
            LanguageCode='en-US',  # Adjust based on your language needs
            OutputBucketName='student-progress-recordings',
            OutputKey=file_key.replace('recordings/', 'transcriptions/').replace('.webm', '.json')
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Transcription job started successfully',
                'jobName': job_name,
                'jobStatus': response['TranscriptionJob']['TranscriptionJobStatus']
            })
        }
        
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing audio file: {str(e)}')
        }