import os
import random
import string
import time
import requests

def generate_file_name() -> str:

    file_name = "".join(
        random.choices(string.ascii_uppercase + string.ascii_lowercase+ string.digits, k=100)
    )
    return file_name


def download_image(location: str= "downloaded_images", files_count :int = 1):
    try:
        os.mkdir(location)
    except FileExistsError:
        pass
    for i in range(0, files_count):
        try:
            file_name = location+'/'+generate_file_name()+'.jpg'
            print(f"Downloading file: {file_name}")
            f = open(file_name,'wb')
            f.write(requests.get('https://dummyimage.com/600x400/000/fff&text=Rajan').content)
            f.close()
        except:
            raise IOError



def main():
    # Generate 20 files
    files_count = 100
    start_t = time.perf_counter()
    
    for f in range(0, files_count):
        download_image()
    
    end_t = time.perf_counter()
    
    total_duration = end_t - start_t
    
    print(f"Non-parallel Run: Generated files = {files_count} Total time taken {total_duration:.2f}s total")


if __name__ == "__main__":
    main()
