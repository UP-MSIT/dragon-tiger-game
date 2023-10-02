from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint


class DragonTiger:
    def __init__(self):
        self.gui = Tk()
        self.__user_chips = 10000
        self.__passConfirm = FALSE
        self.__passChoose = FALSE

        self.gui.resizable(0, 0)

        self.canvas = Canvas(self.gui, height=360, width=1333)
        self.canvas.pack()

        self.image = Image.open("img/background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        # self.background = Label(self.gui, image=self.background_image)
        # self.background.pack(fill=BOTH, expand=YES)
        self.bg_label = self.canvas.create_image((0, 0), image=self.background_image, anchor=N + W)


        # self.background.bind('<Configure>', self._resize_image)

        self.gui.geometry("900x600")
        self.gui.title("Dragon Tiger")
        # self.gui.iconbitmap(r'img/cards1.ico')

        self.__img = Image.open("img/back_card.png")
        self.__img = self.__img.resize((int(self.__img.width * .2), int(self.__img.height * .2)))
        photo = ImageTk.PhotoImage(self.__img)

        self.__lbl = Label(image=photo)
        self.__lbl2 = Label(image=photo)
        self.__lbl.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.__lbl2.place(relx=0.75, rely=0.3, anchor=CENTER)

        bets = Label(self.gui, text="BET: ", font=('', 45, 'bold'))
        # bets = self.canvas.create_text((410, 120), text='BET: ', font=('', 45, 'bold'), fill="#652828")
        self.__input_bet = Entry(self.gui)
        bets.place(relx=0.35, rely=0.8, anchor=CENTER)
        # self.canvas.itemconfig(bets)
        self.__input_bet.place(relx=0.55, rely=0.8, anchor=CENTER)

        self.open = Button(self.gui, text="OPEN CARD", bg='black', command=self.open_card)
        self.open.place(relx=0.1, rely=0.6, anchor=CENTER)
        self.dragon = Button(self.gui, text="DRAGON", bg='red', command=self.choose_dragon)
        self.dragon.place(relx=0.3, rely=0.6, anchor=CENTER)
        self.tiger = Button(self.gui, text="TIGER", bg='blue', command=self.choose_tiger)
        self.tiger.place(relx=0.75, rely=0.6, anchor=CENTER)
        self.tiger = Button(self.gui, text="DRAW", bg='green', command=self.choose_draw)
        self.tiger.place(relx=0.53, rely=0.45, anchor=CENTER)
        self.check = Button(self.gui, text="CONFIRM", command=self.confirm)
        self.check.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.check = Button(self.gui, text="EXIT", bg='black', command=self.exit)
        self.check.place(relx=0.95, rely=0.95, anchor=CENTER)

        self.__chip = Label(text=f"Chips  : {self.__user_chips}")
        self.__chip.place(relx=0.05, rely=0.05, anchor=CENTER)
        self.gui.mainloop()

    @property
    def user_chips(self):
        return self.__user_chips

    @user_chips.setter
    def user_chips(self, user_chips):
        self.__user_chips = user_chips

    @property
    def pass_confirm(self):
        return self.__passConfirm

    @pass_confirm.setter
    def pass_confirm(self, pass_confirm):
        self.__passConfirm = pass_confirm

    @property
    def pass_choose(self):
        return self.__passChoose

    @pass_choose.setter
    def pass_choose(self, pass_choose):
        self.__passChoose = pass_choose

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    @property
    def lbl(self):
        return self.__lbl

    @lbl.setter
    def lbl(self, lbl):
        self.__lbl = lbl

    @property
    def lbl2(self):
        return self.__lbl2

    @lbl2.setter
    def lbl2(self, lbl2):
        self.__lbl2 = lbl2

    @property
    def input_bet(self):
        return self.__input_bet

    @input_bet.setter
    def input_bet(self, input_bet):
        self.__input_bet = input_bet

    def display(self):
        if self.__choose == 0:
            self.txt = Label(text="Dragon", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        elif self.__choose == 1:
            self.txt = Label(text="  Tiger  ", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        elif self.__choose == 2:
            self.txt = Label(text="  Draw  ", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        else:
            self.txt = Label(text="Select", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)

    def choose_dragon(self):
        self.__choose = 0
        self.display()

    def choose_tiger(self):
        self.__choose = 1
        self.display()

    def choose_draw(self):
        back_img = Image.open("img/back_card.png")
        temp_back_img = ImageTk.PhotoImage(back_img)

        self.__lbl = Label(image=temp_back_img)
        self.__lbl1 = Label(image=temp_back_img)

        self.__choose = 2
        self.display()

    def confirm(self):
        self.__val = self.__input_bet.get()
        if not (self.__val.isdigit()):
            messagebox.showerror("Error", "Not Integer Number")
        elif not (self.__choose == 1 or self.__choose == 2 or self.__choose == 0):
            messagebox.showerror("Error", "Please Choose dragon OR tiger OR draw")
        else:
            try:
                if int(self.__val) > self.__user_chips or int(self.__val) <= 0:
                    messagebox.showerror("Sorry", "You have lost all your chips.")
                else:

                    messagebox.showinfo("Success", "Bet Successful")
                    self.open_card(self)
                    self.__passConfirm = TRUE
                    if self.__passChoose == TRUE:
                        Dragon = randint(1, 13)
                        Tiger = randint(1, 13)

                        opDragon = randint(1, 4)
                        opTiger = randint(1, 4)

                        self.imgDra = Image.open("img/cards/" + str(Dragon) + "_" + str(opDragon) + ".PNG")
                        self.photoDragon = ImageTk.PhotoImage(self.imgDra)

                        self.imgTi = Image.open("img/cards/" + str(Tiger) + "_" + str(opTiger) + ".PNG")
                        self.photoTiger = ImageTk.PhotoImage(self.imgTi)

                        self.__lbl = Label(image=self.photoDragon)
                        self.__lbl1 = Label(image=self.photoTiger)
                        self.__lbl.place(relx=0.3, rely=0.3, anchor=CENTER)
                        self.__lbl1.place(relx=0.75, rely=0.3, anchor=CENTER)

                        win = 99
                        if (Dragon < Tiger):
                            win = 1
                        elif (Dragon > Tiger):
                            win = 0
                        elif (Dragon == Tiger):
                            win = 2

                        if (self.__choose == win):
                            if (win != 2):
                                self.__val = int(self.__val) * 1
                            else:
                                self.__val = int(self.__val) * 7
                            self.__user_chips = self.__user_chips + int(self.__val)
                            messagebox.showinfo("You Win", " + " + str(self.__val) + " Chips")
                        else:
                            if (win != 2):
                                self.__user_chips = self.__user_chips - int(self.__val)
                                messagebox.showinfo("You Lose", " - " + str(self.__val) + " Chips")
                            else:
                                self.__user_chips = self.__user_chips - (int(self.__val) / 2)
                                messagebox.showinfo("You Lose", " - " + str((int(self.__val) / 2)) + " Chips")

                        self.__chip1 = Label(text=f"Chips   :  {self.__user_chips}  ")
                        self.__chip1.place(relx=0.05, rely=0.05, anchor=CENTER)
                        self.__passChoose = FALSE
                        self.__passConfirm = FALSE
                        self.__choose = 99
                        self.display()

                    else:
                        messagebox.showerror("Error", "Betting  Unsuccessful")
            except ValueError:
                messagebox.showerror("Error", "Error message")

    def open_card(self):
        if (self.__passConfirm == TRUE and self.__passChoose == TRUE):
            Dragon = randint(1, 13)
            Tiger = randint(1, 13)

            opDragon = randint(1, 4)
            opTiger = randint(1, 4)

            self.imgDra = Image.open("img/cards/" + str(Dragon) + "_" + str(opDragon) + ".PNG")
            self.photoDra = ImageTk.PhotoImage(self.imgDra)
            self.imgTi = Image.open("img/cards/" + str(Tiger) + "_" + str(opTiger) + ".PNG")
            self.photoTi = ImageTk.PhotoImage(self.imgTi)
            self.__lbl = Label(image=self.photoDra)
            self.__lbl1 = Label(image=self.photoTi)
            self.__lbl.place(relx=0.3, rely=0.3, anchor=CENTER)
            self.__lbl1.place(relx=0.75, rely=0.3, anchor=CENTER)

            win = 99
            if (Dragon < Tiger):
                win = 1
            elif (Dragon > Tiger):
                win = 0
            elif (Dragon == Tiger):
                win = 2

            if (self.__choose == win):
                if (win != 2):
                    self.__val = int(self.__val) * 1
                else:
                    self.__val = int(self.__val) * 7
                self.__user_chips = self.__user_chips + int(self.__val)
                messagebox.showinfo("You Win", " + " + str(self.__val) + " Chips")
            else:
                if (win != 2):
                    self.__user_chips = self.__user_chips - int(self.__val)
                    messagebox.showinfo("You Lose", " - " + str(self.__val) + " Chips")
                else:
                    self.__user_chips = self.__user_chips - (int(self.__val) / 2)
                    messagebox.showinfo("You Lose", " - " + str((int(self.__val) / 2)) + " Chips")

            self.__chip1 = Label(text=f"Chips   :  {self.__user_chips}  ")
            self.__chip1.place(relx=0.05, rely=0.05, anchor=CENTER)
            self.__passChoose = FALSE
            self.__passConfirm = FALSE
            self.__choose = 99
            self.display()

        else:
            messagebox.showerror("Error", "Betting  Unsuccessful")

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def exit(self):
        self.gui.destroy()
