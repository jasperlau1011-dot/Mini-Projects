import tkinter as tk
import random

class BouncingBall:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = float(x)
        self.y = float(y)
        self.vx = random.uniform(100, 300)
        self.vy = random.uniform(-50, 50)
        self.radius = 18
        self.gravity = 980.0
        self.bounce = -0.8
        self.shape = canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=color, outline="#EEEEEE", width=2
        )

    def update(self, dt):
        self.vy += self.gravity * dt * 0.999
        self.x += self.vx * dt * 0.999
        self.y += self.vy * dt * 0.999
        if self.x + self.radius >= 580:
            self.x = 580 - self.radius
            self.vx *= self.bounce
        elif self.x - self.radius <= 20:
            self.x = 20 + self.radius
            self.vx *= self.bounce
        if self.y + self.radius >= 580:
            self.y = 580 - self.radius
            self.vy *= self.bounce
        self.canvas.coords(
            self.shape,
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius
        )

root = tk.Tk()
root.geometry("600x600")
root.title("Day 9: Object-Oriented Physics Engine")

canvas = tk.Canvas(root, width=600, height=600, bg="#1e1e1e")
canvas.pack(fill="both", expand=True)
balls = [
    BouncingBall(canvas, 100, 50, "#00ADB5"),
    BouncingBall(canvas, 300, 50, "#FF5722"),
    BouncingBall(canvas, 500, 50, "#4CAF50")
]

dt = 0.016

def game_loop():
    for ball in balls:
        ball.update(dt)
    
    root.after(16, game_loop)

game_loop()
root.mainloop()