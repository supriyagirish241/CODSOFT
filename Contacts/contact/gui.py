from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("📇 Contact Book")
root.geometry("400x400")

# Load icons from 'Contacts/contact/' folder
add_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/add.png").resize((25, 25)))
view_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/view.png").resize((25, 25)))
update_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/update.png").resize((25, 25)))
delete_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/delete.png").resize((25, 25)))
exit_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/exit.png").resize((25, 25)))
contact_icon = ImageTk.PhotoImage(Image.open("Contacts/contact/contact.png").resize((40, 40)))

# Show app title with contact icon
Label(root, image=contact_icon).pack(pady=10)
Label(root, text="Contact Book", font=("Helvetica", 16, "bold")).pack()

# Add buttons with icons
Button(root, text=" Add Contact", image=add_icon, compound=LEFT, width=200).pack(pady=5)
Button(root, text=" View Contacts", image=view_icon, compound=LEFT, width=200).pack(pady=5)
Button(root, text=" Update Contact", image=update_icon, compound=LEFT, width=200).pack(pady=5)
Button(root, text=" Delete Contact", image=delete_icon, compound=LEFT, width=200).pack(pady=5)
Button(root, text=" Exit", image=exit_icon, compound=LEFT, width=200, command=root.quit).pack(pady=5)

root.mainloop()
