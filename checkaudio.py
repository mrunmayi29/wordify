import urllib2
import os,sys

#from django.conf import settings
import hashlib
import time
#stpath = settings.STATIC_PATH+'/audio'
def populate():
	objlist=[]
	stpath="/home/mrunmayi/wordify-new/static/audio"
	objlist=Word.objects.filter().order_by('-word')
	for i in objlist:
	    cword = i.word
	    filename = 'w'+hashlib.sha1(cword).hexdigest()
	    filepath = stpath+'/'+filename+'.mp3'
	    #print filepath
	    if os.path.isfile(filepath):
		#print 'the file is already present for word:', cword
		continue;
	    print 'file not present for word:',cword
	    

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
