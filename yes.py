from yt_dlp import YoutubeDL
import math
import json

included = [

	"thumbnail",
	"duration", "webpage_url", "fulltitle", "format", "formatid",
	"filesize_approx", "resolution", "fps"

]

with YoutubeDL() as ydl: 
  info_dict = ydl.extract_info('https://www.youtube.com/watch?v=MPV7JXTWPWI', download=False)


  videoTitle = info_dict["title"]
  videoThumbnail = info_dict["thumbnail"]

  videoDuration = info_dict["duration"]
  videoMinutes = math.floor(videoDuration / 60)
  videoSeconds = str(videoDuration % 60) if (videoDuration % 60 > 9) else "0" + str(videoDuration % 60)
  videoDuration = str(videoMinutes) + ":" + videoSeconds

  videoURL = info_dict["webpage_url"]
  print(info_dict["fulltitle"])