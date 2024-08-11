from pytube import YouTube
import os

try:
    yt = YouTube(str(input("Enter the video link to download: ")))

    video = yt.streams.filter(only_audio=True).first()

    print("Enter the destination (leave blank for current directory)") 
    destination = str(input(">> ")) or '.'

    out_file = video.download(output_path=destination) 

    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
   
    if os.path.exists(new_file):
        print(f"File '{new_file}' already exists. Renaming skipped.")
    else:
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded as MP3.")

except Exception as e:
    print(f"An error occurred: {e}")
