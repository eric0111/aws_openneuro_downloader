import csv
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import os

DOWNLOAD_FOLDER = '../bin/downloaded/'
PARTECIPANTS_FILE = "../bin/participants.tsv"


def downloader():
    with open(PARTECIPANTS_FILE) as file:
        tsv_file = csv.reader(file, delimiter="\t")

        s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
        bucket = "openneuro"
        folder = "ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/"

        for line in tsv_file:
            patient = line[0]
            if patient != "participant_id":
                sub_folder = patient + "/func/"
                file = patient + "_task-stopsignal_bold_space-MNI152NLin2009cAsym_preproc.nii.gz"

                downloaded_files = os.listdir(DOWNLOAD_FOLDER)

                if (file not in downloaded_files):
                    try:
                        print("downloading:   \n" + file)
                        s3_client.download_file(bucket, folder + sub_folder + file, DOWNLOAD_FOLDER + file)
                        print(line[0] + "-> downloaded :)")
                    except Exception as e:
                        print("task not present for " + patient)
