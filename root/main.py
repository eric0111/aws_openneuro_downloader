import time
from root.downloader import downloader


def main():
    done = False

    while(not done):
        try:
            downloader()
            done = True
        except Exception as e:
                print(e)
                time.sleep(60)

main()