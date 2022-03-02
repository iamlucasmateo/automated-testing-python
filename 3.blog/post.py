class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        dict_repr = {
            "title": self.title,
            "content": self.content,
        }
        return dict_repr
    
        
    def __str__(self):
        return f"Post. Title: {self.title}. Content: {self.content}"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return (
            self.title == other.title
            and self.content == other.content
        )