import os
import paramiko
from dotenv import dotenv_values

class CloudConnection:
    sftp = None
    transport = None
    
    def init(self):
        self.open_connection()

    def open_connection(self):
        self.transport = paramiko.Transport((os.environ["CLOUD_HOSTNAME"], 22))
        self.transport.connect(None, os.environ["CLOUD_USERNAME"], os.environ["CLOUD_PASSWORD"])
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        print ("Connection succesfully stablished ... ")
    
    def list(self):
        directory_structure = self.sftp.listdir_attr(os.environ["CLOUD_PATH"])
        folder_dict = {}
        for attr in directory_structure:
            folder_dict[attr.filename] = attr
        return folder_dict

    def download_file(self, remoteFilePath, localFilePath):
        self.sftp.get(remoteFilePath, localFilePath)

    def download_cloud_files(self):
        list = self.list()
        try:
            os.mkdir("csv_files")
        except:
            print("warning directory exists")
        for key in list.keys():
            self.download_file(os.environ["CLOUD_PATH"] + "/" + key, "csv_files/" + key)
        if self.sftp: self.sftp.close()
        if self.transport: self.transport.close()

    def run_test(self):
        self.download_cloud_files()
