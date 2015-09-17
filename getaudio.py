import urllib2
import os,sys

#from django.conf import settings
import hashlib
import time
#stpath = settings.STATIC_PATH+'/audio'
def populate():
	objlist=[]
	stpath="/home/mrunmayi/wordify-masteratta/static/audio"
	objlist=Word.objects.filter().order_by('-word')
	for i in objlist:
	    cword = i.word
	    if(cword=="Vituperative "):
		print "nako"
		continue;
	    filename = 'w'+hashlib.sha1(cword).hexdigest()
	    filepath = stpath+'/'+filename+'.mp3'
	    print filepath
	    if os.path.isfile(filepath):
		print 'the file is already present for word:', cword
		continue
	    print 'file not present for word:',cword
	    PATH = 'https://api.voicerss.org/?key=ab3334fbd85148b6965b2fc8c10fb402&src='+cword+'&hl=en-gb&f=24khz_16bit_stereo'
	    response = ''
	    while True:
		print 'in the loop:',cword
		try:
		    print 'trying to open url:',PATH
		    response = urllib2.urlopen(PATH)
		    print 'successful:', cword
		    time.sleep(2)
		    print 'successful sleep complete',cword
		    break;
		except:
		    print 'there was error:',cword
		    time.sleep(2)
		    print 'error sleep complete',cword
	    print response
	    audiocontents = response.read()
	    newfile = open(filepath, 'wb')
	    newfile.write(audiocontents)
	    print 'written',newfile.tell(),'bytes'
	    newfile.close()

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordify.settings')
    from words.models import Word
    populate()

	    
# print html
# response = urllib2.urlopen(html);
# audiocontents = response.read()
# newfile.write(audiocontents)
# newfile.write(html)
# newfile.close()
