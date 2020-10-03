from test_abc import ABC

import os, boto3
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from google.cloud import storage


class StorageClient(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def open(self):
        pass



class AwsClient(StorageClient):
    def __init__(self):
        self.session = boto3.Session(
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        )
    
    def open(self):
        with open(url, 'wb', transport_params={'session': self.session}) as fout:
            bytes_written = fout.write(b'hello world!')
            print(bytes_written)



class AzureClient(StorageClient):
    def __init__(self):
        token_credential = DefaultAzureCredential()

        blob_service_client = BlobServiceClient(
            account_url="https://<my_account_name>.blob.core.windows.net",
            credential=token_credential
        )
    
    def open(self):
        pass
    

class GoogleClient(StorageClient):
    client = storage.Client()
    bucket = client.get_bucket('bucket-id-here')
    blob = bucket.get_blob('remote/path/to/file.txt')
    print(blob.download_as_string())
    blob.upload_from_string('New contents!')
    blob2 = bucket.blob('remote/path/storage.txt')
    blob2.upload_from_filename(filename='/local/path.txt')


class ServerClient(StorageClient):
    def __init__(self, url):
        super().__init__()



class BaseEdl(ABC):
    def __init__(self):
        super().__init__()
    
    def __enter__(self):
        self.client = client
    
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def check(self):
        pass



class IPList(BaseEdl):
    def __init__(self):
        super().__init__()
    
    def add(self):
        pass
    
    def remove(self):
        pass
    
    def check(self):
        pass


class URLList(BaseEdl):
    def __init__(self):
        super().__init__()
    
    def add(self):
        pass
    
    def remove(self):
        pass
    
    def check(self):
        pass


class DomainList(BaseEdl):
    def __init__(self):
        super().__init__()
    
    def add(self):
        pass
    
    def remove(self):
        pass
    
    def check(self):
        pass

    


ip_list = IPEDLList()
print(ip_list)

aws = AwsClient()
print(aws)



