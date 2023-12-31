import json
import boto3
import base64
import botocore
import botocore.session



from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # environment = event['env']
    secret_name = "dev/test/apikey"
    region_name = "eu-north-1"

    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as error:
        print(error)
    else:
        if "SecretString" in secret_value_response:
            secret = json.loads(secret_value_response["SecretString"])
            # apikeyjson = json.loads(secret)
            apiVal = secret.get("dev-api-key")
            response = dict()
            response["statusCode"] = 302
            response["body"] = json.dumps(dict())
            response["headers"] = {"Location": "http://yahoo.com"}


           
            return response
        else:
            decoded_binary_secret = base64.b64decode(
                secret_value_response["SecretBinary"]
            )
            return decoded_binary_secret

