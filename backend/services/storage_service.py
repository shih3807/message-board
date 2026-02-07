from fastapi import UploadFile
import boto3
from botocore.exceptions import ClientError
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

def get_s3_client():
    try:
        s3_client = boto3.client('s3', region_name=os.getenv('AWS_REGION'))
        s3_client.list_buckets()
        return s3_client
    except ClientError as e:
            print("S3 upload error:", e)
            return boto3.client(
            's3',
            region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )


s3_client = get_s3_client()


class StorageService:
    @staticmethod
    def save_image(image: UploadFile | None):

        if not image:
            return None

        file_ext = image.filename.split(".")[-1] #type:ignore
        file_name = f"{uuid.uuid4()}.{file_ext}"

        try:
            s3_client.upload_fileobj(
                image.file,
                os.getenv('AWS_S3_BUCKET_NAME'),
                file_name,
                ExtraArgs={"ContentType": image.content_type}
            )

            file_url = f"https://{os.getenv('CLOUDFRONT_DOMAIN')}/{file_name}"

            return file_url
        except ClientError as e:
            print("S3 upload error:", e)
            return None
