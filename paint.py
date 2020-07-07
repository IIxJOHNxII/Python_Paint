from tkinter import *
from tkinter import ttk, colorchooser
from tkinter.ttk import Scale


class main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.eraser_color = 'white'
        self.master.configure(background='white')
        self.old_x = None
        self.old_y = None
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)


        self.color_frame = LabelFrame(self.master, text='Color', font = ('arial',15), bd=5, relief=RIDGE, bg='white')
        self.color_frame.place(x=5, y=2, width=70, height=160)

        colors = ['#FFFFFF', '#000000', '#808080', '#FF0000', '#FFFF00', '#00FF00', '#008000', '#00FFFF', '#0000FF', '#000080']
        i=j=0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE, width=3, command=lambda col = color:self.select_color(col)).grid(row=i, column=j)
            i+=1
            if i==5:
                i=0
                j=1


        self.save_button = Button(self.master, text="Add brush\ncolor", bd=4, bg=self.color_bg, command=self.change_fg, width=8, relief=RIDGE)
        self.save_button.place(x=5, y=165)

        self.eraser_button = Button(self.master, text="Eraser", bd=4, bg=self.color_bg, command=self.eraser, width=8, relief=RIDGE)
        self.eraser_button.place(x=5, y=214)

        self.clear_button = Button(self.master, text="Clear", bd=4, bg=self.color_bg, command=self.clear, width=8, relief=RIDGE)
        self.clear_button.place(x=5, y=247)

        self.canvas_clour_button = Button(self.master, text="Backround", bd=4, bg=self.color_bg, command=self.change_bg, width=8, relief=RIDGE)
        self.canvas_clour_button.place(x=5, y=281)


        self.pen_size_scale_frame = LabelFrame(self.master, text='size', bd=5, bg=self.color_bg, font=('arial', 15, 'bold'), relief=RIDGE)
        self.pen_size_scale_frame.place(x=5, y=312, height=180, width=70)

        self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_ = 50, to = 0, length=150)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)


    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.pen_size.get(), fill=self.color_fg, capstyle=ROUND, smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):  # reseting or cleaning the canvas
        self.old_x = None
        self.old_y = None

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):  # changing the pen color
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

    def select_color(self, col):
        self.pen_color = col

    def change_bg(self):  # changing the background color canvas
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.c = Canvas(self.master, width=500, height=500, bg=self.color_bg, )
        self.c.pack(fill=BOTH, expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)

    def eraser(self):
        self.color_fg = self.color_bg


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.iconbitmap(r'icon.ico')
    root.title('Paint')
    root.mainloop()