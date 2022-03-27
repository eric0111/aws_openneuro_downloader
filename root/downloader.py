import csv
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import os


def downloader(partecipants_file, bucket, folder, file_to_download, export_folder):
    with open(partecipants_file) as file:
        tsv_file = csv.reader(file, delimiter="\t")

        s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

        for line in tsv_file:
            patient = line[0]
            if patient != "participant_id":
                sub_folder = patient + "/func/"
                complete_file_to_download = patient + file_to_download

                downloaded_files = os.listdir(export_folder)

                if (file not in downloaded_files):
                    try:
                        print("downloading:   \n" + complete_file_to_download)
                        s3_client.download_file(bucket, folder + sub_folder + complete_file_to_download, export_folder + complete_file_to_download)

                        print(line[0] + "-> downloaded :)")
                    except Exception as e:
                        print("task not present for " + patient)
