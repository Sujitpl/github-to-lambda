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
            # # # Redirect the URL
            # http = urllib3.PoolManager()
            # response = http.request(
            #     "GET",
            #     "https://www.google.com/search?q=birds&sxsrf=APwXEdfog0xuWijCyJ42EEeqUALcJtgHzQ%3A1685035577803&source=hp&ei=OZpvZKHYLeDn7_UPpOqU2A4&iflsig=AOEireoAAAAAZG-oSUOo5jMdDdLF6cFKNFVT_fQRdblC&oq=bir&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQigUQJzIHCAAQigUQQzIHCAAQigUQQzIKCC4QigUQ1AIQQzIHCAAQigUQQzIHCAAQigUQQzIFCAAQgAQyBQguEIAEMgUILhCABDIFCAAQgAQ6BwgjEOoCECc6CAgAEIoFEJECOggILhCABBDUAlDODFjnDmDYGmgBcAB4AIABdYgBvQKSAQMxLjKYAQCgAQGwAQo&sclient=gws-wiz",
            # )

            # r.data
            # b'User-agent: *\nDisallow: /deny\n'
            # r.status
            # 200

            # Redirect to the specified URL with the edited headers
            # return redirect(url, headers=headers)
            # print(headers)
            return response
        else:
            decoded_binary_secret = base64.b64decode(
                secret_value_response["SecretBinary"]
            )
            return decoded_binary_secret

