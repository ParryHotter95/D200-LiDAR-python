import pyglet
import csv
import math


window = pyglet.window.Window()

class App(pyglet.window.Window):
    FILE = 'D:\\Python\\D200-LiDAR-python\\testfile.csv'
    shapes = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.origin_x = int(self.width/2)
        self.origin_y = int(self.height/2)
        self.generate_datapoints()
    
    def generate_datapoints(self):
        self.batch = pyglet.graphics.Batch()
        with open(self.FILE, "r", newline='') as csvfile:
            fieldnames = ['timestamp', 'angle', 'distance', 'signal']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for i, point in enumerate(reader):
                if int(point["distance"]) < 2500:
                    vector = pyglet.math.Vec2.from_polar(int(point["distance"])/10, math.radians(float(point["angle"]))).clamp(-249, 249)
                    p = pyglet.shapes.Circle(vector.x+self.origin_x, vector.y+self.origin_y, 1, batch=self.batch)
                    self.shapes.append(p)

        centerpoint = pyglet.shapes.Circle(self.origin_x, self.origin_y, 10, color=(255, 0, 0), batch=self.batch)
        self.shapes.append(centerpoint)


    def on_draw(self):
        # self.clear()
        self.batch.draw()

if __name__ == "__main__":
    app = App(500,500)
    pyglet.app.run()