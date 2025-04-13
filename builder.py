import boto3
import os
import json
import time
from datetime import datetime
import speech_recognition as sr
import tempfile
import wave

class RecordingBuilder:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = 
        self.transcriptions_path = 
        self.recognizer = sr.Recognizer()

    def create_folder_structure(self):
        today = datetime.now()
        folder_path = f"{self.transcriptions_path}/{today.year}/{today.month:02d}/{today.day:02d}"
        return folder_path

    def convert_audio_to_text(self, audio_file_path):
        """Convert audio file to text using speech recognition."""
        try:
            print(f"Converting audio to text: {audio_file_path}")
            
            # Check if file is webm and convert to wav if needed
            if audio_file_path.endswith('.webm'):
                # For webm files, we'd normally need to convert them
                # This is a simplified example - in production you would use 
                # something like ffmpeg to convert webm to wav
                print("Note: Actual implementation would convert webm to wav using ffmpeg")
                # For demo purposes, assuming it's already a compatible format
            
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio_data)
                return text
        except Exception as e:
            print(f"Error in speech recognition: {str(e)}")
            return "Error transcribing audio: " + str(e)

    def process_recording(self, audio_file_path):
        try:
            # Convert audio to text
            transcription_text = self.convert_audio_to_text(audio_file_path)
            
            # Create folder structure for storing the text
            folder_path = self.create_folder_structure()
            base_filename = os.path.basename(audio_file_path).replace('.webm', '')
            
            # Create paths for both JSON and TXT files
            json_filename = f"{base_filename}.json"
            txt_filename = f"{base_filename}.txt"
            
            json_key = f"{folder_path}/{json_filename}"
            txt_key = f"{folder_path}/{txt_filename}"
            
            # Create a JSON structure for the transcription
            transcription_data = {
                "status": "COMPLETED",
                "transcriptText": transcription_text,
                "timestamp": datetime.now().isoformat()
            }
            
            # Upload JSON transcription to S3
            print(f"Uploading JSON transcription to S3: {json_key}")
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=json_key,
                Body=json.dumps(transcription_data),
                ContentType='application/json'
            )
            
            # Upload TXT transcription to S3
            print(f"Uploading TXT transcription to S3: {txt_key}")
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=txt_key,
                Body=transcription_text,
                ContentType='text/plain'
            )

            print(f"Transcriptions uploaded successfully: {json_key} and {txt_key}")
            
            # Save the transcription locally as a TXT file
            local_txt_path = f"{base_filename}.txt"
            with open(local_txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(transcription_text)
            print(f"Transcription saved locally as: {local_txt_path}")
            
            return {
                'json_key': json_key,
                'txt_key': txt_key,
                'transcription_text': transcription_text,
                'local_txt_path': local_txt_path
            }

        except Exception as e:
            error_message = f"Error processing recording: {str(e)}"
            print(error_message)
            return {
                'error': error_message,
                'status': 'FAILED'
            }