import boto3
import logging
from botocore.exceptions import ClientError
import json
import os

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Constants
TOPIC_ARN = os.getenv("SNS_TOPIC_ARN") 
PROTOCOL = "email"  # Replace with your desired protocol

def lambda_handler(event, context):
    """
    AWS Lambda handler to subscribe an email address to an SNS topic.
    
    :param event: The Lambda event containing subscription details.
        Example:
        {
            "endpoint": "example@example.com"
        }
    :param context: Lambda context (not used here).
    :return: Response with subscription ARN or an error message.
    """
    sns_client = boto3.client('sns')
    
    # Extract the endpoint from the event
    
    try:
        
        endpoint = event['endpoint']
    except KeyError as e:
        logger.error("Missing required key: %s", e)
        return {
            "statusCode": 400,
            "body": f"Error: Missing required key {e} in event."
        }
    
    try:
        # Subscribe to the topic with predefined protocol and topic_arn
        response = sns_client.subscribe(
            TopicArn=TOPIC_ARN,
            Protocol=PROTOCOL,
            Endpoint=endpoint,
            ReturnSubscriptionArn=True
        )
        subscription_arn = response.get('SubscriptionArn', 'PendingConfirmation')
        logger.info(
            "Successfully subscribed %s to topic %s with protocol %s.",
            endpoint, TOPIC_ARN, PROTOCOL
        )
        return {
            "statusCode": 200,
            "body": {
                "message": f"Subscription request sent for {endpoint}.",
                "subscription_arn": subscription_arn
            }
        }
    except ClientError as e:
        logger.exception("Failed to subscribe %s to topic %s.", endpoint, TOPIC_ARN)
        return {
            "statusCode": 500,
            "body": {
                "error": "Failed to subscribe.",
                "message": str(e)
            }
        }
