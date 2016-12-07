import boto3
s3 = boto3.resource('s3')
client = boto3.client('rekognition')
for bucket in s3.buckets.all():
    print("===== %s contents: %s" % (bucket.name , bucket) )
    if bucket.name == 'ddmcanon':
        objects = [ o for o in bucket.objects.all() if o.key[-1] != '/']
        print( bucket, len(objects) )
        for object in objects:
            print ( " -> [%s] [%s]" % (object.bucket_name, object.key) )
            response = client.detect_labels(
                                            Image={
                                                'S3Object': {
                                                    'Bucket': object.bucket_name,
                                                    'Name': object.key,
                                                }
                                            },
                                            MaxLabels=10,
                                            MinConfidence=.5
            )
            print(str(object.key) + " --- " + str(response))
            out_file = open('outcomes/' + object.key.split('/')[1] + '.outcome', "w")
            out_file.write(str(response ))
            out_file.close()
