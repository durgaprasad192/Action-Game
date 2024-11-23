import tkinter as tk
import random
window_width = 600
window_height = 600
player_size = 30
obstacle_size = 30
player_speed = 15
obstacle_speed = 3
level_up_score = 100

root = tk.Tk()





root.title("Enhanced Game")

canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

player = canvas.create_rectangle(
    window_width // 2 - player_size // 2, window_height // 2 - player_size // 2,
    window_width // 2 + player_size // 2, window_height // 2 + player_size // 2,
    fill="blue"
)

obstacles = []

score = 0
level = 1
score_text = canvas.create_text(10, 10, text=f"Score: {score}", anchor="nw", font=("Arial", 16))
level_text = canvas.create_text(10, 30, text=f"Level: {level}", anchor="nw", font=("Arial", 16))

def move_left(event):
    canvas.move(player, -player_speed, 0)

def move_right(event):
    canvas.move(player, player_speed, 0)

def move_up(event):
    canvas.move(player, 0, -player_speed)

def move_down(event):
    canvas.move(player, 0, player_speed)

def check_collision():
    player_coords = canvas.bbox(player)
    for obstacle in obstacles:
        obstacle_coords = canvas.bbox(obstacle)
        if (player_coords[2] > obstacle_coords[0] and player_coords[0] < obstacle_coords[2] and
            player_coords[3] > obstacle_coords[1] and player_coords[1] < obstacle_coords[3]):
            return True
    return False

def create_obstacles():
    global obstacles
    for _ in range(level * 3):
        x = random.randint(0, window_width - obstacle_size)
        y = random.randint(0, window_height - obstacle_size)
        obstacles.append(canvas.create_rectangle(x, y, x + obstacle_size, y + obstacle_size, fill="red"))

def move_obstacles():
    global score
    for obstacle in obstacles:
        canvas.move(obstacle, random.choice([-obstacle_speed, obstacle_speed]), random.choice([-obstacle_speed, obstacle_speed]))

        coords = canvas.bbox(obstacle)
        if coords[0] < 0 or coords[2] > window_width:
            canvas.move(obstacle, -random.choice([-obstacle_speed, obstacle_speed]), 0)
        if coords[1] < 0 or coords[3] > window_height:
            canvas.move(obstacle, 0, -random.choice([-obstacle_speed, obstacle_speed]))
    score += 1
def level_up():
    global level, player_speed, obstacles, score, level_up_score
    if score >= level_up_score * level:
        level += 1
        player_speed += 5
        create_obstacles()
        canvas.itemconfig(level_text, text=f"Level: {level}")
        canvas.itemconfig(score_text, text=f"Score: {score}")
def game_loop():
    global score
    move_obstacles()
    level_up()
    if check_collision():
        canvas.create_text(window_width // 2, window_height // 2, text="Game Over!", font=('Arial', 24), fill='red')
    else:
        root.after(50, game_loop)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
create_obstacles()
game_loop()
root.mainloop()