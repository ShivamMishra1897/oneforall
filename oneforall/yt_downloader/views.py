from django.shortcuts import render,redirect
from .models import Video
from pytube import YouTube, Playlist
# imoport re
'''
class Youtube():

    def check_for_playlist(request):
        link = ''
        playlist_links = ['https://www.youtube.com/playlist?list=','https://www.youtube.com/watch?v=']
        if link:
            try:
                stream = re.findall(r"",playlist_links)
            except Exception as e:
                break
        return render(request,'ytdownload.html')

    def playlist():
        if request.method == "POST":
            link=""
            playlist = playlist(link)
            for video in playlist:
                stream = video.streams.get_by_resolution
                stream.download()        
                return render(request,'ytdownload.html')
            return render(request,'ytdownload.html')

    def download_video():
        if request.method=="POST"
            url=""
            if "playlist" in url:
                pl = Playlist(url)
                for video in pl:
                    stream=video.streams.get_by_resolution
                    stream.download()
                    return render(request,".html")
            else:
                vi = Youtube(url)
                stream=vi.streams.get_by_resolution
                stream.download()
                return render(request,".html")
'''

def youtube_downloader(request):
    if request.method == "POST":

        link = request.POST['url_link']
        video = YouTube(link)

        stream = video.streams.get_by_resolution()

        stream.download()
        
        return render(request,'ytdownload.html')
    return render(request,'ytdownload.html')