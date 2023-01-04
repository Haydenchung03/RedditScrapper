
Set up venv on windows
1. pip install virtualenv 
2. virtualenv venv
3. venv\Scripts\activate
4. deactivate (To exit)

Set up venv on Linux/Max
1. pip install virtualenv
2. virtualenv --version
3. virtualenv venv 
4. source venv/bin/activate
5. deactivate (To exit)

// To run this program, you much run these installation commands:

1. pip install -r requirements.txt

// To run the program:
1. Run scrapeClips.py to scrape reddit data onto highlights.txt
2. Run downloadVideos.py to download the videos from the txt file onto the folder "videos"
3. Configure the right paths and test out some uploads with instagramUpload.py

Currentely, it scrapes the top 1 highlight for r/nba, however, edit postClips.py values however you may like to scrape different subreddits 
and to scrape different amounts.

