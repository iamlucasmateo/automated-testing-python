from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        test_title = "Test title"
        test_content = "Test content"
        p = Post(test_title, test_content)
        self.assertEqual(test_title, p.title)
        self.assertEqual(test_content, p.content)
    
    def test_json(self):
        test_title, test_content = "Test", "Test content"
        p = Post(test_title, test_content)
        expected = {
            "title": test_title,
            "content": test_content,
        }
        self.assertDictEqual(expected, p.json())
    
    def test_str(self):
        title = "test title"
        content = "test content"
        actual = str(Post(title, content))
        expected = f"Post. Title: {title}. Content: {content}"
        self.assertEqual(expected, actual)
