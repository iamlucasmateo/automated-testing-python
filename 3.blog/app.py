from blog import Blog

MENU_PROMPT = (
    "Enter 'c' to create a blog, "
    "'l' to list blogs, 'r' tp read one, "
    "'p' to create a new post "
)

blogs = dict() # blog_name to Blog object


def menu():
    # Show available blogs
    # User chooses
    # Do something with choice
    # exit
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)



def print_blogs():
    if len(blogs) == 0:
        print("No blogs yet")
        return
    for title, blog in blogs.items():
        print(str(title))
        print(str(blog))

def ask_create_blog():
    title = input("Blog title? ")
    author = input("Blog author? ")
    blogs.update({title: Blog(title, author)})

def ask_read_blog():
    blog = fetch_blog()
    print(blog)
    for post in blog.posts:
        print(post)

def fetch_blog():
    which_blog = input("Which blog?")
    while which_blog not in blogs:
        which_blog = input("Which blog?")
    return blogs[which_blog]

def ask_create_post():
    blog = fetch_blog()
    title = input("Post title? ")
    content = input("Post content? ")
    blog.create_post(title, content)

if __name__ == "__main__":
    menu()