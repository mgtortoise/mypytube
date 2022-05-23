from pytube import YouTube

# def vid_download(url):
#      vid_me = YouTube(url)
     
#      for i in vid_me.streams.filter(only_audio=True):
#          print(i)
#          vid_me.streams.get_by_itag('139').download()

# vid_download('https://www.youtube.com/watch?v=icPHcK_cCF4')

yt = YouTube('https://www.youtube.com/watch?v=icPHcK_cCF4')
t = yt.streams.filter(only_audio = True)
print(t[0])
t[0].download()