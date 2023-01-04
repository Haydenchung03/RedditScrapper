import praw
from datetime import datetime, timedelta
import translate


def main():
    # Get the info from here (https://www.reddit.com/prefs/apps)
    reddit = praw.Reddit(client_id="vSRs9UEaiwTce92OkOgjcA",
                        client_secret="qO-ccY01tN_epr6Z3r0R3lvuYA9NXw",
                        user_agent="Basketball")

    # Set the subreddit to r/nba (Change to ur own liking)
    subreddit = reddit.subreddit("nba")

  
    highlights = []

    numberOfVideosSaved = 0;
    # time_filter is by the time period. It is set today but you can change to your own liking
    # Goes through the last 100 posts in the subreddit. 
    # Can't get it to only search the highlights so
    # it will search through the last 100 post and check if the tag has [highlight] or [highlights] 
    # 'time_filter' must be one of: 'day', 'all', 'hour', 'year', 'week', 'month'
    for submission in subreddit.top(limit=1000, time_filter = "week"):
        # This info here is onlpy for r/nba as the flair is Highlight or Highlights. Change it to ur own liking. 
        # Check if the post has the flair [highlight] and was posted in the last 24 hours
        # Change line 24 to see how many videos you want to save
        if(numberOfVideosSaved >= 1):
            break
        if (submission.link_flair_text == "Highlight" or submission.link_flair_text == "Highlights"):
            # If it does, add it to the list of highlights
            print("Found a highlight: + submission.title")
            highlights.append(submission)
            numberOfVideosSaved += 1
        

    # Open a file to save the highlights
    with open("highlights.txt", "w") as file:
        for highlight in highlights:
            # Save each highlight's title and URL to the file
            file.write(f"{highlight.title}\n{highlight.url}\n\n")



if __name__ == "__main__":
    main()
