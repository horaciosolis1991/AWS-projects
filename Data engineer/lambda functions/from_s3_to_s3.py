import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        #response = s3.get_object(Bucket=bucket, Key=key)
        s3 = boto3.resource('s3')
        copy_source = {
            'Bucket': bucket,
            'Key': key
        }
        obj = s3.Object(bucket,key)
        file_content = obj.get()['Body'].read().decode("utf-8")
        print('move object2')
        client = boto3.client('s3')
        client.put_object(Body=file_content, Bucket='poc-dest-bucket', Key='poc-dataset.json')
        print('succesfull')
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
