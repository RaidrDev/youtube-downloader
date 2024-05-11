from pytube import YouTube

def download_video():
    url = input("Enter the url of the video: ")
    yt = YouTube(url)
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    
    print("1. Download video")
    option = int(input("Enter the option: "))

    if option == 1:
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Download complete")
    else:
        print("Invalid option")

download_video()