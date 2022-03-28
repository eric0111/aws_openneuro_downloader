import time
from root.downloader import downloader
from root.utils import print_files_in_folder


def main():
    #### SETTINGS ####
    ##inputs
    partecipants_file = "../bin/participants.tsv"
    bucket = "openneuro"
    bucket_folder = "ds000030/ds000030_R1.0.5/uncompressed/derivatives/fmriprep/"
    task = "bart" #stopsignal

    files_to_download = "_task-"+task+"_bold_space-MNI152NLin2009cAsym_preproc.nii.gz"
    confounds_to_download = "_task-"+task+"_bold_confounds.tsv"

    export_folder =  "/Users/eb/Desktop/bart/" #"/Users/eb/Desktop/stopsignal/"
    export_confounds_folder = "/Users/eb/Desktop/bart_confounds/" #"/Users/eb/Desktop/stopsignal_confounds/"

    ##commands
    print_files_in_bucket = False
    download_files = True
    download_confounds = False

    #PRINT FILES IN BUCKET
    if(print_files_in_bucket):
        print_files_in_folder(bucket, bucket_folder)

    #### DOWNLOAD ####
    if(download_files):
        done = False

        while(not done):
            try:
                downloader(partecipants_file, bucket, bucket_folder, files_to_download, export_folder)
                done = True
            except Exception as e:
                    print(e)
                    time.sleep(60)

    if (download_confounds):
        done = False

        while (not done):
            try:
                downloader(partecipants_file, bucket, bucket_folder, confounds_to_download, export_confounds_folder)
                done = True
            except Exception as e:
                print(e)
                time.sleep(60)

main()