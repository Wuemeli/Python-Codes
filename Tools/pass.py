import random
import string
import turtle


def password_generator():
    password = ""
    for i in range(8):
        password += random.choice(string.ascii_letters + string.digits)
    return password

turtle.ht()

turtle.write(password_generator(), font=("Arial", 16, "normal"))

turtle.setpos(0, 0)

turtle.mainloop()




