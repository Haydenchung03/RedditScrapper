import os
import requests
import urllib.request
from urllib.request import urlretrieve
import logging
from argparse import ArgumentParser
from urllib import request

# download_video_file_decorator, video_url_getter_decorator, streamable_video_download comes from https://github.com/id872/streamable-video-downloader
# Credit goes to him for those functions
class ExecutionError(Exception):
    pass

def download_video_file_decorator(func_decorated):
    def func_wrapper(*args, **kwargs):
        direct_video_url = func_decorated(*args, **kwargs)

        if not direct_video_url or 'https://' not in direct_video_url:
            raise ExecutionError('Video URL not found')

        patterns = '/video/mp4/', '?'
        file_name = direct_video_url.split(patterns[0])[1].split(patterns[1])[0] \
            if patterns[0] in direct_video_url else 'video.mp4'
        
        logging.info('Direct link:\n%s\nDownloading...', direct_video_url)
        with open(f"videos/{file_name}", 'wb') as video_file:
            # download the video into the videos folder
            pass
            video_file.write(request.urlopen(direct_video_url).read())
        logging.info('Video downloaded')

    return func_wrapper


def video_url_getter_decorator(fun_decorated):
    def func_wrapper(*args, **kwargs):
        html_content = fun_decorated(*args, **kwargs)
        patterns = '<meta property="og:video:url" content="', '">'
        return html_content.split(patterns[0])[1].split(patterns[1])[0] \
            if patterns[0] in html_content else None

    return func_wrapper


@download_video_file_decorator
@video_url_getter_decorator
def streamable_video_download(streamable_link):
    try:
        logging.info('Downloading video from: %s', streamable_link)
        return str(request.urlopen(streamable_link).read())
    except Exception as exc:
        raise ExecutionError('Error: could not download data from {}'.format(streamable_link)) \
            from exc


def main():
    logging.basicConfig(format="%(asctime)s-%(levelname)s -- %(message)s", level=logging.INFO)


    try:
        file_path = "highlights.txt"

        folder_name = "videos"

        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        with open(file_path, "r") as file:
           
            for line in file:
                

                if "https://streamable.com/" in line:
                    
                    video_url = line.strip()
                    
                   
                    video_id = video_url[-6:]
                    
                    response = requests.get(f"https://streamabledl.com/{video_id}")
                
                    if response.status_code == 200:
                        streamable_video_download(f"https://streamable.com/{video_id}")
                    else:
                        print("Failed to download video. Status code:", response.status_code)
    except ExecutionError as ex_err:
        logging.error(ex_err)


if __name__ == "__main__":
    main()

