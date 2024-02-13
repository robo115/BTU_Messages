from customtkinter import *
from PIL import Image, ImageTk
import re

side_img_data = Image.open("images/side-img.png")
email_icon_data = Image.open("images/email-icon.png")
password_icon_data = Image.open("images/password-icon.png")


class GUI:
    def __init__(self, root, email="", password=""):

        self.root = root
        self.email = email
        self.password = password
        self.root.geometry("600x480")
        self.root.resizable(False, False)
        self.root.title("  BTU Messages")
        self.logo_image = Image.open("images/logo.png")
        self.iconpath = ImageTk.PhotoImage(image=self.logo_image)
        self.root.wm_iconbitmap()

        self.root.iconphoto(False, self.iconpath)
        side_img = CTkImage(
            dark_image=side_img_data, light_image=side_img_data, size=(300, 480)
        )
        email_icon = CTkImage(
            dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20)
        )
        password_icon = CTkImage(
            dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17)
        )

        CTkLabel(master=root, text="", image=side_img).pack(expand=True, side="left")
        frame = CTkFrame(master=root, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(False)
        frame.pack(expand=True, side="right")
        self.button = 0

        self.check_var = BooleanVar()

        self.first_label = CTkLabel(
            master=frame,
            text="Welcome Back!",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 24),
        ).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        self.label = CTkLabel(
            master=frame,
            text="Sign in to your account",
            text_color="#7E7E7E",
            anchor="w",
            justify="left",
            font=("Arial Bold", 12),
        )
        self.label.pack(anchor="w", padx=(25, 0))

        CTkLabel(
            master=frame,
            text="  Email:",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            image=email_icon,
            compound="left",
        ).pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.input_mail = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#601E88",
            border_width=1,
            text_color="#000000",
        )

        self.input_mail.pack(anchor="w", padx=(25, 0))

        CTkLabel(
            master=frame,
            text="  Password:",
            text_color="#601E88",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            image=password_icon,
            compound="left",
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.input_password = CTkEntry(
            master=frame,
            width=225,
            fg_color="#EEEEEE",
            border_color="#601E88",
            border_width=1,
            text_color="#000000",
            show="*",
        )

        self.root.bind("<Return>", self.click_button)
        self.input_password.pack(anchor="w", padx=(25, 0))
        CTkButton(
            master=frame,
            text="Login",
            command=self.click_button,
            fg_color="#601E88",
            hover_color="#E44982",
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=225,
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        self.checkbox = CTkCheckBox(
            master=frame,
            text="Monitoring",
            variable=self.check_var,
            onvalue=True,
            offvalue=False,
            corner_radius=8,
            border_color="#601E88",
            fg_color="#601E88",
            hover_color="#601E88",
        )
        self.checkbox.pack(padx=10, pady=10)

        self.checkbox.place(relx=0.1, rely=0.8)

    def click_button(self, event="Return"):
        email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@btu.edu.ge+$")
        value = self.input_mail.get()
        if email_pattern.match(value) and self.input_password.get() != "":
            self.email = self.input_mail.get()
            self.password = self.input_password.get()
            self.button = 1
            self.root.destroy()
        else:
            self.label.configure(
                text="ავტორიზაციისთვის გამოიყენეთ\n BTU-ს ელ. ფოსტა და შეავსეთ პაროლის ველი",
                text_color="red",
            )


class FinishGUI:
    def __init__(self, root, email="", password=""):
        self.root = root
        self.root.geometry("500x380")
        self.root.resizable(False, False)
        self.root.title("  BTU Messages")
        self.logo_image = Image.open("images/logo.png")
        self.iconpath = ImageTk.PhotoImage(image=self.logo_image)
        self.root.wm_iconbitmap()
        self.root.iconphoto(False, self.iconpath)

        frame = CTkFrame(master=root, width=500, height=480, fg_color="#b2e4eb")
        frame.pack_propagate(False)
        frame.pack(expand=True, side="right")
        self.first_label = CTkLabel(
            master=frame,
            text="",
            text_color="#20292e",
            anchor="w",
            justify="left",
            font=("Arial Bold", 16),
        )
        self.first_label.pack(anchor="n", pady=(50, 5))

        self.button = CTkButton(
            master=frame,
            text="Close",
            fg_color="#ffffff",
            hover_color="#cc2f2f",
            font=("Arial Bold", 12),
            text_color="#000000",
            width=150,
            height=50,
            command=self.click_button,
        )

        self.button.pack(anchor="s", pady=(120, 0), padx=(25, 0))

    def click_button(self):
        self.root.destroy()
