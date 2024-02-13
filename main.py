from parsing import Parsing
from gui import GUI, FinishGUI
from customtkinter import CTk


def logining(try_again: int = 0):
    root = CTk()
    app = GUI(root)
    if try_again == 1:
        app.label.configure(
            text="შეყვანილი მეილი და პაროლი არასწორია,\n გთხოვთ თავიდან სცადოთ",
            text_color="red",
        )
    root.mainloop()
    return app.email, app.password, app.button, app.check_var.get()


def start_parsing(info: tuple):
    count_messages = None
    email = info[0]
    password = info[1]
    button = info[2]
    var = info[3]
    if button == 1 and var:
        user = Parsing(password=password, email=email)
        try:
            user.login()
            mess = user.messages()
            while not mess:
                mess = user.messages()
            mess_list = user.select_message(all_messages=mess)
            count_messages = len(mess_list)
            user.send_email(mess_list)
        except:
            count_messages = 0
    elif button == 1 and not var:
        user = Parsing(password=password, email=email)
        try:
            user.login()
            mess = user.messages()
            mess_list = user.select_message(all_messages=mess)
            count_messages = len(mess_list)
            user.send_email(mess_list)
        except:
            user.driver.close()
            log = logining(try_again=1)
            start_parsing(log)
    return count_messages


if __name__ == "__main__":
    log = logining()
    count_mess = start_parsing(log)
    root = CTk()
    sec_app = FinishGUI(root)
    if count_mess is not None:
        if count_mess > 0:
            sec_app.first_label.configure(
                text=f"თქვენს მეილზე გამოგზავნილია {count_mess} წერილი გთხოვთ შეამოწმოთ 🚀"
            )
        elif count_mess == 0:
            sec_app.first_label.configure(
                text=f"თქვენს აქაუნთზე ახალი მესიჯები ვერ მოიძებნა  🔔️"
            )
        root.mainloop()
    else:
        pass
