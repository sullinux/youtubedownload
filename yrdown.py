##########################################
#                                       ##
# YouTube Downloader Highest Resolution ##
#            WWW.Sullinux.Com           ##       
##########################################
from pytube import YouTube
video_link = input("enter video link : ")
ytd = YouTube(video_link)
print("title: ",ytd.title)
print("numbers of viws : ",ytd.views)
print("length of video", ytd.length,"seconds")
print("Ratings : ", ytd.rating)
print(ytd.streams)
print(ytd.streams.filter(only_audio=True))
print(ytd.streams.filter(only_video=True))
print(ytd.streams.filter(progressive=True))
ys =ytd.streams.get_highest_resolution()
ys = ytd.streams.get_by_itag("22")
ys.download()
ys.download("location")
"""
Instgram : Sullinux_com
Site: http://www.sullinux.com
Author : Sullinux
"""
