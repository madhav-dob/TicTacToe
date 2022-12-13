from tkinter import *
from random import choice
import pyautogui
import gspread


sa = gspread.service_account(filename="requirements/service_account.json")
sheet = sa.open("ttt_database")
credentials = sheet.worksheet("credentials")
user_data = sheet.worksheet("Sheet2")

screen_width, screen_height = pyautogui.size()

window = Tk()
window.title("tic tac toe")
temp = str(screen_width // 6) + "+" + str(screen_height // 18)
window.geometry('900x650+' + temp)
window.configure(bg='#D9D9D9')
# window.overrideredirect(True)
window.resizable(0, 0)

# close_button = PhotoImage(file="requirements/45.png")
# butt = Button(window, image=close_button, cursor="hand2", highlightthickness=0, bd=0,
#               command=lambda: [window.destroy()])
# butt.pack(side='right', anchor='ne')
icon_grid = Frame(window, width=250, bg='#545454', height=700)
icon_grid.pack(side='left', anchor='n')
button_frame = Frame(window, width=650, bg='#D9D9D9', height=700)
button_frame.pack(anchor='s')

logged_in = False

blank = PhotoImage(file="requirements/blank.png")
acc_logo = PhotoImage(file="requirements/4.png")
about_logo = PhotoImage(file="requirements/8.png")
contact_logo = PhotoImage(file="requirements/7.png")
account = PhotoImage(file="requirements/1.png")
about = PhotoImage(file="requirements/2.png")
contact_us = PhotoImage(file="requirements/3.png")
logo = PhotoImage(file="requirements/18.png")
photo = PhotoImage(file="requirements/block.png")
set_logo = PhotoImage(file="requirements/41.png")
set_logo2 = PhotoImage(file="requirements/40.png")
settings = PhotoImage(file="requirements/42.png")
empty = PhotoImage(file="requirements/43.png")
banner = PhotoImage(file="requirements/44.png")
user_win_result = PhotoImage(file="requirements/48.png")
comp_win_result = PhotoImage(file="requirements/49.png")
draw_result = PhotoImage(file="requirements/50.png")
banner_login = PhotoImage(file="requirements/32.png")
arrow = PhotoImage(file="requirements/17.png")
user_pass = PhotoImage(file="requirements/12.png")
close_button = PhotoImage(file="requirements/13.png")
login_btn = PhotoImage(file="requirements/14.png")
grad = PhotoImage(file="requirements/15.png")
wrn2 = PhotoImage(file="requirements/22.png")
wrn1 = PhotoImage(file="requirements/26.png")
acc_logo2 = PhotoImage(file="requirements/33.png")

symbol_choice_label = PhotoImage(file="requirements/Choose your symbol.png")
restart = PhotoImage(file="requirements/reset.png")
symbol_user = PhotoImage(file="requirements/cross.png")
symbol_comp = PhotoImage(file="requirements/circle.png")
user_win_symbol = PhotoImage(file="requirements/cross_win.png")
comp_win_symbol = PhotoImage(file="requirements/circle_win.png")
cross_name = PhotoImage(file="requirements/cross_name.png")
circle_name = PhotoImage(file="requirements/circle_name.png")
you_win = PhotoImage(file="requirements/you_win.png")
you_lose = PhotoImage(file="requirements/you_lose.png")

hello = PhotoImage(file="requirements/20.png")
face = PhotoImage(file="requirements/23.png")
logout_btn = PhotoImage(file="requirements/24.png")
logout_btn2 = PhotoImage(file="requirements/25.png")
banner_about = PhotoImage(file="requirements/34.png")
blank_about = PhotoImage(file="requirements/38.png")
close_button_about = PhotoImage(file="requirements/37.png")
about_logo2 = PhotoImage(file="requirements/9.png")
main_pic_aboutwindow = PhotoImage(file="requirements/39.png")
stats_banner = PhotoImage(file="requirements/wins_loses.png")
# defining empty lists

all_positions = [[1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2]]
user_positions_list = []
comp_positions_list = []
arrangements = [

    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[3, 0], [3, 1], [3, 2]],
    [[1, 0], [2, 0], [3, 0]],
    [[1, 1], [2, 1], [3, 1]],
    [[1, 2], [2, 2], [3, 2]],
    [[1, 2], [2, 1], [3, 0]],
    [[1, 0], [2, 1], [3, 2]],
]


def admin():
    global button_frame
    global icon_grid
    v = StringVar(window, "1")

    Label(icon_grid, image=banner, bd=0).grid(row=0, column=0, columnspan=2)
    Label(icon_grid, image=blank, bd=0).grid(row=1, column=0, columnspan=2)
    Label(icon_grid, image=acc_logo, bd=0).grid(row=2, column=0)
    Label(icon_grid, image=about_logo, bd=0).grid(row=3, column=0)
    Label(icon_grid, image=contact_logo, bd=0).grid(row=4, column=0)
    Label(icon_grid, image=set_logo, bd=0).grid(row=5, column=0)
    Label(icon_grid, image=blank, bd=0).grid(row=6, column=0, columnspan=2)
    Label(icon_grid, image=logo, bd=0).grid(row=7, column=0, columnspan=2)
    Label(icon_grid, image=blank, bd=0).grid(row=8, column=0, columnspan=2)

    button1 = Button(icon_grid, image=account, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [account_win(window)])
    button1.grid(row=2, column=1)
    button2 = Button(icon_grid, image=about, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [about_win(window)])
    button2.grid(row=3, column=1)
    button3 = Button(icon_grid, image=contact_us, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [contact_win(window)])
    button3.grid(row=4, column=1)
    button4 = Button(icon_grid, image=settings, cursor="hand2", highlightthickness=0, bd=0,
                     command=lambda: [setting_win(window)]
                     )
    button4.grid(row=5, column=1)

    btn1 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 1, 0, button_frame)])
    btn1.grid(row=1, column=0, padx=2, pady=2)
    btn2 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 1, 1, button_frame)])
    btn2.grid(row=1, column=1, padx=2, pady=2)
    btn3 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 1, 2, button_frame)])
    btn3.grid(row=1, column=2, padx=2, pady=2)
    btn4 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 2, 0, button_frame)])
    btn4.grid(row=2, column=0, padx=2, pady=2)
    btn5 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 2, 1, button_frame)])
    btn5.grid(row=2, column=1, padx=2, pady=2)
    btn6 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 2, 2, button_frame)])
    btn6.grid(row=2, column=2, padx=2, pady=2)
    btn7 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 3, 0, button_frame)])
    btn7.grid(row=3, column=0, padx=2, pady=2)
    btn8 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 3, 1, button_frame)])
    btn8.grid(row=3, column=1, padx=2, pady=2)
    btn9 = Button(button_frame, image=photo, cursor="hand2", bd=0, highlightthickness=0,
                  command=lambda: [change_photo(symbol_user, 3, 2, button_frame)])
    btn9.grid(row=3, column=2, padx=2, pady=2)

    Label(button_frame, image=symbol_choice_label, height=30, borderwidth=0) \
        .grid(row=4, column=0, columnspan=2)

    Label(button_frame, image=empty, borderwidth=0).grid(row=0, column=0, columnspan=3)

    Radiobutton(button_frame, image=cross_name, bg='#d9d9d9', cursor="x_cursor", \
                command=lambda: symbol_choice("cross"), variable=v, value=1).grid(row=5, column=0, ipady=0)

    Radiobutton(button_frame, image=circle_name, bg='#d9d9d9', cursor="circle", \
                command=lambda: symbol_choice("circle"), variable=v, value=2).grid(row=5, column=1, ipady=0)

    window.mainloop()


def change_photo(i, m, n, f):
    Label(f, image=i, bd=0).grid(row=m, column=n)

    user_positions_list.append([m, n])
    comp_response2()


def change_window_icons(i, m, n, f):
    Label(f, image=i, bd=0).grid(row=m, column=n)


def symbol_choice(n):
    global symbol_user
    global symbol_comp
    global user_win_symbol
    global comp_win_symbol
    if n == 'cross':
        symbol_user = PhotoImage(file="requirements/cross.png")
        symbol_comp = PhotoImage(file="requirements/circle.png")
        user_win_symbol = PhotoImage(file="requirements/cross_win.png")
        comp_win_symbol = PhotoImage(file="requirements/circle_win.png")
    else:
        symbol_user = PhotoImage(file="requirements/circle.png")
        symbol_comp = PhotoImage(file="requirements/cross.png")
        user_win_symbol = PhotoImage(file="requirements/circle_win.png")
        comp_win_symbol = PhotoImage(file="requirements/cross_win.png")


def about_win(win):
    main = Toplevel(win)
    temp = str(screen_width // 2 - 200) + "+" + str(screen_height // 2 - 255)
    main.geometry('650x500+' + temp)
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)



    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_about, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Label(entry_frame, image=blank_about, padx=0, pady=0, bd=0).grid(row=0, column=1)
    Label(entry_frame, image=main_pic_aboutwindow, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=3)

    Button(entry_frame, image=close_button_about, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), change_window_icons(about_logo, 3, 0, icon_grid)]).grid(row=0, column=2)

    change_window_icons(about_logo2, 3, 0, icon_grid)
    main.mainloop()
def my_self(win):
    global button_frame2
    global user_name,total_draws,total_wins,total_loses

    main = Toplevel(win)
    temp = str(screen_width // 2 - 200) + "+" + str(screen_height // 2 - 255)
    main.geometry('650x500+' + temp)
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)
    total_wins = user_data.col_values(2)[index]
    total_loses = user_data.col_values(3)[index]
    total_draws = user_data.col_values(4)[index]

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), change_window_icons(acc_logo, 2, 0, icon_grid)]).grid(row=0,
                                                                                           column=1)

    Label(entry_frame, text="       " + user_name, bg='#D1D1D1', font=('verdana', 27), bd=0).grid(row=3, column=0)
    Label(entry_frame, image=hello, bd=0).grid(row=2, column=0)
    Label(entry_frame, image=face, bd=0).grid(row=2, column=1, rowspan=2, columnspan=2)
    Label(entry_frame, image=arrow, padx=0, pady=0, bd=0).grid(row=1, column=0)
    Label(entry_frame, image=stats_banner, padx=0, pady=0, bd=0).grid(row=4, column=0,columnspan = 2)
    Label(entry_frame, text=str(int(total_loses)+int(total_wins)+int(total_draws))+'           '+total_wins, bg='#D1D1D1', font=('verdana', 27), bd=0).grid(row=5, column=0)
    Label(entry_frame, text=total_loses + '        ' +total_draws+ ' ', bg='#D1D1D1', font=('verdana', 27), bd=0).grid(row=5, column=1)


    #Label(entry_frame, image=grad, padx=0, pady=0, bd=0).grid(row=4, column=0, rowspan=2)
    change_window_icons(acc_logo2, 2, 0, icon_grid)
    main.mainloop()

def account_win(win):
    def login_final(main):

        def close():
            error.destroy()
            entry1.config(fg='black')
            entry2.config(fg='black')

        global user_name
        global logged_in
        global index
        entry1.config(fg='black')
        entry2.config(fg='black')
        u = user.get()
        p = password.get()
        if u in users:
            index = users.index(u)

            if passwords[index] == p:
                print("values matched")
                user_name = u
                logged_in = True
                main.destroy()
                my_self(window)

            else:
                entry2.config(fg='red')
                error = Toplevel(main)
                error.title("Error")
                error.geometry('250x150+500+400')
                error.config(bg='#F4AB90')
                error.protocol("WM_DELETE_WINDOW", close)
                error.resizable(0, 0)
                Label(error, text='WRONG', image=wrn1, bd=0).pack()


        else:
            entry1.config(fg='red')
            error = Toplevel(main)
            error.title("Error")
            error.geometry('250x150+500+400')
            error.config(bg='#F4AB90')
            error.protocol("WM_DELETE_WINDOW", close)
            error.resizable(0, 0)
            Label(error, text='WRONG', image=wrn2, bd=0).pack()

    users = credentials.col_values(1)
    passwords = credentials.col_values(2)
    password = StringVar()
    user = StringVar()

    if logged_in :
        my_self(window)
    else:
        main = Toplevel(win)
        temp = str(screen_width // 2 - 200) + "+" + str(screen_height // 2 - 255)
        main.geometry('650x500+' + temp)
        main.configure(bg='#D1D1D1')
        main.overrideredirect(True)
        main.resizable(0, 0)


        entry_frame = Frame(main, bg='#D1D1D1', width=700)
        entry_frame.pack(side='left', anchor='n')

        Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
        Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
               command=lambda: [main.destroy(), change_window_icons(acc_logo, 2, 0, icon_grid)]).grid(row=0,
                                                                                               column=1)
        Label(entry_frame, image=arrow, padx=0, pady=0, bd=0).grid(row=1, column=0)
        Label(entry_frame, image=grad, padx=0, pady=0, bd=0).grid(row=4, column=0, rowspan=2)

        Label(entry_frame, image=user_pass, padx=0, pady=0, bd=0).grid(row=2, column=0, rowspan=2)
        entry1 = Entry(entry_frame, text=user, width=12, font=('verdana', 25), fg='black', bg='white')
        entry1.grid(row=2, column=1)

        entry2 = Entry(entry_frame, text=password, width=12, show="*", fg='black', font=('verdana', 25), bg='white')
        entry2.grid(row=3, column=1)

        Button(entry_frame, image=login_btn, cursor='hand2', width=200, height=60, highlightthickness=0, bd=0,
               command=lambda: [login_final(main)]).grid(padx=4, row=4, column=1)
        change_window_icons(acc_logo2, 2, 0, icon_grid)
        main.mainloop()


def contact_win(win):

    main = Toplevel(win)
    temp = str(screen_width // 2 - 200) + "+" + str(screen_height // 2 - 255)
    main.geometry('650x500+' + temp)
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)
    banner_login = PhotoImage(file="requirements/35.png")
    close_button = PhotoImage(file="requirements/37.png")
    blank = PhotoImage(file="requirements/38.png")
    contact_logo = PhotoImage(file="requirements/7.png")
    contact_logo2 = PhotoImage(file="requirements/6.png")
    main_pic = PhotoImage(file="requirements/46.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Label(entry_frame, image=main_pic, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=3)
    Label(entry_frame, image=blank, padx=0, pady=0, bd=0).grid(row=0, column=1)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), change_window_icons(contact_logo, 4, 0, icon_grid)]).grid(row=0, column=2)

    change_window_icons(contact_logo2, 4, 0, icon_grid)
    main.mainloop()


def setting_win(win):
    main = Toplevel(win)
    temp = str(screen_width // 2 - 200) + "+" + str(screen_height // 2 - 255)
    main.geometry('650x500+' + temp)
    main.configure(bg='#D1D1D1')
    main.overrideredirect(True)
    main.resizable(0, 0)
    banner_login = PhotoImage(file="requirements/36.png")
    close_button = PhotoImage(file="requirements/37.png")
    blank = PhotoImage(file="requirements/38.png")
    setting_logo = PhotoImage(file="requirements/41.png")
    setting_logo2 = PhotoImage(file="requirements/40.png")
    main_pic = PhotoImage(file="requirements/47.png")

    entry_frame = Frame(main, bg='#D1D1D1', width=700)
    entry_frame.pack(side='top', anchor='w')

    Label(entry_frame, image=banner_login, padx=0, pady=0, bd=0).grid(row=0, column=0)
    Label(entry_frame, image=main_pic, padx=0, pady=0, bd=0).grid(row=1, column=0, columnspan=3)
    Label(entry_frame, image=blank, padx=0, pady=0, bd=0).grid(row=0, column=1)
    Button(entry_frame, image=close_button, highlightthickness=0, bd=0,
           command=lambda: [main.destroy(), change_window_icons(set_logo, 5, 0, icon_grid)]).grid(row=0, column=2)

    change_window_icons(set_logo2, 5, 0, icon_grid)
    main.mainloop()


def check_comp_win():
    for i in arrangements:

        p = 0
        for j in i:

            if j in comp_positions_list:
                p += 1

            else:
                pass
        if p == 3:
            print("comp win")
            win_display(i, 'comp')
            return 1


def win_display(m, client):
    if client == 'user':
        symbol = user_win_symbol

    else:
        symbol = comp_win_symbol
    j = all_positions.copy()

    for i in m:
        Label(button_frame, image=symbol, bd=0).grid(row=i[0], column=i[1])
    for i in user_positions_list:
        j.remove(i)
    for i in comp_positions_list:
        j.remove(i)
    if j:
        for i in j:
            Label(button_frame, image=photo, bd=0).grid(row=i[0], column=i[1])

    win_dialogbox(client)


def win_dialogbox(client):
    global comp_moves, user_moves
    user_positions_list.clear()
    comp_positions_list.clear()
    comp_moves = all_positions.copy()
    user_moves = all_positions.copy()
    if client == 'user':
        bg_photo = user_win_result
        if logged_in:
            user_data.update_cell(index+1,2,str(int(total_wins)+1))

    elif client == 'draw':
        bg_photo = draw_result
        if logged_in:
            draw = user_data.col_values(4)[index]
            user_data.update_cell(index+1,4, str(int(draw)+ 1))

    else:
        bg_photo = comp_win_result
        if logged_in:
            user_data.update_cell(index+1,3, str(int(total_loses) + 1))
    win = Toplevel(window)
    temp = str(screen_width // 2 - 70) + "+" + str(screen_height // 2 - 70)
    win.geometry('250x200+' + temp)
    win.overrideredirect(True)
    win.resizable(0, 0)

    Label(win, image=bg_photo, padx=0, pady=0, bd=0).pack()
    btn = Button(win, image=restart, highlightthickness=0, bd=0,
                 command=lambda: [win.destroy(), admin()])
    btn.pack()
    win.mainloop()


def comp_response2():
    global user_moves, comp_moves
    comp_moves = []
    user_moves = []

    con = 'un_done'
    print("length of user list", len(user_positions_list))
    print("user list at starting :", user_positions_list)
    print("comp list at starting :", comp_positions_list)
    if len(user_positions_list) > 1 and len(user_positions_list) < 5:

        for i in arrangements:
            if con == 'un_done':

                o = i.copy()

                p = 0
                for j in i:

                    if j in user_positions_list:
                        p += 1
                        o.remove(j)
                    else:
                        pass
                if p == 3:
                    print("user won1")
                    win_display(i, 'user')
                    con = 'done'

        if con == 'un_done':
            for i in arrangements:
                if con == 'un_done':
                    l = i.copy()

                    m = 0

                    for j in i:

                        if j in comp_positions_list:
                            m += 1
                            l.remove(j)

                        else:
                            pass
                    if m == 2:

                        comp_moves = all_positions.copy()
                        for a in user_positions_list:
                            comp_moves.remove(a)
                        for d in comp_positions_list:
                            comp_moves.remove(d)

                        if l[0] in comp_moves:
                            print("found two moves of comp, winning possibility")
                            Label(button_frame, image=symbol_comp, bd=0).grid(row=l[0][0], column=l[0][1])
                            comp_positions_list.append([l[0][0], l[0][1]])
                            print('user_locs', user_positions_list)
                            print('comp_locs', comp_positions_list)
                            con = 'done'
                            check_comp_win()

        if con == 'un_done':
            for i in arrangements:
                if con == 'un_done':

                    o = i.copy()

                    p = 0
                    for j in i:

                        if j in user_positions_list:
                            p += 1
                            o.remove(j)
                        else:
                            pass

                    if p == 2:

                        user_moves = all_positions.copy()
                        for a in user_positions_list:
                            user_moves.remove(a)
                        for d in comp_positions_list:
                            user_moves.remove(d)

                        if o[0] in user_moves:
                            print("found two moves of user, blocking the win")
                            Label(button_frame, image=symbol_comp, bd=0).grid(row=o[0][0], column=o[0][1])
                            comp_positions_list.append([o[0][0], o[0][1]])
                            print('user_locs', user_positions_list)
                            print('comp_locs', comp_positions_list)
                            con = 'done'
                            check_comp_win()
        if con == 'un_done':

            comp_moves = all_positions.copy()
            for a in user_positions_list:
                comp_moves.remove(a)
            for d in comp_positions_list:
                comp_moves.remove(d)
            print('comp_moves', comp_moves)
            for b in comp_positions_list:
                if con == 'un_done':
                    temp_row = [1, 2, 3]
                    temp_col = [0, 1, 2]
                    x, y = b[0], b[1]
                    print("x,y values", x, y)
                    temp_row.remove(x)
                    temp_col.remove(y)
                    print("temp_row", temp_row)
                    print("temp_col", temp_col)
                    if [temp_row[0], b[1]] in comp_moves and [temp_row[1], b[1]] in comp_moves:

                        print("no threat, building a base by 1 ")
                        Label(button_frame, image=symbol_comp, bd=0).grid(row=temp_row[1], column=b[1])
                        comp_positions_list.append([temp_row[1], b[1]])
                        print('user_locs', user_positions_list)
                        print('comp_locs', comp_positions_list)
                        con = 'done'


                    elif [b[0], temp_col[0]] in comp_moves and [b[0], temp_col[1]] in comp_moves:

                        print("no threat, building a base by 2 ")
                        Label(button_frame, image=symbol_comp, bd=0).grid(row=b[0], column=temp_col[0])
                        comp_positions_list.append([b[0], temp_col[0]])
                        print('user_locs', user_positions_list)
                        print('comp_locs', comp_positions_list)
                        con = 'done'


                    elif [temp_row[0], temp_row[0]] in comp_moves and [temp_row[1], temp_row[1]] in comp_moves:

                        print("no threat, building a base by 3 ")
                        Label(button_frame, image=symbol_comp, bd=0).grid(row=temp_row[1], column=temp_row[1])
                        comp_positions_list.append([temp_row[1], temp_row[1]])
                        print('user_locs', user_positions_list)
                        print('comp_locs', comp_positions_list)
                        con = 'done'

                    else:

                        print("building base ka else")
                        comp_moves = all_positions.copy()
                        for i in user_positions_list:
                            comp_moves.remove(i)
                        for i in comp_positions_list:
                            comp_moves.remove(i)
                        move = choice(comp_moves)
                        Label(button_frame, image=symbol_comp, bd=0).grid(row=move[0], column=move[1])
                        comp_positions_list.append([move[0], move[1]])
                        print('user_locs', user_positions_list)
                        print('comp_locs', comp_positions_list)
                        con = 'done'

    elif len(user_positions_list) == 5:
        co = "undone"
        for i in arrangements:

            o = i.copy()

            p = 0
            for j in i:

                if j in user_positions_list:
                    p += 1
                    o.remove(j)
                else:
                    pass
            if p == 3:
                print("user won2")
                win_display(i, 'user')
                co = 'done'

            else:
                co = 'undone'
        if co == 'undone':
            print("its a draw")
            win_dialogbox('draw')


    elif len(user_positions_list) == 1:

        print("first time")
        comp_moves = all_positions.copy()
        for i in user_positions_list:
            comp_moves.remove(i)
        move = choice(comp_moves)
        Label(button_frame, image=symbol_comp, bd=0).grid(row=move[0], column=move[1])
        comp_positions_list.append([move[0], move[1]])
        print('user_locs', user_positions_list)
        print('comp_locs', comp_positions_list)

    else:
        print("else ka bhi else")


admin()
