from grid import Grid
import tkinter as tk

HEIGHT = 600
WIDTH = 800

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
main_grid = Grid(15, 100, canvas, WIDTH, HEIGHT)

decrease_scale_button = tk.Button(root, text="Decrease Grid Scale", command=main_grid.decrease_scale)
increase_scale_button = tk.Button(root, text="Increase Grid Scale", command=main_grid.increase_scale)


def drawing(event):
    grid_x = int(event.x / main_grid.scale)
    grid_y = int(event.y / main_grid.scale)
    fill_color = ""
    if (event.state == 256):
        fill_color = "red"
    elif (event.state == 1024):
        fill_color = "blue"
    main_grid.change_color(grid_x, grid_y, fill_color)


canvas.bind("<B1-Motion>", drawing)
canvas.bind("<B3-Motion>", drawing)
canvas.pack()
decrease_scale_button.pack()
increase_scale_button.pack()
root.mainloop()
