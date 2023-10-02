from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint
from tkmacosx import Button


class DragonTiger:
    def __init__(self):
        self.gui = Tk()
        self.__user_chips = 10000
        self.__passConfirm = FALSE
        self.__passChoose = FALSE

        self.image = Image.open("img/background.png")
        self.img_copy = self.image.copy()

        # self.background_image = ImageTk.PhotoImage(self.image)

        # self.background = Label(self.gui, image=self.background_image)
        # self.background.pack(fill=BOTH, expand=YES)
        # self.bg_label = self.canvas.create_image((0, 0), image=self.background_image, anchor=N + W)

        # self.background.bind('<Configure>', self._resize_image)

        self.gui.title("Dragon Tiger")

        w = 900
        h = 700

        # Get the screen dimensions
        sw = self.gui.winfo_screenwidth()
        sh = self.gui.winfo_screenheight()

        # Find the center of the point
        cx = int(sw/2 - h/2)
        cy = int(sh/2 - w/2)
        self.gui.geometry(f'{w}x{h}+{cx}+{cy}')
        self.gui.resizable(False, False)

        self.__img = Image.open("img/back_card1.png")
        self.__img = self.__img.resize((int(self.__img.width * .36), int(self.__img.height * .36)))

        self.__img1 = Image.open("img/back_card.png")
        self.__img1 = self.__img1.resize((int(self.__img1.width * .2), int(self.__img1.height * .2)))

        photo = ImageTk.PhotoImage(self.__img)
        photo1 = ImageTk.PhotoImage(self.__img1)

        self.__lbl = Label(image=photo)
        self.__lbl2 = Label(image=photo1)

        self.__lbl.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.__lbl2.place(relx=0.75, rely=0.3, anchor=CENTER)

        bets = Label(self.gui, text="BET: ", font=('', 45, 'bold'))
        self.__input_bet = Entry(self.gui, font=('', 30, 'bold'))

        bets.place(relx=0.55, rely=0.7, anchor=CENTER)
        self.__input_bet.place(relx=0.55, rely=0.8, anchor=CENTER)

        # self.open = Button(self.gui, text="OPEN CARD", fg='red', command=self.open_card, pady=12,
        #                    font=('', 30, 'bold'))
        # self.open.place(relx=0.65, rely=0.95, anchor=CENTER)

        self.check = Button(self.gui, text="CONFIRM", command=self.confirm, pady=12, font=(None, 30, 'bold'))
        self.check.place(relx=0.55, rely=0.90, anchor=CENTER)

        self.dragon = Button(self.gui, text="DRAGON", command=self.choose_dragon, pady=12, font=(None, 30, 'bold'))
        self.dragon.place(relx=0.3, rely=0.55, anchor=CENTER)

        self.tiger = Button(self.gui, text="TIGER", command=self.choose_tiger, pady=12, font=('', 30, 'bold'))
        self.tiger.place(relx=0.75, rely=0.55, anchor=CENTER)

        self.tiger = Button(self.gui, text="DRAW", command=self.choose_draw, pady=12, font=(None, 30, 'bold'))
        self.tiger.place(relx=0.53, rely=0.32, anchor=CENTER)

        self.check = Button(self.gui, text="EXIT", fg='red', command=self.exit, pady=12, font=(None, 30, 'bold'))
        self.check.place(relx=0.92, rely=0.95, anchor=CENTER)

        self.__chip = Label(text=f"Chips  : {self.__user_chips}", pady=12, font=(None, 45, 'bold'))
        self.__chip.place(relx=0.53, rely=0.05, anchor=CENTER)
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
    def img1(self):
        return self.__img1

    @img1.setter
    def img1(self, img1):
        self.__img1 = img1

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
            self.dragon = Button(
                self.gui, text="DRAGON", bg='red', fg='white', command=self.choose_dragon, pady=12,
                font=(None, 30, 'bold')
            )
            self.dragon.place(relx=0.3, rely=0.55, anchor=CENTER)
            self.tiger = Button(self.gui, text="TIGER", command=self.choose_tiger, pady=12, font=('', 30, 'bold'))
            self.tiger.place(relx=0.75, rely=0.55, anchor=CENTER)
            self.tiger = Button(self.gui, text="DRAW", command=self.choose_draw, pady=12, font=(None, 30, 'bold'))
            self.tiger.place(relx=0.53, rely=0.32, anchor=CENTER)
            self.__passChoose = TRUE

        elif self.__choose == 1:
            self.tiger = Button(self.gui, text="TIGER", bg='blue', fg='white', command=self.choose_tiger, pady=12,
                                font=('', 30, 'bold'))
            self.tiger.place(relx=0.75, rely=0.55, anchor=CENTER)
            self.dragon = Button(self.gui, text="DRAGON", command=self.choose_dragon, pady=12, font=(None, 30, 'bold'))
            self.dragon.place(relx=0.3, rely=0.55, anchor=CENTER)
            self.tiger = Button(self.gui, text="DRAW", command=self.choose_draw, pady=12, font=(None, 30, 'bold'))
            self.tiger.place(relx=0.53, rely=0.32, anchor=CENTER)
            self.__passChoose = TRUE

        elif self.__choose == 2:
            self.tiger = Button(
                self.gui, text="DRAW", bg='lightgreen', fg='white', command=self.choose_draw, pady=12,
                font=(None, 30, 'bold')
            )
            self.tiger.place(relx=0.53, rely=0.32, anchor=CENTER)
            self.dragon = Button(self.gui, text="DRAGON", command=self.choose_dragon, pady=12, font=(None, 30, 'bold'))
            self.dragon.place(relx=0.3, rely=0.55, anchor=CENTER)
            self.tiger = Button(self.gui, text="TIGER", command=self.choose_tiger, pady=12, font=('', 30, 'bold'))
            self.tiger.place(relx=0.75, rely=0.55, anchor=CENTER)
            self.__passChoose = TRUE

    def choose_dragon(self):
        self.__choose = 0
        self.display()

    def choose_tiger(self):
        self.__choose = 1
        self.display()

    def choose_draw(self):
        back_img = Image.open("img/back_card1.png")
        temp_back_img = ImageTk.PhotoImage(back_img)

        back_img_1 = Image.open("img/back_card.png")
        temp_back_img_1 = ImageTk.PhotoImage(back_img_1)

        self.__lbl = Label(image=temp_back_img)
        self.__lbl1 = Label(image=temp_back_img_1)

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

                        self.__chip1 = Label(text=f"Chips   :  {self.__user_chips}", pady=12, font=(None, 45, 'bold'))
                        self.__chip1.place(relx=0.53, rely=0.05, anchor=CENTER)

                        self.__passChoose = FALSE
                        self.__passConfirm = FALSE
                        self.__choose = 99
                        self.display()

                    else:
                        messagebox.showerror("Error", "Betting  Unsuccessful")
            except ValueError:
                messagebox.showerror("Error", "Error message")

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def exit(self):
        self.gui.destroy()
