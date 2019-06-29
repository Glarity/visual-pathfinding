class Grid:
    def __init__(self, size, canvas):
        self.size = size
        self.canvas = canvas
        self.draw()

    def increase_size(self):
        print("increase_size")
        self.size += 5
        self.draw()

    def decrease_size(self):
        if self.size > 10:
            self.size -= 5
            self.draw()

    def draw(self):
        self.canvas.delete("all")
        grid_width = round(self.canvas.winfo_width() / self.size)
        grid_height = round(self.canvas.winfo_height() / self.size)
        print("{}, {}".format(grid_width, grid_height))
        for i in range(grid_width):
            for j in range(grid_height):
                self.canvas.create_rectangle(self.size * i + 1, self.size * j + 1, self.size * (i + 1) + 1, self.size * (j + 1) + 1, tags="grid_sqaure_" + str(i) + "_" + str(j))
