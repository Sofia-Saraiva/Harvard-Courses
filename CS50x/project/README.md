# Telegrama

#### Description:
A mail web-app that allows you to exchange messages to your colleagues, friends and family!

# How it works
    Sign up to Telegrama inputting a mail address, password and confirming its password. Then log in. You can send mails to other user of the website, inputting a subject and the body of the message.
    The website allows you to check your inbox (all mails received) and all mails you sent in the past. You can also reply to any mail you received easily, the recipient and subject is automatically shown there. It also allows you to change your password.




# static folder:
    - message.png: brand of the website (credits to: https://www.flaticon.com/free-icon/message_4144781#).
    - style.css: css used in the layout.

# templates folder:
    - layout.html: layout used in all pages.
    - login.html: input for the username and the password for the user to log in.
    - register.html: an input for an unique username, a password and the its confirmation to create an account.
    - inbox.html: it shows all mails received.
    - change.html: an input for a new password and the confirmation of it. it updates on the sql database.
    - send.html: it requires a recipient, subject and body of message to send a mail.
    - reply.html: it replies to a mail (same form method of send).it automatically puts the recipient and subject.
    - mail.html: it shows full view of mail received.
    - sent.html: it shows every mail sent.

# helpers.py:
    - function to require login.

# app.py:
    - /register: requires username, password and password confirmation input for user's record. each username should be unique. its inserted to user's sql table.
    - /login: requires username and password for user to log in, it queries user's sql table.
    - /logout: logs user out of their account;
    - /change: it changes user's password, asking for a input of a new password and the confirmation of it.
    - /inbox: it queries every mail received of the user logged in.
    - /send: it requires a recipient, subject and body to send a mail. it inserts the mail, sender, recipient, subject and body into mails table.
    - /reply: it replies to a mail. uses the same form method of "send".
    - /mail: it gives a full view of any mail received clicking the button "view mail" on inbox page, it queries database.
    - /sent: it queries every mail sent by user logged in.

# mail.db: SQL Database.
    Tables:
        - users: stores data of all users, including their cash, mail address and password.
        - mail: stores: id (autoincremented), sender, recipient, subject, body, timestamp.

# requirements.txt
# flask_session
