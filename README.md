**Meeting Summarizer and Task Extractor**

**Project Overview**
This project provides an end-to-end solution to record meetings, convert audio into text, summarize discussions, and extract tasks and roles automatically. The final output is securely stored and distributed to meeting participants, helping improve meeting documentation and action tracking.

**Tech Stack**

Frontend

HTML5
CSS3
JavaScript
Flask (Python-based backend framework)
Dashboard for audio upload and meeting management

**Backend**
AWS Cognito & IAM for authentication and authorization
AWS S3 for storing uploaded audio and summarized content
AWS Lambda for serverless backend processing
Pyaudio for audio preprocessing
AWS Comprehend for basic text analysis
AWS Bedrock for hosting advanced models
Titan Model for summarization and task extraction
AWS SES (Simple Email Service) for emailing summaries
Amazon Glacier (S3 Deep Archive) for long-term meeting archive

**Architecture Flow**

**Frontend Interaction**
Users upload meeting audio through the dashboard. Authentication is handled securely using Cognito and IAM.

**Storage and Preprocessing**
Uploaded audio is stored in S3. Lambda functions trigger audio-to-text conversion using Pyaudio, followed by text analysis using AWS Comprehend.

**Summarization and Task Extraction**
Text is processed through Bedrock services and the Titan Model to create a meeting summary, identify roles, and extract action items.

**Output Generation**
Summarized outputs are saved back into S3. Meeting summaries are emailed to participants via SES and archived into Amazon Glacier for long-term storage.

**Features**
Audio Upload and Processing
Secure User Authentication
Automatic Meeting Summarization
Task and Role Extraction
Email Notifications to Participants
Archiving Meeting Records for Long-Term Storage

**Setup Instructions**
Set up the frontend using HTML, CSS, JavaScript, and Flask.
Configure AWS services like Cognito, IAM roles, S3 buckets, Lambda functions, Bedrock models, Comprehend analysis, and SES email service.
Ensure security settings and email verifications are properly configured for a smooth flow of data and notifications.

**Future Enhancements**
Real-time meeting transcription and summarization
Downloadable Minutes of Meeting (MoM) in PDF or Word format
Multi-language meeting support
Dashboard analytics to track meetings and action items

**Dataflow Diagram**
![Screenshot 2025-04-18 142124](https://github.com/user-attachments/assets/7ce6a93c-830d-494e-819a-0805dec66049)
