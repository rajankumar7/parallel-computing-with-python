import asyncio
import aiohttp
import os
import random
import string
import time

def generate_file_name() -> str:

    file_name = "".join(
        random.choices(string.ascii_uppercase + string.ascii_lowercase+ string.digits, k=100)
    )
    return file_name


async def download_image(location: str= "downloaded_files", files_count :int = 1, session = None):
    try:
        os.mkdir(location)
    except FileExistsError:
        pass
    for i in range(0, files_count):
        try:
            file_name = location+'/'+generate_file_name()+'.jpg'
            print(f"Downloading file: {file_name}")
            f = open(file_name,'wb')
            async with session.get('https://dummyimage.com/600x400/000/fff&text=Rajan') as response:
                content = await response.read()
                f.write(content)
            f.close()
        except:
            raise IOError




if __name__ == "__main__":
    
    start_t = time.perf_counter()
    files_count = 100
    
    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = [download_image("downloaded_files_asyncio", 1, session) for _ in range(files_count)]
            await asyncio.gather(*tasks)
    
    asyncio.run(main())

    end_t = time.perf_counter()
    
    total_duration = end_t - start_t
    
    print(f"Parellel-AsyncIO Run: Generated files = {files_count} Total time taken {total_duration:.2f}s total")