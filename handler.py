import json
import boto3
from botocore.exceptions import ClientError

def send_email(event, context):
    body = json.loads(event['body'])
    receiver_email = body.get('receiver_email')
    subject = body.get('subject')
    body_text = body.get('body_text')

    if not receiver_email or not subject or not body_text:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing required fields: receiver_email, subject, and body_text"})
        }

    ses_client = boto3.client('ses', region_name='us-east-1')

    try:
        response = ses_client.send_email(
            Source='tamannachoudhary8797@gmail.com',
            Destination={
                'ToAddresses': [receiver_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body_text
                    }
                }
            }
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }
