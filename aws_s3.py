import boto3
import botocore

# Define your AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'


class S3Access:

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.access_key = aws_access_key_id
        self.secret_key = aws_secret_access_key
        self.region = region_name
        self.s3_object = None

    def get_s3_client(self) -> None:
        """
        Function is used to get S3 Client
        :return: None
        """
        try:
            s3_object = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key,
                         region_name=self.region)
            self.s3_object = s3_object
            return True, s3_object
        except Exception as ex:
            return False, f'Not Able to create encounter error :{ex}'

    def create_bucket(self, bucket_name) -> None:
        """
        # Function to create an S3 bucket
        :param bucket_name: name of the bucket
        :return: None
        """
        try:
            self.s3_object.create_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} created successfully.")
        except botocore.exceptions.ClientError as e:
            print(f"Error: {e}")

    # Function to upload a file to an S3 bucket
    def upload_file(self, bucket_name, file_name, object_name) -> None:
        try:
            self.s3_object.upload_file(file_name, bucket_name, object_name)
            print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
        except botocore.exceptions.ClientError as e:
            print(f"Error: {e}")

    def delete_file(self, bucket_name, object_name) -> None:
        """
        Function to delete a file from an S3 bucket
        :param bucket_name: name of the bucket
        :param object_name: file name which need to be deleted
        :return: None
        """

        try:
            self.s3_object.delete_object(Bucket=bucket_name, Key=object_name)
            print(f"File {object_name} deleted from {bucket_name}")
        except botocore.exceptions.ClientError as e:
            print(f"Error: {e}")

    def download_file(self, bucket_name, object_name, file_name) -> None:
        """
        # Function to download a file from an S3 bucket
        :param bucket_name: name of the bucket
        :param object_name: file name store in s3
        :param file_name: file to use to download
        :return: None
        """
        try:
            self.s3_object.download_file(bucket_name, object_name, file_name)
            print(f"File {object_name} downloaded as {file_name}")
        except botocore.exceptions.ClientError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    obj_ = S3Access(aws_access_key_id, aws_secret_access_key, region_name)
    obj_.create_bucket(bucket_name)
    obj_.upload_file(bucket_name, 'local-file.txt', 'remote-file.txt')
    obj_.download_file(bucket_name, 'remote-file.txt', 'downloaded-file.txt')
    obj_.delete_file(bucket_name, 'remote-file.txt')
