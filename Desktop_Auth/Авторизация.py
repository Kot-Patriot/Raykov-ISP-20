from tkinter import *  # Импортирование модуля
from tkinter import messagebox  # Второй импорт ткинтера
window = Tk()  # Создание окна
window.title('Авторизация')
window.geometry('450x230')  # Настройка окна
window.resizable(False, False)  # Возможность менять размер окна
font_header = ('TimesNewRoman', 15)
font_entry = ('TimesNewRoman', 12)
label_font = ('TimesNewRoman', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def clicked():  # Создание функции clicked
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo(
        'Заголовок',
        '{username}, {password}'.format(
            username=username,
            password=password))  # Создание окна с данными пароля и логина


main_label = Label(
    window,
    text='Авторизация',
    font=label_font,
    justify=CENTER,
    **header_padding)  # Создание главного названия Label
main_label.pack()
username_label = Label(
    window,
    text='Имя пользователя',
    font=label_font,
    **base_padding)
username_label.pack()
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()
password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)  # Окно
password_entry.pack()
send_btn = Button(window, text='Войти', command=clicked)  # Кнопка войти
send_btn.pack(**base_padding)
window.mainloop()  # Запуск окна
