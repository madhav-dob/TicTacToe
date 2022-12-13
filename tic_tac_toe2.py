'''
 This is the second file and a sequel to tic_tac_toe.py
 the code was copied from that file into this

'''

from tkinter import *
import random

window = Tk()
window.geometry('520x750')
window.resizable(0, 0)
window.configure(bg='#d9d9d9')
window.title('tic tac toe game')
print("executed this !")

banner = PhotoImage(file="main_label.png")

Label(window, image=banner, borderwidth=0, width=330).pack(anchor=W)

button_frame = Frame(window, bg='#d9d9d9', width=312, height=272.5)
button_frame.pack()

v = StringVar(window, "1")
radio_button_frame = Frame(window, bg='#d9d9d9', width=312, height=100)
radio_button_frame.pack()

# importing photos :-
symbol_choice_label = PhotoImage(file="Choose your symbol.png")
photo = PhotoImage(file="block.png")
symbol_user = PhotoImage(file="cross.png")
symbol_comp = PhotoImage(file="circle.png")
user_win_symbol = PhotoImage(file="cross_win.png")
comp_win_symbol = PhotoImage(file="circle_win.png")
cross_name = PhotoImage(file="cross_name.png")
circle_name = PhotoImage(file="circle_name.png")
you_win = PhotoImage(file="you_win.png")
you_lose = PhotoImage(file="you_lose.png")
reset_button = PhotoImage(file="reset.png")

user_loc = []
comp_loc = []
con = 0
arrangements = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def symbol_choice(n):
    global symbol_user
    global symbol_comp
    global user_win_symbol
    global comp_win_symbol
    if n == 'cross':
        symbol_user = PhotoImage(file="cross.png")
        symbol_comp = PhotoImage(file="circle.png")
        user_win_symbol = PhotoImage(file="cross_win.png")
        comp_win_symbol = PhotoImage(file="circle_win.png")
    else:
        symbol_user = PhotoImage(file="circle.png")
        symbol_comp = PhotoImage(file="cross.png")
        user_win_symbol = PhotoImage(file="circle_win.png")
        comp_win_symbol = PhotoImage(file="cross_win.png")


def display_photo(n, m, p):
    # func for changing block image

    global user_loc, comp_loc

    if p == 1:
        panel = Label(button_frame, image=symbol_user)
        panel.grid(row=n, column=m)
        user_loc.append((n, m))
        # print("user locations", user_loc)
    else:
        panel = Label(button_frame, image=symbol_comp)
        panel.grid(row=n, column=m)
        comp_loc.append((n, m))
        # print("comp locations", comp_loc)



def comp_response():
    global con
    print(con)
    for i in arrangements:
        r = 0
        t = []
        for j in i:
            if j in user_loc:
                t.append(j)
                r += 1
            else:
                pass
        if r == 3:
            print("You Won !")
            # print(t)
            #win(t, 1)
            play()
            clear()

            con = 1
        else:
            pass
    if con != 1:
        temp_list = []
        for i, j in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
            if (i, j) in user_loc:
                pass
            elif (i, j) in comp_loc:
                pass
            else:
                temp_list.append((i, j))
        # rint("comp options",temp_list)
        if temp_list:
            a, b = random.choice(temp_list)

            display_photo(a, b, 2)

            for f in arrangements:
                z = []
                h = 0
                for g in f:
                    if g in comp_loc:
                        h += 1
                        z.append((g))
                    else:
                        pass
                if h == 3:
                    print("Computer Won !")
                    # print(z)
                    #win(z, 2)
                    play()
                    clear()



                else:
                    pass
        else:
            pass
    else:
        con = 0
        print("inside comp response")
        print("con", con)
        print("user loc", user_loc)
        print("comp loc", comp_loc)


def clear():
    global user_loc, comp_loc, con
    user_loc = []
    comp_loc = []
    # con = 0


def win(b, o):
    global n
    for c, d in b:
        if o == 1:
            panel = Label(button_frame, image=user_win_symbol)
            panel.grid(row=c, column=d)

        else:
            panel = Label(button_frame, image=comp_win_symbol)
            panel.grid(row=c, column=d)
    play()
    clear()


def play():

    Label(radio_button_frame, image=symbol_choice_label, height=30, borderwidth=0) \
        .grid(row=0, column=0, columnspan=2)

    Radiobutton(radio_button_frame, text='Cross', image=cross_name, bg='#d9d9d9', cursor="x_cursor", font= \
        ("Arial Bold", 30), command=lambda: symbol_choice("cross"), variable=v, value=1).grid(row=1, column=0, ipady=0)

    Radiobutton(radio_button_frame, text='Circle', image=circle_name, bg='#d9d9d9', cursor="circle", font= \
        ("Arial Bold", 30), command=lambda: symbol_choice("circle"), variable=v, value=2).grid(row=1, column=2, ipady=0)

    # main program begins :

    btn1 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(0, 0, 1), comp_response()])
    btn1.grid(row=0, column=0, padx=2, pady=2)

    btn2 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(0, 1, 1), comp_response()])
    btn2.grid(row=0, column=1, padx=2, pady=2)

    btn3 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(0, 2, 1), comp_response()])
    btn3.grid(row=0, column=2, padx=2, pady=2)

    btn4 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(1, 0, 1), comp_response()])
    btn4.grid(row=1, column=0, padx=2, pady=2)

    btn5 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(1, 1, 1), comp_response()])
    btn5.grid(row=1, column=1, padx=2, pady=2)

    btn6 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(1, 2, 1), comp_response()])
    btn6.grid(row=1, column=2, padx=2, pady=2)

    btn7 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(2, 0, 1), comp_response()])
    btn7.grid(row=2, column=0, padx=2, pady=2)

    btn8 = Button(button_frame, width=155, height=155, image=photo, bd=0,
                  cursor="hand2", command=lambda: [display_photo(2, 1, 1), comp_response()])
    btn8.grid(row=2, column=1, padx=2, pady=2)

    btn9 = Button(button_frame, width=155, height=155, image=photo, bd=0, \
                  cursor="hand2", command=lambda: [display_photo(2, 2, 1), comp_response()])
    btn9.grid(row=2, column=2, padx=2, pady=2)


play()
window.mainloop()
