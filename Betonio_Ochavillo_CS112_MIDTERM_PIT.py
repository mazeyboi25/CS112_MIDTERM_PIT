from tkinter import *       # for importing the Tkinter module

root = Tk()     # Variable for initializing the Tkinter window
root.geometry("500x200")        # For setting a specified window size
root.resizable(FALSE, FALSE)        # For setting the window to be not resizable
root.title('Pixpay')        # For setting the title of the window


def intro():        # Defined function for Tkinter GUI
    label_for_intro = Label(root, text="Welcome to Pixpay!"
                                       "This shop will offer you discounted game credits of your favorite games!\n"
                                       "What game credits would you like to purchase?\n")
    label_for_intro.pack()

    def valorant_game_choice():     # Defined function for Valorant as game choice
        label_for_valorant_choice = Label(root, text="You have selected \"Valorant.\"\n"
                                                     "Select credits:\n")
        label_for_valorant_choice.pack()
        # Interactive buttons for the user to choose from
        valop1 = Button(text='150 VP (₱75)', width=25, command=lambda: (label_for_valorant_choice.pack_forget(),
                                                                        valop1.pack_forget(), valop2.pack_forget(),
                                                                        valop3.pack_forget(), valop4.pack_forget(),
                                                                        payment_valo1()))
        valop1.pack()
        valop2 = Button(text='300 VP (₱150)', width=25, command=lambda: (label_for_valorant_choice.pack_forget(),
                                                                         valop1.pack_forget(), valop2.pack_forget(),
                                                                         valop3.pack_forget(), valop4.pack_forget(),
                                                                         payment_valo2()))
        valop2.pack()
        valop3 = Button(text='600 VP (₱295)', width=25, command=lambda: (label_for_valorant_choice.pack_forget(),
                                                                         valop1.pack_forget(), valop2.pack_forget(),
                                                                         valop3.pack_forget(), valop4.pack_forget(),
                                                                         payment_valo3()))
        valop3.pack()
        valop4 = Button(text='1050 VP (₱350)', width=25, command=lambda: (label_for_valorant_choice.pack_forget(),
                                                                          valop1.pack_forget(), valop2.pack_forget(),
                                                                          valop3.pack_forget(), valop4.pack_forget(),
                                                                          payment_valo4()))
        valop4.pack()

    def payment_valo1():        # Defined function for Valorant as game choice
        def total():        # Defined function for converting Entry from string to integer
            try:        # Calculates the remaining balance of the user
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 75
                if remaining_balance >= 75:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?\n')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?\n")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_valo1(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:      # Segregates runtime error and prompting the user to input an integer.
                error_label = (Label(text='Input is not a number. Would you like to retry?\n'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_valo1(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_valo2():        # Defined function for Valorant as game choice
        def total():        # Defined function for converting Entry from string to integer
            try:       # Calculates the remaining balance of the user.
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 150
                if remaining_balance >= 150:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing1'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_valo2(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_valo2(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_valo3():
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 295
                if remaining_balance >= 295:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_valo3(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_valo3(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_valo4():
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 350
                if remaining_balance >= 350:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_valo4(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_valo1(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def codm_game_choice():         # Defined function for CODM as game choice.
        label_for_codm_choice = Label(root, text="You have selected \"CODM.\"\n"
                                                 "Select credits:")
        label_for_codm_choice.pack()
        # Interactive buttons for the user to choose from
        codop1 = Button(text='50 GS (₱25)', width=25, command=lambda: (label_for_codm_choice.pack_forget(),
                                                                       codop1.pack_forget(), codop2.pack_forget(),
                                                                       codop3.pack_forget(), codop4.pack_forget(),
                                                                       payment_cod1()))
        codop1.pack()
        codop2 = Button(text='150 GS (₱70)', width=25, command=lambda: (label_for_codm_choice.pack_forget(),
                                                                        codop1.pack_forget(), codop2.pack_forget(),
                                                                        codop3.pack_forget(), codop4.pack_forget(),
                                                                        payment_cod2()))
        codop2.pack()
        codop3 = Button(text='400 GS (₱180)', width=25, command=lambda: (label_for_codm_choice.pack_forget(),
                                                                         codop1.pack_forget(), codop2.pack_forget(),
                                                                         codop3.pack_forget(), codop4.pack_forget(),
                                                                         payment_cod3()))
        codop3.pack()
        codop4 = Button(text='1000 GS (₱420)', width=25, command=lambda: (label_for_codm_choice.pack_forget(),
                                                                          codop1.pack_forget(), codop2.pack_forget(),
                                                                          codop3.pack_forget(), codop4.pack_forget(),
                                                                          payment_cod4()))
        codop4.pack()

    def payment_cod1():     # Defined function for CODM as game choice
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 25
                if remaining_balance >= 25:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_cod1(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_cod1(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_cod2():
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 70
                if remaining_balance >= 70:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_cod2(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_cod2(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_cod3():
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 180
                if remaining_balance >= 180:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_cod3(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_cod3(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()

    def payment_cod4():
        def total():
            try:
                remaining_balance = int(coins_balance.get())
                expression = remaining_balance - 420
                if remaining_balance >= 420:
                    label_total = Label(root, text=f'Your remaining balance is ₱{expression}. Thank you for purchasing!'
                                                   '\nWould you like to purchase again?')
                    label_total.pack()
                    return_submit_yes = Button(width=25, text='Yes', command=lambda: (intro(),
                                                                                      label_total.pack_forget(),
                                                                                      return_submit_yes.pack_forget(),
                                                                                      return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(width=25, text='No', command=root.quit)
                    return_submit_no.pack()
                else:
                    label_total = Label(root, text='Your balance is insufficient. Please try again later.')
                    label_total.pack()
                    return_label = Label(root, text="Would you like to retry?")
                    return_label.pack()
                    return_submit_yes = Button(root, width=25, text='Yes',
                                               command=lambda: (payment_cod4(),
                                                                label_total.pack_forget(),
                                                                return_label.pack_forget(),
                                                                return_submit_yes.pack_forget(),
                                                                return_submit_no.pack_forget()))
                    return_submit_yes.pack()
                    return_submit_no = Button(root, width=25, text='No', command=root.quit)
                    return_submit_no.pack()
            except ValueError:
                error_label = (Label(text='Input is not a number. Would you like to retry?'))
                error_label.pack()
                return_submit_yes = Button(width=25, text='Yes', command=lambda: (payment_cod4(),
                                                                                  error_label.pack_forget(),
                                                                                  return_submit_yes.pack_forget(),
                                                                                  return_submit_no.pack_forget()))
                return_submit_yes.pack()
                return_submit_no = Button(width=25, text='No', command=root.quit)
                return_submit_no.pack()

        coins_balance_label = Label(root, text='Enter your Pixpay balance.')
        coins_balance_label.pack()
        coins_balance = Entry(root, width=15)
        coins_balance.pack()
        balance_submit = Button(text='Submit', width=15, command=lambda: (total(), coins_balance_label.pack_forget(),
                                                                          coins_balance.pack_forget(),
                                                                          balance_submit.pack_forget()))
        balance_submit.pack()
    # --------------------------------------------------------------------------------------------
    valorant_game_button = Button(text='Valorant', width=25, command=lambda: (valorant_game_choice(),
                                                                              label_for_intro.pack_forget(),
                                                                              valorant_game_button.pack_forget(),
                                                                              codm_game_button.pack_forget()))
    valorant_game_button.pack()
    codm_game_button = Button(text='CODM', width=25, command=lambda: (codm_game_choice(),
                                                                      label_for_intro.pack_forget(),
                                                                      valorant_game_button.pack_forget(),
                                                                      codm_game_button.pack_forget()))
    codm_game_button.pack()


intro()     # Calls the defined function "intro"
root.mainloop()     # Leaves the window open
