from unittest import TestCase
from unittest.mock import call, patch

import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def setUp(self):
        # general setup before running all tests goes here
        pass

    def test_print_blogs(self):
        blog = Blog("Test Blog", "Test Author")
        app.blogs = { "Test Blog": blog }
        # patching print function: checking that it was called, with what argument
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called()
            mocked_print.assert_called_with(
                "Blog. Title: Test Blog. "
                "Author: Test Author. Post count: 0"
            )
        app.blogs = {}
    
    def test_print_no_blogs(self):
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("No blogs yet")

    
    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value="q") as _:
                app.menu()
                mocked_print_blogs.assert_called()
    
    def test_fetch_blog(self):
        blog = Blog("Title", "Author")
        app.blogs = {"One": blog }
        with patch("builtins.input", return_value="One"):
            returned_blog = app.fetch_blog()
            self.assertEqual(blog, returned_blog)
        app.blogs = dict()
    
    def test_ask_create_post(self):
        blog = Blog("Title", "Author")
        blog.create_post("Title1", "Content1")
        blog.create_post("Title2", "Content2")
        with patch("app.fetch_blog", return_value=blog):
            with patch("builtins.print") as patched_print:
                with patch("builtins.input"):
                    app.ask_read_blog()
                    patched_print.assert_called()
                    patched_print.assert_any_call(blog)
                    for post in blog.posts:
                        patched_print.assert_any_call(post)
        # ver tambien: call_args_list
    
    def test_ask_create_blog(self):
        with patch("builtins.input") as mocked_input:
            # the tuple states the return values for each call to the patched function
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))
    
    def test_ask_read_blog(self):
        blog = Blog("Title", "Author")
        blog.create_post("Title1", "Content1")
        blog.create_post("Title2", "Content2")
        with patch("app.fetch_blog", return_value=blog) as patched_fetch:
            with patch("builtins.print") as patched_print:
                app.ask_read_blog()
                calls = [call(blog), call(blog.posts[0]), call(blog.posts[1]),]
                patched_print.assert_has_calls(calls)
    
    def test_ask_read_blog2(self):
        blog = Blog("Title", "Author")
        blog.create_post("Title1", "Content1")
        blog.create_post("Title2", "Content2")
        with patch("app.fetch_blog", return_value=blog):
            with patch("builtins.print") as patched_print:
                with patch("builtins.input"):
                    app.ask_read_blog()
                    patched_print.assert_called()
                    patched_print.assert_any_call(blog)
                    for post in blog.posts:
                        patched_print.assert_any_call(post)
        # ver tambien: call_args_list
    
    def test_ask_create_post(self):
        blog = Blog("Title", "Author")
        app.blogs = { "Title": blog }
        with patch("app.fetch_blog", return_value=blog):
            with patch("builtins.input") as patched_input:
                patched_input.side_effect = ("Post title", "Post content")
                app.ask_create_post()
                expected = [Post("Post title", "Post content")]
                self.assertListEqual(app.blogs["Title"].posts, expected)
    
    @patch("builtins.print")
    def test_menu_calls_create_blog(self, _):
        with patch("builtins.input") as patched_input:
            with patch("app.ask_create_blog") as patched_create_blog:
                patched_input.side_effect = ("c", "Title", "Author", "q")
                app.menu()
                patched_create_blog.assert_called()