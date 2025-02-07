import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Log message from AWS Lambda')
    return {'statusCode': 200, 'body': 'Log written successfully'}