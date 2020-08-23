from pytube import YouTube


url = input("Enter video URL here: ")
 


try:
    print("[..] Connecting to Youtube.......")
    yt = YouTube(url)
    print("[..] Downloading.......")
    yt.streams.get_by_itag(22).download()
    print("[..] Download Complete!")
except Exception:
    print("Video could not download, Sorry.")