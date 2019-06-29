class Grid:
    def __init__(self, size, canvas, canvas_width, canvas_height):
        self.size = size
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.draw()

    def increase_size(self):
        self.size += 5
        self.draw()

    def decrease_size(self):
        if self.size > 10:
            self.size -= 5
            self.draw()

    def draw(self):
        self.canvas.delete("all")
        grid_width = round(self.canvas_width / self.size)
        grid_height = round(self.canvas_height / self.size)
        for i in range(grid_width):
            for j in range(grid_height):
                self.canvas.create_rectangle(self.size * i + 1, self.size * j + 1, self.size * (i + 1) + 1, self.size * (j + 1) + 1, tags="grid_sqaure_" + str(i) + "_" + str(j))
