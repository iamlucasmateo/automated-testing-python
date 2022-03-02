from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []
    
    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [p.json() for p in self.posts],
        }
    
    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)
    
    def __repr__(self):
        return (
            f"Blog. Title: {self.title}. Author: {self.author}. " 
            f"Post count: {len(self.posts)}"
        )