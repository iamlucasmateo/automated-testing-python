from unittest import TestCase

from blog import Blog
from post import Post

class BlogTest(TestCase):
    def test_create_post(self):
        blog = Blog("title", "author")
        blog.create_post("post title", "post content")
        blog.create_post("post title2", "post content2")
        expected = [
            Post("post title", "post content"),
            Post("post title2", "post content2")
        ]
        self.assertListEqual(expected, blog.posts)