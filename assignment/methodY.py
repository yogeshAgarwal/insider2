import urllib.parse as urlparse
from urllib.parse import urlunparse
import urllib.request

def crop(width, height, url):
    o = urlparse.urlparse(url)
    i = o.path.index('/',1)
    temp1 =o.path[i+26:]
    desired_path='http://res.cloudinary.com/ifyogesh/image/upload/w_'+str(width)+',h_'+str(height)+',c_crop/'+str(temp1)
    name='w_'+str(width)+'h_'+str(height)+'.jpg'
    urllib.request.urlretrieve(desired_path,"assignment/static/assignment/"+name)

# url='http://res.cloudinary.com/ifyogesh/image/upload/v1558895854/atrpftvogyq1ykwzsdnh.jpg'
# crop(250,340, url)
# crop(380,380, url)
