import os, sys, smtplib, getpass, time
from simple_term_menu import TerminalMenu

W = '\033[0m'  #White
R = '\033[31m' #Red
G = '\033[32m' #Green
Y = '\033[93m' #Yellow
Servers = ["Google", "Yahoo", "Quit"]

def main():
    os.system("clear")
    main_menu_title = "  Welcome to Email Spammer Menu\n"
    main_menu_items = Servers
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    edit_menu_title = "  Authentication\n"
    edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)
    Spammer(main_menu, edit_menu)

class Spammer():
    def __init__(self, main_menu, edit_menu):
        main_menu_exit = False
        # edit_menu_back = False
        while not main_menu_exit:
            main_sel = main_menu.show()

            if main_sel == 0:
                self.smtp_server = 'smtp.gmail.com'
                self.port = 587
                self.set_server = "gmail"
                self.auth()
                main_menu_exit = True
                self.exit()
            elif main_sel == 1:
                self.smtp_server = 'smtp.mail.yahoo.com'
                self.port = 25
                self.set_server = "yahoo"
                self.auth()
                main_menu_exit = True
                self.exit()
            elif main_sel == 2:
                main_menu_exit = True
                self.exit()
      
    def exit(self):
        print("Thank you for using Email Spammer")

    def auth(self):
        # For prod
        self.email_user = input('Email: ')
        if self.set_server == "gmail":
            print(Y + "\nYou have to use a mobile application password\n" + W)
        self.passwd = getpass.getpass('Password: ')
        self.email_to = input('\nTo: ')
        self.subject = input('Subject: ')
        self.body = input('Message: ')
        self.total = int(input('Amount of Sendings: '))

        self.send()
    
    def send(self): 
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)

            server.ehlo()

            if self.set_server == "gmail":
                server.starttls()
                server.ehlo()

            server.login(self.email_user, self.passwd)

            print("\n\n\n - Target : {} -\n".format(self.email_to))

            for i in range(1, self.total+1):

                msg = 'From: ' + self.email_user + '\nSubject: ' + self.subject + '\n' + self.body

                server.sendmail(self.email_user, self.email_to, msg)

                print(G + "\rEmail Sent - {}".format(i))

                sys.stdout.flush()

            server.close()
            print( R + "\n\n-Proccess Terminated-" + W)


        except KeyboardInterrupt:

            print(R + "\nError - Keyboard Interrupt" + W)
            sys.exit()

        except smtplib.SMTPAuthenticationError:
            print( R + "\nError - Authentication error, Are you sure the password or the username is correct?" + W)
            sys.exit()

if __name__ == "__main__":
  main()
