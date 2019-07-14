from troposphere import s3, Template
import boto3
import time

t = Template()

s3_bucket = s3.Bucket("davidsbucket", 
BucketName = "davidsawesomebucket"
)
t.add_resource(s3_bucket)

s3_bucket2 = s3.Bucket("davidsbucket2", 
BucketName = "davidsawesomebucket2"
)
t.add_resource(s3_bucket2)

print(t.to_yaml())
temp = open("cfn.yaml", "w+")
temp.write(t.to_yaml())
temp.close()