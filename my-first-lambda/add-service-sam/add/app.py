import json

def lambda_handler(event, context):
    print(event)
    number_one = int(event["queryStringParameters"]["a"])
    number_two = int(event["queryStringParameters"]["b"])
    
    result = number_one + number_two
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }