"""
"error"			"info"
"questhead"	"question"
"warning"		"hourglass"
"gray75"		"gray50"
"gray25"		"gray12"
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Bitmap")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root,bg='white',bitmap = 'error',padx = 20, pady= 10)
label2 = tk.Label(root,bg='white',bitmap = 'info',padx = 20, pady= 10)
label3 = tk.Label(root,bg='white',bitmap = 'questhead',padx = 20, pady= 10)
label4 = tk.Label(root,bg='white',bitmap = 'question',padx = 20, pady= 10)
label5 = tk.Label(root,bg='white',bitmap = 'warning',padx = 20, pady= 10)
label6 = tk.Label(root,bg='white',bitmap = 'gray75',padx = 20, pady= 10)
label7 = tk.Label(root,bg='white',bitmap = 'hourglass',padx = 20, pady= 10)
label8 = tk.Label(root,bg='white',bitmap = 'gray50',padx = 20, pady= 10)
label9 = tk.Label(root,bg='white',bitmap = 'gray25',padx = 20, pady= 10)
label10 = tk.Label(root,bg='white',bitmap = 'gray12',padx = 20, pady= 10)

for i in range(1,11):
    label = f"label{i}"
    eval(label).pack()

root.mainloop()
