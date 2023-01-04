from instagrapi import Client
from instagrapi.types import Usertag, Location
from moviepy.editor import VideoFileClip
import imageio
import PIL
def main():
    client = Client()

    # Testing
    '''
    username = "USERNAME"
    password = "PASSWORD"
    try:
        client = Client("USERNAME", "PASSWORD")
        with open("savedLogins.txt", "w") as file:
            file.write(f"{username}\n{password}\n\n")
        client.login()
        print("Logged in")
    except:
        print("error")
    '''
    # Give instagram your username and password
    client.login("USERNAME", "PASSWORD")
    adw0rd = client.user_info_by_username('USERNAME')
    # Video path: "videos/{NAME OF VIDEO}"
    # Change it to automate by reading videos folder

    # Change to path of video downloaded to path
    
    video_path = "videos/w61or9.mp4"

    # All working: 
    # Upload to igtv: Needed stuff: Link to video, title, caption
    #client.igtv_upload(video_path, title = "My first automated video", caption="Testing")

    # Uploads as a reel
    #client.clip_upload(video_path, caption="Testing")

    # Uploads a photo
    #photo_path = "videos/laniebo01.jpg"
    #client.photo_upload(photo_path, caption="Testing")

    # Needs work:

    # Error I am getting: AttributeError: 'VideoFileClip' object has no attribute 'close'
    # Nvm i Dont know why it works now. It works today, will test tommorow. 
    client.video_upload(video_path, caption="Testing")

if __name__ == "__main__":
    main()
