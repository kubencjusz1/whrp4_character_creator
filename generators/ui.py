from tkinter import ttk


class DraggableLabel(ttk.Label):
    def __init__(self, parent, textvariable):
        super().__init__(parent, textvariable=textvariable)
        self.parent = parent
        self.bind("<ButtonPress-1>", self.on_start)
        self.bind("<B1-Motion>", self.on_drag_motion)

    def on_start(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def on_drag_motion(self, event):
        x = self.winfo_x() - self._drag_start_x + event.x
        y = self.winfo_y() - self._drag_start_y + event.y
        self.place(x=x, y=y)


def label_with_label(frame, text, var, column=0, row=0):
    label = ttk.Label(frame, textvariable=var)
    label.grid(row=row + 1, column=column, padx=5, pady=5)
    label = ttk.Label(frame, text=text)
    label.grid(row=row, column=column, padx=5, pady=5)


def spinbox_with_label(frame, text, var, from_, to, column=0, row=0):
    spinbox = ttk.Spinbox(frame,textvariable=var,from_=from_,to=to,width=5)
    spinbox.grid(row=row + 1, column=column, padx=5, pady=5)
    label = ttk.Label(frame, text=text)
    label.grid(row=row, column=column, padx=5, pady=5)
    return spinbox
