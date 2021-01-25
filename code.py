from pytube import YouTube as ytb
from pytube import Playlist as ply
import os
while True:
    print("Welcome to MiDownloader Script :")
    down_option=int(input("What do you want to download ?\n1.video\n2.Playlist\n\t> option : "))

    if down_option== 1:
        url = ytb(input("enter The video url : "))
        download_option=int(input("Download options :\n1.highest resolution\n2.lowest resolution\n3.advanced options\n\t>option : "))

        if download_option==1:
            path=input("Download path (type \"default\" for download video in current path) : ").lower()
            if path=="default":
                print(f"downloading : {url.title}")
                url.streams.get_highest_resolution.download()
            else:
                print(f"downloading : {url.title}")
                url.streams.get_highest_resolution.download(output_path=path)
        elif download_option == 2:
            path=input("Download path (type \"default\" for download video in current path) : ").lower()
            if path=="default":
                print(f"downloading : {url.title}")
                url.streams.get_lowest_resolution.download()
            else:
                url.streams.get_lowest_resolution.download(output_path=path)
        elif download_option == 3:
            advance_option=int(input("what Do you want :\n1.Thumbnail link\n2.Infos(title,description,rating,views,length,etc)\n> option : "))
            if advance_option==1:print(f"Thumbnail URL : {url.thumbnail_url}")
            elif advance_option==2:
                print(f"infos : \ntitle : {url.title}")
                print(f"description : \n**********\n{url.description}\n**********\n")
                print(f"rating : \n\t{round(url.rating,2)} ")
                print(f'views : \n\t{url.views} ')
                print(f'length in minutes : \n\t{round((url.length/60),2)}')
            else:
                print("Script will restart!!")
                continue
    elif down_option==2:
        url=ply(input("enter The playlist url : "))
        download_option=int(input("Download options :\n1.highest resolution\n2.lowest resolution\n\t>option : "))
        if download_option==1:
            path=input("Download path (type \"default\" for download video in current path) : ").lower()
            if path=="default":
                for video in path.videos:
                    print(f"downloading : {video.title}")
                    video.streams.get_highest_resolution.download()
            else:
                for video in path.videos:
                    print(f"downloading : {video.title}")
                    video.streams.get_highest_resolution.download(output_path=path)
        elif download_option == 2:
            path=input("Download path (type \"default\" for download video in current path) : ").lower()
            if path=="default":
                for video in url.videos:
                    print(f"downloading : {video.title}")
                    video.streams.get_lowest_resolution.download()
            else:
                for video in url.videos:
                    print(f"downloading : {video.title}")
                    video.streams.get_lowest_resolution.download(output_path=path)
    else:
        print("Restart the script. You have entered the wrong option !")

    # script restarting option :
    if input("Do you want Restart script (Y/n) ?").lower()=="y":
        os.system("cls")
        continue
    else:
        print("see you later!")
        break

exit()