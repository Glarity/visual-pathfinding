from grid import Grid
import tkinter as tk
import sys

HEIGHT = 600
WIDTH = 800

sys.setrecursionlimit(10000)
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
button_frame = tk.Frame(root)
main_grid = Grid(15, 80, root, canvas, WIDTH, HEIGHT)


decrease_scale_button = tk.Button(button_frame, text="Decrease Grid Scale", command=main_grid.decrease_scale)
increase_scale_button = tk.Button(button_frame, text="Increase Grid Scale", command=main_grid.increase_scale)
clear_array_button = tk.Button(button_frame, text="Clear Array", command=main_grid.clear_array)
flood_button = tk.Button(button_frame, text="Flood", command=main_grid.start_flood)
stop_flood_button = tk.Button(button_frame, text="Stop Flood", command=main_grid.stop_flood)


def drawing(event):
    grid_x = int(event.x / main_grid.scale)
    grid_y = int(event.y / main_grid.scale)
    fill_color = ""
    if (event.state == 256):
        fill_color = "black"
    main_grid.change_color(grid_x, grid_y, fill_color)


def set_start(event):
    main_grid.set_start(int(event.x / main_grid.scale), int(event.y / main_grid.scale))


canvas.bind("<B1-Motion>", drawing)
canvas.bind("<Button-3>", set_start)
canvas.pack()
button_frame.pack(side=tk.BOTTOM)
decrease_scale_button.pack(side=tk.LEFT)
increase_scale_button.pack(side=tk.LEFT)
clear_array_button.pack(side=tk.LEFT)
flood_button.pack(side=tk.LEFT)
stop_flood_button.pack(side=tk.LEFT)
root.mainloop()
