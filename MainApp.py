
import SQLConnector as db

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = db.get_user_by_username(username)
    if user and user[3] == password:
        return user
    else:
        print("Invalid credentials.")
        return False

#  ==============  user for signup  ================

def signup():
    user_id= input("Enter user ID: ")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")  
    role = input("Enter role (admin/editor/contributor/subscriber): ").lower()
    db.insert_user(user_id, username,email, password, role)
    print("User created successfully.")

# ============== display the main menu  =============
def display_menu(role):
    print("Welcome")
    print("1. View Profile")
    
    if role == "admin":
        print("2. Manage Users")      
    elif role == "editor":
        print("2. Manage Pages")
        print("3. Manage Posts")
        print("4. Manage Media")
    elif role == "contributor":
        print("2. Create Pages")
        print("3. Create Posts")
        print("4. Create Media")
        print("5. Create Tags")
        print("6. Create Categories")
    elif role == "subscriber":
        print("2. View Pages")
        print("3. View Posts")
        print("4. View Media")
        print("5. View Tags")
        print("6. View Categories")
    print("0. Logout")


# ================= display user profile ==========

def display_profile(user):
    print("User Profile")
    print("============")
    print("User ID:", user[0])
    print("Username:", user[1])
    print("Email:", user[2])
    print("Password: ", user[3])
    print("Role:", user[4])
    

# ============  manage users  (admin)   ================
def manage_users():
    users = db.get_users()
    
    for user in users:
        print(user)
    user_id = input("Enter the ID of the user to update/delete (0 to cancel): ")
    if user_id == "0":
        return
    user = db.get_user_by_id(user_id)
    if user:

        print("1. Update User")
        print("2. Delete User")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            column = input("Enter the name of the column to update: ")
            new_value = input("Enter the new value: ")
            db.update_user(user_id, column, new_value)
            print("User updated successfully.")
        elif choice == "2":
            confirm = input("Are you sure you want to delete this user? (y/n): ")
            if confirm.lower() == "y":
                db.delete_user(user_id)
                print("User deleted successfully.")
            else:
                print("cancelled.")
        else:
            print("Invalid choice.")
    else:
        print("User not found.")

#   ===================== manage pages (editor)     ===================
def manage_pages():
    pages = db.get_pages()
    
    for page in pages:
        print(page)

    page_id = input("Enter the ID of the page to update/delete (0 to cancel): ")
    if page_id == "0":
        return
    
    print("1. Update Page")
    print("2. Delete Page")
    print("0. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        column = input("Enter the name of the column to update: ")
        new_value = input("Enter the new value: ")
        db.update_page(page_id, column, new_value)
        print("Page updated successfully.")
    elif choice == "2":
        confirm = input("Are you sure you want to delete this page? (y/n): ")
        if confirm.lower() == "y":
            db.delete_page(page_id)
            print("Page deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Invalid choice.")


# ================  manage posts (editor)   ========================

def manage_posts():
    posts = db.get_posts()
    
    for post in posts:
        print(post)
    post_id = input("Enter the ID of the post to update/delete (0 to cancel): ")
    if post_id == "0":
        return
    print("1. Update Post")
    print("2. Delete Post")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        column = input("Enter the name of the column to update: ")
        new_value = input("Enter the new value: ")
        db.update_post(post_id, column, new_value)
        print("Post updated successfully.")
    elif choice == "2":
        confirm = input("Are you sure you want to delete this post? (y/n): ")
        if confirm.lower() == "y":
            db.delete_post(post_id)
            print("Post deleted.")
        else:
            print("Cancelled.")
            
    else:
        print("Invalid choice.")

# ===========   manage media (editor)   ============================
def manage_media():
    media = db.get_media()
    
    for m in media:
        print(m)
        
    media_id = input("Enter the ID of the media to update/delete (0 to cancel): ")
    if media_id == "0":
        return
    
    choice = input("Enter your choice: ")
    if choice == "1":
        column = input("Enter the name of the column to update: ")
        new_value = input("Enter the new value: ")
        db.update_media(media_id, column, new_value)
        print("Media updated successfully.")
    elif choice == "2":
        confirm = input("Are you sure you want to delete this media? (y/n): ")
        if confirm.lower() == "y":
            db.delete_media(media_id)
            print("Media deleted.")
        else:
            print("Cancelled.")
    else:
        print("Invalid choice.")

# =============================  create pages (contributor)   ==============
def create_pages():
    page_id= input("Enter page ID: ")
    title = input("Enter page title: ")
    url = input("Enter page URL: ")
    user_id = input("Enter user ID: ")
    db.insert_page(page_id, title, url, user_id)
    print("Page created successfully.")

# ===============   create posts (contributor)  =====================
def create_posts():
    post_id= input("Enter post ID: ")
    title = input("Enter post title: ")
    user_id = input("Enter user ID: ")
    db.insert_post(post_id, title, user_id)
    print("Post created successfully.")

# =====================  create media (contributor)  =====================
def create_media():
    media_id= input("Enter media ID: ")
    filename = input("Enter filename: ")
    filetype = input("Enter filetype: ")
    filesize = input("Enter filesize: ")
    user_id = input("Enter user ID: ")
    db.insert_media(media_id, filename, filetype, filesize, user_id)
    print("Media created successfully.")

# ============================  create tags (contributor)   =========================
def create_tags():
    tag_id= input("Enter tag ID: ")
    tag_name = input("Enter tag name: ")
    tag_description = input("Enter tag description: ")
    page_id = input("Enter page ID: ")
    post_id = input("Enter post ID: ")
    db.insert_tag(tag_id, tag_name, tag_description, page_id, post_id)
    print("Tag created successfully.")

# ================================  create categories (contributor) =============================
def create_categories():
    category_id= input("Enter category ID: ")
    category_name = input("Enter category name: ")
    category_description = input("Enter category description: ")
    page_id = input("Enter page ID: ")
    post_id = input("Enter post ID: ")
    db.insert_category(category_id, category_name, category_description, page_id, post_id)
    print("Category created successfully.")

# ========================= view pages (subscriber) ===============================
def view_pages():
    pages = db.get_pages()
    
    for page in pages:
        print(page)


# ==========================    view posts (subscriber)     ======================
def view_posts():
    posts = db.get_posts()
   
    for post in posts:
        print(post)


# =========================     view media (subscriber)     =======================
def view_media():
    media = db.get_media()
    
    for m in media:
        print(m)


# ============================  view tags (subscriber)  ===============================
def view_tags():
    tags = db.get_tags()
    
    for tag in tags:
        print(tag)


# ===========================       view categories (subscriber)    ==========================
def view_categories():
    categories = db.get_categories()
   
    for category in categories:
        print(category)


# Main 
def main():
    print("Welcome")
    
    user = False
    
    while not user:
        print("1. Login")
        print("2. Signup")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user = login()
        elif choice == "2":
            signup()
        elif choice == "0":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.")
    while True:
        
        display_profile(user)
        
        display_menu(user[4])
        
        choice = input("Enter your choice: ")
        if choice == "0":
            print("Logging out...")
            break
        elif choice == "1":
            display_profile(user)
        elif choice == "2":
            if user[4] == "admin":
                manage_users()
            elif user[4] == "editor":
                manage_pages()
            elif user[4] == "contributor":
                create_pages()
            elif user[4] == "subscriber":
                view_pages()
        elif choice == "3":
            if user[4] == "editor":
                manage_posts()
            elif user[4] == "contributor":
                create_posts()
            elif user[4] == "subscriber":
                view_posts()
        elif choice == "4":
            if user[4] == "editor":
                manage_media()
            elif user[4] == "contributor":
                create_media()
            elif user[4] == "subscriber":
                view_media()
        elif choice == "5":
            if user[4] == "contributor":
                create_tags()
            elif user[4] == "subscriber":
                view_tags()
        elif choice == "6":
            if user[4] == "contributor":
                create_categories()
            elif user[4] == "subscriber":
                view_categories()
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()
