import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods.media import GetMediaItem, GetMediaLibrary, UploadFile
from wordpress_xmlrpc import xmlrpc_client

wp = Client('http://www.vfvrpq.cn/xmlrpc.php', email , password)

# get all blogs
# print wp.call(GetPosts())

# get user info
# print wp.call(GetUserInfo())


#create a new blog
#post = WordPressPost()
#post.title = 'My new title'
#post.content = 'This is the body of my new post.'
#post.terms_names = {
#    'post_tag' : ['test'],
#    'category' : ['Tests']
#}
#wp.call(NewPost(post))


# get all the media
#print wp.call(GetMediaLibrary(100)) # max num

# get media of id=2
# print wp.call(GetMediaItem(2)) # id

# upload a picture to wordpress

def uploadToWordpress(image,name,type = 'image/jpeg'):
    data = {
        'name': name,
        'type': type
    }
    data['bits'] = xmlrpc_client.Binary(image)
    return wp.call(UploadFile(data))


file = open('/Users/chaojielyu/Desktop/IMG_3522.jpg', 'rb')
print uploadToWordpress(file.read(),'IMG_3522.jpg','image/jpeg')