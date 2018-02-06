import os,time
import glob,string
inpath='part2/'
outpath='converted/'
os.chdir(inpath)
onlyfiles = glob.glob('*.webm')

alpha=list(string.ascii_lowercase)

for i in range(0,len(onlyfiles)):
	st = onlyfiles[i][20:-5]
	print st
	os.system("vlc "+ onlyfiles[i] + " :sout='#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100}:std{access=file{no-overwrite},mux=mp4,dst='"+outpath+alpha[i]+'.mp4} vlc://quit')
	time.sleep(1)
	