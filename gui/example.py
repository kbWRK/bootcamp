import tkinter as tk
def zrub_cos():
   if label["text"] == "hi":
       label.configure(text="ha")
   elif label["text"] == "ha":
       label.configure(text="ho")
   elif label["text"] == "ho":
       label.configure(text="hi")
   p = tk.Button(root, text="zmylka!")
   p.pack()


root = tk.Tk()
label = tk.Label(root, text="hi")
label.pack()
przycisk = tk.Button(root, text="kliknij", command=zrub_cos())
label.pack()
root.mainloop()