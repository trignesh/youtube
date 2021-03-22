#!/bin/python
'''This program will download video from youtube
based on input given url link from youtube and
It will saving it with name given by 3rd argument.
It used pytube module'''
from pytube import YouTube
import sys

if len(sys.argv) < 2:
	print("Usage:\nNeed more arguments,\n <script> Youtube_video_link saving_file_name.mp4")
	exit(-1)
link=sys.argv[1]
print(link)
print(sys.argv[2])
try:
	y=YouTube(link)
	v=y.streams.first().download(sys.argv[2])
except:
	print("error\n")