from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    @staticmethod
    def get_mock_data():
        return "Test title","Test author",
    
    def test_create_blog(self):
        title, author = self.get_mock_data()
        blog = Blog(title, author)
        self.assertEqual(title, blog.title)
        self.assertEqual(author, blog.author)
        self.assertListEqual([], blog.posts)
    
    def test_repr(self):
        title, author = self.get_mock_data()
        expected = (
            f"Blog. Title: {title}. Author: {author}. " 
            "Post count: 0"
        )
        self.assertEqual(expected, str(Blog(title, author)))



