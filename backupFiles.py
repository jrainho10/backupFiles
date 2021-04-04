import datetime
import tarfile
import subprocess
import os
from pathlib import Path

now = datetime.datetime.now()
today_date = now.strftime("%m-%d-%Y_%H:%M:%S")
archive_name = "jrainho_backup_"+today_date+"_tar.gz"

certPath = "/Users/jrainho/aws-certs/aws_ubuntu.pem"
serverPath = "ubuntu@ec2-52-59-229-123.eu-central-1.compute.amazonaws.com:/home/ubuntu/"
archiveFilePath = str(Path().absolute())+"/"+archive_name

with tarfile.open(archive_name,mode="w:gz") as archive:
    archive.add("/Users/jrainho/backup")

p = subprocess.Popen(["scp","-i",certPath,archiveFilePath,serverPath])
sts = os.waitpid(p.pid, 0)
os.remove(archiveFilePath)