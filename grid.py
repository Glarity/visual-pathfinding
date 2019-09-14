import time
import threading


class Grid:
    def __init__(self, scale, size, root, canvas, canvas_width, canvas_height):
        self.scale = scale
        self.size = size
        self.root = root
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.flood_speed = .01
        self.flood_start_x = 0
        self.flood_start_y = 0
        self.stop_thread_flag = 0
        self.clear_array()

    def increase_scale(self):
        self.scale += 5
        self.draw()

    def decrease_scale(self):
        if self.scale > 10:
            self.scale -= 5
            self.draw()

    def change_color(self, x, y, color):
        self.array[x, y] = color
        self.canvas.itemconfig("grid_sqaure_" + str(x) + "_" + str(y), fill=color)

    def clear_array(self):
        self.array = {(i, j): "white" for i in range(self.size) for j in range(self.size)}
        self.draw()

    def set_start(self, x, y):
        self.change_color(self.flood_start_x, self.flood_start_y, "white")
        self.flood_start_x = x
        self.flood_start_y = y
        self.change_color(x, y, "blue")

    def start_flood(self):
        def start_flood_thread():
            self.flood(self.flood_start_x, self.flood_start_y, "white", "green")
            print("Done flooding")
            self.stop_thread_flag = 0

        flood_thread = threading.Thread(target=start_flood_thread)
        flood_thread.start()
        print("Active threads: " + str(threading.active_count()))

    def stop_flood(self):
        print("Stopping flood")
        self.stop_thread_flag = 1

    def flood(self, x, y, target, replacement):
        if self.stop_thread_flag == 1:
            return
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return
        if self.array[x, y] == replacement:
            return
        elif x == self.flood_start_x and y == self.flood_start_y:
            self.change_color(x, y, replacement)
        elif self.array[x, y] != target:
            return
        else:
            self.change_color(x, y, replacement)

        self.root.update_idletasks()
        time.sleep(self.flood_speed)
        self.flood(x - 1, y, target, replacement)
        self.flood(x + 1, y, target, replacement)
        self.flood(x, y - 1, target, replacement)
        self.flood(x, y + 1, target, replacement)
        return

    def draw(self):
        self.canvas.delete("all")
        # grid_width = round(self.canvas_width / self.scale)
        # grid_height = round(self.canvas_height / self.scale)
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(self.scale * i + 1, self.scale * j + 1, self.scale * (i + 1) + 1, self.scale * (j + 1) + 1, tags="grid_sqaure_" + str(i) + "_" + str(j), fill=self.array[i, j])
        self.change_color(self.flood_start_x, self.flood_start_y, "blue")
