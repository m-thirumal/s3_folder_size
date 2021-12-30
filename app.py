import logging
import boto3

from chalice import Chalice

app = Chalice(app_name='s3_folder_size', debug=True, configure_logs=True)
logging.getLogger().setLevel(logging.DEBUG)


@app.lambda_function()
def get_folder_size(event, context):
    bucket = event['bucket']
    path = event['path']
    logging.debug("The request is for the path {} of bucket {}".format(path, bucket))
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    total_size = 0
    for obj in my_bucket.objects.filter(Prefix=path):
        total_size = total_size + obj.size
    logging.debug("The size of path {} is {}".format(path, total_size))
    return total_size

