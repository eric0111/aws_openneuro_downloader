import csv
import boto3
from botocore import UNSIGNED
from botocore.config import Config
import os

DOWNLOAD_FOLDER = '../bin/downloaded/'
PARTECIPANTS_FILE = "../bin/participants.tsv"

def main():
    with open(PARTECIPANTS_FILE) as file:
        tsv_file = csv.reader(file, delimiter="\t")

        s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
        bucket = "openneuro"
        folder = "ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/"

        for line in tsv_file:
            patient = line[0]
            if patient != "participant_id":
                sub_folder =  patient + "/func/"
                file = patient + "_task-stopsignal_bold_space-MNI152NLin2009cAsym_preproc.nii.gz"

                print("downloading: " + line[0])

                downloaded_files = os.listdir(DOWNLOAD_FOLDER)

                print(file)

                if(file not in downloaded_files):
                    s3_client.download_file(bucket, folder+sub_folder+file, DOWNLOAD_FOLDER+ file)
                    print(line[0] + "-> downloaded :)")

main()