import time
import smtplib
from email.mime.text import MIMEText

import keyring
from selenium.webdriver.common.by import By
from selenium import webdriver


class Parsing:
    def __init__(self, email, password):
        self.driver = None
        self.email = email
        self.password = password
        self.options = webdriver.ChromeOptions()

    def login(self):
        self.driver = webdriver.Chrome(options=self.options)
        email = self.email
        password = self.password
        self.driver.get("https://classroom.btu.edu.ge/ge/login")
        time.sleep(0.5)
        self.driver.find_element(by=By.CLASS_NAME, value="btn").click()
        time.sleep(0.5)
        self.driver.find_element(by=By.NAME, value="identifier").send_keys(email)
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH, value='//*[@id="identifierNext"]/div/button/span'
        ).click()
        time.sleep(4.2)
        self.driver.find_element(
            By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input'
        ).send_keys(password)
        time.sleep(0.2)
        self.driver.find_element(
            By.XPATH, value='//*[@id="passwordNext"]/div/button/span'
        ).click()
        time.sleep(3)

    def messages(self):
        self.driver.get("https://classroom.btu.edu.ge/ge/messages/index/0/9999/40")
        time.sleep(5)
        return self.driver.find_elements(By.CLASS_NAME, value="info")

    def select_message(self, all_messages):
        messages_list = []
        index = 0
        for message in all_messages:
            title = message.text
            href = message.find_element(By.TAG_NAME, "a")
            href.click()
            time.sleep(2)
            text = self.driver.find_element(By.ID, value="message_body").text
            messages_list.append({"title": title, "text": text})
            index += 1
            self.driver.back()
            time.sleep(1)
        return messages_list

    @staticmethod
    def send_email(message_list):
        sender = "btumessages@gmail.com"
        password = keyring.get_password()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        for message in message_list:
            subject = message["title"]
            text = message["text"]
            try:
                msg = MIMEText(text)
                msg["subject"] = subject
                server.login(sender, password)
                server.sendmail(
                    sender, "roberti.dovlatbegiani.1@btu.edu.ge", msg.as_string()
                )
                return "The message was sent successfully!"
            except Exception as _ex:
                return f"{_ex}\nCheck your login or password please!"
