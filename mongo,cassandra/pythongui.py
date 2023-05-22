# from tkinter import *
# from cassandra.cluster import Cluster

# # Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])
# session = cluster.connect('demo2')

# # Define the GUI
# root = Tk()
# root.title("Cassandra GUI")
# root.geometry("400x200")

# # Define the functions for CRUD operations
# def create():
#     name = name_entry.get()
#     email = email_entry.get()
#     id = id_entry.get()
# session.execute("INSERT INTO demo2.users (id,email,name) VALUES (%s, %s,%s)", (id,email,name))

# def read():
#     result = session.execute("SELECT * FROM demo2.users")
#     for row in result:
#         print(row.name, row.email)

# def update():
#     name = name_entry.get()
#     email = email_entry.get()
#     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

# def delete():
#     name = name_entry.get()
#     session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# # Define the labels and input fields
# name_label = Label(root, text="Name:")
# name_label.grid(row=0, column=0)
# name_entry = Entry(root)
# name_entry.grid(row=0, column=1)

# email_label = Label(root, text="Email:")
# email_label.grid(row=1, column=0)
# email_entry = Entry(root)
# email_entry.grid(row=1, column=1)

# id_label = Label(root, text="Email:")
# id_label.grid(row=1, column=0)
# id_entry = Entry(root)
# id_entry.grid(row=1, column=1)

# # Define the buttons for CRUD operations
# create_button = Button(root, text="Create", command=create)
# create_button.grid(row=2, column=0)

# read_button = Button(root, text="Read", command=read)
# read_button.grid(row=2, column=1)

# update_button = Button(root, text="Update", command=update)
# update_button.grid(row=3, column=0)

# delete_button = Button(root, text="Delete", command=delete)
# delete_button.grid(row=3, column=1)

# # Run the GUI
# root.mainloop()









# from tkinter import *
# from cassandra.cluster import Cluster

# # Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])
# session = cluster.connect('demo2')

# # Define the GUI
# root = Tk()
# root.title("Cassandra GUI")
# root.geometry("400x200")

# # Define the functions for CRUD operations
# def create():
#     name = name_entry.get()
#     email = email_entry.get()
#     id = id_entry.get()
#     session.execute("INSERT INTO demo2.users (id, email, name) VALUES (%s, %s, %s)", (id, email, name))

# def read():
#     result = session.execute("SELECT * FROM demo2.users")
#     for row in result:
#         print(row.name, row.email)

# def update():
#     name = name_entry.get()
#     email = email_entry.get()
#     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

# def delete():
#     name = name_entry.get()
#     session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# # Define the labels and input fields
# name_label = Label(root, text="Name:")
# name_label.grid(row=0, column=0)
# name_entry = Entry(root)
# name_entry.grid(row=0, column=1)

# email_label = Label(root, text="Email:")
# email_label.grid(row=1, column=0)
# email_entry = Entry(root)
# email_entry.grid(row=1, column=1)

# id_label = Label(root, text="ID:")
# id_label.grid(row=2, column=0)
# id_entry = Entry(root)
# id_entry.grid(row=2, column=1)

# # Define the buttons for CRUD operations
# create_button = Button(root, text="Create", command=create)
# create_button.grid(row=3, column=0)

# read_button = Button(root, text="Read", command=read)
# read_button.grid(row=3, column=1)

# update_button = Button(root, text="Update", command=update)
# update_button.grid(row=4, column=0)

# delete_button = Button(root, text="Delete", command=delete)
# delete_button.grid(row=4, column=1)

# # Run the GUI
# root.mainloop()











# from tkinter import *
# from cassandra.cluster import Cluster

# # Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])
# session = cluster.connect('demo2')

# # Define the GUI
# root = Tk()
# root.title("Cassandra GUI")
# root.geometry("800x200")

# # Define the functions for CRUD operations
# def create():
#     name = name_entry.get()
#     email = email_entry.get()
#     id = int(id_entry.get())
#     session.execute("INSERT INTO demo2.users (id, email, name) VALUES (%s, %s, %s)", (id, email, name))

# def read():
#     result = session.execute("SELECT * FROM demo2.users")
#     for row in result:
#         print(row.name, row.email)

# def update():
#     name = name_entry.get()
#     email = email_entry.get()
#     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

# def delete():
#     name = name_entry.get()
#     session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# # Define the labels and input fields
# name_label = Label(root, text="Name:")
# name_label.grid(row=0, column=0)
# name_entry = Entry(root)
# name_entry.grid(row=0, column=1)

# email_label = Label(root, text="Email:")
# email_label.grid(row=1, column=0)
# email_entry = Entry(root)
# email_entry.grid(row=1, column=1)

# id_label = Label(root, text="ID:")
# id_label.grid(row=2, column=0)
# id_entry = Entry(root)
# id_entry.grid(row=2, column=1)

# # Define the buttons for CRUD operations
# create_button = Button(root, text="Create", command=create)
# create_button.grid(row=3, column=0)

# read_button = Button(root, text="Read", command=read)
# read_button.grid(row=3, column=1)

# update_button = Button(root, text="Update", command=update)
# update_button.grid(row=4, column=0)

# delete_button = Button(root, text="Delete", command=delete)
# delete_button.grid(row=4, column=1)

# # Run the GUI
# root.mainloop()

# ***************************
# from tkinter import *
# from cassandra.cluster import Cluster

# # Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])
# session = cluster.connect('demo2')

# # Define the GUI
# root = Tk()
# root.title("Cassandra GUI")
# root.geometry("800x400")

# # Set background color
# root.configure(background='#f0f0f0')

# # Define the functions for CRUD operations
# def create():
#     name = name_entry.get()
#     email = email_entry.get()
#     id = id_entry.get()
#     session.execute("INSERT INTO demo2.users (id,email,name) VALUES (%s, %s,%s)", (int(id), email, name))

# def read():
#     result = session.execute("SELECT * FROM demo2.users")
#     for row in result:
#         print(row.name, row.email)

# def update():
#     name = name_entry.get()
#     email = email_entry.get()
#     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

# def delete():
#     name = name_entry.get()
#     session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# # Define the labels and input fields
# name_label = Label(root, text="Name:", background='#f0f0f0')
# name_label.grid(row=0, column=0, padx=10, pady=10)
# name_entry = Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=10)

# email_label = Label(root, text="Email:", background='#f0f0f0')
# email_label.grid(row=1, column=0, padx=10, pady=10)
# email_entry = Entry(root)
# email_entry.grid(row=1, column=1, padx=10, pady=10)

# id_label = Label(root, text="ID:", background='#f0f0f0')
# id_label.grid(row=2, column=0, padx=10, pady=10)
# id_entry = Entry(root)
# id_entry.grid(row=2, column=1, padx=10, pady=10)

# # Define the buttons for CRUD operations
# create_button = Button(root, text="Create", command=create, background='#008000', fg='white')
# create_button.grid(row=3, column=0, padx=10, pady=10)

# read_button = Button(root, text="Read", command=read, background='#0000FF', fg='white')
# read_button.grid(row=3, column=1, padx=10, pady=10)

# update_button = Button(root, text="Update", command=update, background='#FFA500')
# update_button.grid(row=4, column=0, padx=10, pady=10)

# delete_button = Button(root, text="Delete", command=delete, background='#FF0000', fg='white')
# delete_button.grid(row=4, column=1, padx=10, pady=10)

# # Run the GUI
# root.mainloop()






from tkinter import *
from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['localhost'])
session = cluster.connect('demo2')

# Define the GUI
root = Tk()
root.title("Cassandra GUI")
root.geometry("800x400")

# Set background color
root.configure(background='#f0f0f0')

# Define the functions for CRUD operations
def create():
    name = name_entry.get()
    email = email_entry.get()
    id = id_entry.get()
    session.execute("INSERT INTO demo2.users (id,email,name) VALUES (%s, %s,%s)", (int(id), email, name))

def read():
    result = session.execute("SELECT * FROM demo2.users")
    for row in result:
        print(row.name, row.email)

def update():
    name = name_entry.get()
    email = email_entry.get()
    session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

def delete():
    name = name_entry.get()
    session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# Define the labels and input fields
name_label = Label(root, text="Name:", background='#f0f0f0', font=("Arial", 14))
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = Label(root, text="Email:", background='#f0f0f0', font=("Arial", 14))
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = Entry(root, font=("Arial", 14))
email_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = Label(root, text="ID:", background='#f0f0f0', font=("Arial", 14))
id_label.grid(row=2, column=0, padx=10, pady=10)
id_entry = Entry(root, font=("Arial", 14))
id_entry.grid(row=2, column=1, padx=10, pady=10)

# Define the buttons for CRUD operations
create_button = Button(root, text="Create", command=create, background='#008000', fg='white', font=("Arial", 14))
create_button.grid(row=3, column=0, padx=10, pady=10)

read_button = Button(root, text="Read", command=read, background='#0000FF', fg='white', font=("Arial", 14))
read_button.grid(row=3, column=1, padx=10, pady=10)

update_button = Button(root, text="Update", command=update, background='#FFA500', font=("Arial", 14))
update_button.grid(row=4, column=0, padx=10, pady=10)

delete_button = Button(root, text="Delete", command=delete, background='#FF0000', fg='white', font=("Arial", 14))
delete_button.grid(row=4, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()
































































































































































# from tkinter import *
# from cassandra.cluster import Cluster

# # Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])
# session = cluster.connect('demo2')

# # Define the GUI
# root = Tk()
# root.title("Cassandra GUI")
# root.geometry("400x200")

# # Define the functions for CRUD operations
# def create():
#     name = name_entry.get()
#     email = email_entry.get()
#     id = int(id_entry.get())
#     session.execute("INSERT INTO demo2.users (id, email, name) VALUES (%s, %s, %s)", (id, email, name))

# def read():
#     result = session.execute("SELECT * FROM demo2.users")
#     for row in result:
#         print(row.name, row.email)

# # def update():
# #     name = name_entry.get()
# #     old_email = email_entry.get()
# #     new_email = new_email_entry.get()
# #     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s and email = %s ALLOW FILTERING", (new_email, name, old_email))

# def update():
#     name = name_entry.get()
#     old_email = new_email_entry.get()
#     new_email = new_email_entry.get()
#     session.execute("UPDATE demo2.users SET email = %s WHERE name = %s and email = %s", (new_email, name, old_email))


# def delete():
#     name = name_entry.get()
#     email = email_entry.get()
#     session.execute("DELETE FROM demo2.users WHERE name = %s and email = %s", [name, email])

# # Define the labels and input fields
# name_label = Label(root, text="Name:")
# name_label.grid(row=0, column=0)
# name_entry = Entry(root)
# name_entry.grid(row=0, column=1)

# email_label = Label(root, text="Email:")
# email_label.grid(row=1, column=0)
# email_entry = Entry(root)
# email_entry.grid(row=1, column=1)

# new_email_label = Label(root, text="New Email:")
# new_email_label.grid(row=2, column=0)
# new_email_entry = Entry(root)
# new_email_entry.grid(row=2, column=1)

# id_label = Label(root, text="ID:")
# id_label.grid(row=3, column=0)
# id_entry = Entry(root)
# id_entry.grid(row=3, column=1)

# # Define the buttons for CRUD operations
# create_button = Button(root, text="Create", command=create)
# create_button.grid(row=4, column=0)

# read_button = Button(root, text="Read", command=read)
# read_button.grid(row=4, column=1)

# update_button = Button(root, text="Update", command=update)
# update_button.grid(row=5, column=0)

# delete_button = Button(root, text="Delete", command=delete)
# delete_button.grid(row=5, column=1)

# # Run the GUI
# root.mainloop()
