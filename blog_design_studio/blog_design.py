class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    # Allow people to "like" posts, a la Facebook
    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author


class VideoPost(Post):
    def __init__(self, title, author, url):
        Post.__init__(self, title, author, None)
        self.video_url = url
        self.plays = 0

    # track plays of the video
    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " played " + str(self.plays) + " times"

class ImagePost(Post):
    def __init__(self, title, author, file_name):    
        super().__init__(title, author, file_name)
        self.file_name = file_name

class LinkPost(Post):
    def __init__(self, title, author, url):
        super().__init__(title, author, url)
        self.clicks = 0
        self.url = url

    def click(self):
        self.clicks += 1

    def __str__(self):
        return "{} by {} \n{}".format(self.title, self.author, self.url)

img = ImagePost("rape me", "Nirvana", "nirvana.img")
link = LinkPost("kitties", "bubbles", "www.trailerparkboys.com")

print(img)
print(link)
