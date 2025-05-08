from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("📇 Contact Book")
root.geometry("400x400")

contacts = {}

add_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/add.png").resize((25, 25)))
view_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/view.png").resize((25, 25)))
update_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/update.png").resize((25, 25)))
delete_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/delete.png").resize((25, 25)))
exit_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/exit.png").resize((25, 25)))
contact_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/contact.png").resize((40, 40)))

button_frame = Frame(root)
button_frame.pack(pady=0)

Label(root, image=contact_icon).pack(pady=10)
Label(root, text="Contact Book", font=("Helvetica", 10, "bold")).pack()

Button(button_frame, text=" Add Contact",bg="White", fg="Black", activebackground="Green", activeforeground="White", image=add_icon, compound=LEFT, width=500, command=lambda: show_add_contact()).pack(pady=5)
Button(button_frame, text=" View Contacts", bg="White", fg="Black", activebackground="Green", activeforeground="White", image=view_icon, compound=LEFT, width=500, command=lambda: show_contacts()).pack(pady=5)
Button(button_frame, text=" Update Contact", bg="White", fg="Black", activebackground="Green", activeforeground="White", image=update_icon, compound=LEFT, width=500, command=lambda: show_update_contact()).pack(pady=5)
Button(button_frame, text=" Delete Contact", bg="White", fg="Black", activebackground="Green", activeforeground="White", image=delete_icon, compound=LEFT, width=500, command=lambda: show_delete_contact()).pack(pady=5)
Button(button_frame, text=" Exit", bg="White", fg="Black", activebackground="Green", activeforeground="White", image=exit_icon, compound=LEFT, width=500, command=root.destroy).pack(pady=5)

display_frame = Frame(root)
display_frame.pack(pady=10)

def show_add_contact():
    for widget in display_frame.winfo_children():
        widget.destroy()
    name_label = Label(display_frame, text="Name:")
    name_label.pack(pady=5)
    name_entry = Entry(display_frame, width=30)
    name_entry.pack(pady=5)
    phone_label = Label(display_frame, text="Phone:")
    phone_label.pack(pady=5)
    phone_entry = Entry(display_frame, width=30)
    phone_entry.pack(pady=5)
    email_label = Label(display_frame, text="Email:")
    email_label.pack(pady=5)
    email_entry = Entry(display_frame, width=30)
    email_entry.pack(pady=5)
    address_label = Label(display_frame, text="Address:")
    address_label.pack(pady=5)
    address_entry = Entry(display_frame, width=30)
    address_entry.pack(pady=5)
    submit_button = Button(display_frame, text="Submit", command=lambda: submit_contact(name_entry, phone_entry, email_entry, address_entry))
    submit_button.pack(pady=10)

def submit_contact(name_entry, phone_entry, email_entry, address_entry):
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone and email and address:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
        show_message(f"Contact {name} added successfully!", "green")

def show_contacts():
    for widget in display_frame.winfo_children():
        widget.destroy()
    contact_listbox = Listbox(display_frame, width=50, height=10)
    contact_listbox.pack(pady=10)
    for name, details in contacts.items():
        contact_listbox.insert(END, f"Name: {name} | Phone: {details['phone']} | Email: {details['email']} | Address: {details['address']}")
    show_message("Contacts displayed", "blue")

def show_update_contact():
    for widget in display_frame.winfo_children():
        widget.destroy()
    name_label = Label(display_frame, text="Enter Name to Update:")
    name_label.pack(pady=2)
    name_entry = Entry(display_frame, width=30)
    name_entry.pack(pady=5)
    search_button = Button(display_frame, text="Search", command=lambda: search_and_show_update(name_entry))
    search_button.pack(pady=5)

def search_and_show_update(name_entry):
    name = name_entry.get()
    if name in contacts:
        contact = contacts[name]
        for widget in display_frame.winfo_children():
            widget.destroy()
        phone_label = Label(display_frame, text="Phone:")
        phone_label.pack(pady=2)
        phone_entry = Entry(display_frame, width=30)
        phone_entry.insert(0, contact['phone'])
        phone_entry.pack(pady=5)
        email_label = Label(display_frame, text="Email:")
        email_label.pack(pady=2)
        email_entry = Entry(display_frame, width=30)
        email_entry.insert(0, contact['email'])
        email_entry.pack(pady=5)
        address_label = Label(display_frame, text="Address:")
        address_label.pack(pady=2)
        address_entry = Entry(display_frame, width=30)
        address_entry.insert(0, contact['address'])
        address_entry.pack(pady=5)
        update_button = Button(display_frame, text="Update", command=lambda: update_contact(name, phone_entry, email_entry, address_entry))
        update_button.pack(pady=10)
    else:
        show_message("Contact not found!", "red")

def update_contact(name, phone_entry, email_entry, address_entry):
    contacts[name] = {
        'phone': phone_entry.get(),
        'email': email_entry.get(),
        'address': address_entry.get()
    }
    show_message(f"Contact {name} updated successfully!", "green")

def show_delete_contact():
    for widget in display_frame.winfo_children():
        widget.destroy()
    name_label = Label(display_frame, text="Enter Name to Delete:")
    name_label.pack(pady=2)
    name_entry = Entry(display_frame, width=30)
    name_entry.pack(pady=5)
    delete_button = Button(display_frame, text="Delete", command=lambda: delete_contact(name_entry))
    delete_button.pack(pady=10)

def delete_contact(name_entry):
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        show_message(f"Contact {name} deleted successfully!", "red")
    else:
        show_message("Contact not found!", "red")

def show_message(message, color):
    message_label = Label(display_frame, text=message, fg=color)
    message_label.pack(pady=10)

root.mainloop()
