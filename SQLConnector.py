
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cms2b_db"
)

cursor = conn.cursor()

# =========================== insert a new user  ================

def insert_user(userID, username, email, password, role):
    query = "INSERT INTO users (userID, username, email, password, role) VALUES (%s,%s, %s, %s, %s)"
    values = (userID, username,email , password, role)
    cursor.execute(query, values)
    conn.commit()


# =========================== get a user by user id =====================
def get_user_by_id(userID):
    query = "SELECT * FROM users WHERE userID = %s"
    values = (userID,)
    cursor.execute(query, values)
    return cursor.fetchone()


# =========================== get a user by username    ================
def get_user_by_username(username):
    query = "SELECT * FROM users WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)
    return cursor.fetchone()

# =========================== get all users from the database   ========================
def get_users():
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update a user in the database ============================
def update_user(userID, column, new_value):
    query = f"UPDATE users SET {column} = %s WHERE userID = %s"
    values = (new_value, userID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete a user from the database   ==================================
def delete_user(userID):
    query = "DELETE FROM users WHERE userID = %s"
    values = (userID,)
    cursor.execute(query, values)
    conn.commit()

# =========================== insert a new post into the database   =====================
def insert_post(postID, title, userID):
    query = "INSERT INTO posts (postID, title, userID) VALUES (%s, %s, %s)"
    values = (postID, title, userID)
    cursor.execute(query, values)
    conn.commit()

# =========================== get all posts from the database   ==========================
def get_posts():
    query = "SELECT * FROM Posts"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update a post in the database ==================================
def update_post(postID, column, new_value):
    query = f"UPDATE posts SET {column} = %s WHERE postID = %s"
    values = (new_value, postID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete a post from the database   ==================================
def delete_post(postID):
    query = "DELETE FROM posts WHERE postID = %s"
    values = (postID,)
    cursor.execute(query, values)
    conn.commit()

# ===========================   insert a new page into the database   ======================
def insert_page(pageID, title, url, userID):
    query = "INSERT INTO pages (pageID, title, url, userID) VALUES (%s, %s, %s, %s)"
    values = (pageID, title, url, userID)
    cursor.execute(query, values)
    conn.commit()

# =========================== get all pages from the database   ================================
def get_pages():
    query = "SELECT * FROM pages"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update a page in the database     ============================
def update_page(pageID, column, new_value):
    query = f"UPDATE pages SET {column} = %s WHERE pageID = %s"
    values = (new_value, pageID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete a page from the database   =============================
def delete_page(pageID):
    query = "DELETE FROM pages WHERE pageID = %s"
    values = (pageID,)
    cursor.execute(query, values)
    conn.commit()

# =========================== insert a new media into the database  ==================================
def insert_media(mediaID, filename, filetype, filesize, userID):
    query = "INSERT INTO media (mediaID, filename, filetype, filesize, userID) VALUES (%s, %s, %s, %s, %s)"
    values = (mediaID, filename, filetype, filesize, userID)
    cursor.execute(query, values)
    conn.commit()

# =========================== get all media from the database   ================================
def get_media():
    query = "SELECT * FROM media"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update media in the database  =========================================
def update_media(mediaID, column, new_value):
    query = f"UPDATE media SET {column} = %s WHERE mediaID = %s"
    values = (new_value, mediaID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete media from the database    ======================================
def delete_media(mediaID):
    query = "DELETE FROM media WHERE mediaID = %s"
    values = (mediaID,)
    cursor.execute(query, values)
    conn.commit()

# =========================== insert a new category into the database   ===================

def insert_category(categoryID, category_name, category_description, pageID, postID):
    query = "INSERT INTO categories (categoryID, cat_name, cat_desc, pageID, postID) VALUES (%s, %s, %s, %s, %s)"
    values = (categoryID, category_name, category_description, pageID, postID)
    cursor.execute(query, values)
    conn.commit()

# =========================== get all categories from the database  ========================================
def get_categories():
    query = "SELECT * FROM categories"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update a category in the database =================================
def update_category(categoryID, column, new_value):
    query = f"UPDATE categories SET {column} = %s WHERE categoryID = %s"
    values = (new_value, categoryID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete a category from the database   ===================================
def delete_category(categoryID):
    query = "DELETE FROM categories WHERE categoryID = %s"
    values = (categoryID,)
    cursor.execute(query, values)
    conn.commit()

# =========================== insert a new tag into the database    ===========================================
def insert_tag(tagID, tag_name, tag_description, pageID, postID):
    query = "INSERT INTO tags (tagID, tag_name, tag_desc, pageID, postID) VALUES (%s, %s, %s, %s, %s)"
    values = (tagID, tag_name, tag_description, pageID, postID)
    cursor.execute(query, values)
    conn.commit()

# =========================== get all tags from the database    =================================
def get_tags():
    query = "SELECT * FROM tags"
    cursor.execute(query)
    return cursor.fetchall()

# =========================== update a tag in the database  ==============================
def update_tag(tagID, column, new_value):
    query = f"UPDATE tags SET {column} = %s WHERE tagID = %s"
    values = (new_value, tagID)
    cursor.execute(query, values)
    conn.commit()

# =========================== delete a tag from the database    ===============================================
def delete_tag(tagID):
    query = "DELETE FROM tags WHERE tagID = %s"
    values = (tagID,)
    cursor.execute(query, values)
    conn.commit()


 
