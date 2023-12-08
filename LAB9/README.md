# Task 9: Mail client using SMTP and FTP.

Hi everyone, welcome to the 9th laboratory on Network Programming. In this Laboratory you are going to implement a mail client using the FTP and SMTP client.

## Task description.

You should create an application that will take as an input the following inputs:
1. Mail recipient address.
2. Subject of the e-mail.
3. Body of the email.
4. The file attached.

and should send this email to the recipient. Howether there are some tricks:
1. Instead of attaching the file tp the mail you firstly should save the file on the FTP server provided to you by Mr. Alexei Panin and add the url to this file at the end of the mail's body.
2. The application should be able to send multiple mails, meaning that it will not stop after sending an email, and the sendong of another email will be possible.
3. The GUI is not mandatory.

The lab will be tested if a mail send by your app will get to the e-mail address prvided by me.

If you impliment a GUI you get 2 points.
If you only create a CLI you will get 1.5.

You cannot get only 0.5 points by only presenting the GUI.