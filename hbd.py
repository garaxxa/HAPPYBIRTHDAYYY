import turtle
import random
import pygame
import time

# Initialize Pygame for playing the birthday song
pygame.mixer.init()

# Function to play the birthday song
def play_music():
    pygame.mixer.music.load("hbd.mp3")  # Replace with your mp3 file path
    pygame.mixer.music.play()

# Function to display cake decoration
def decorate_cake():
    turtle.penup()
    turtle.goto(100, 0)
    turtle.color("pink")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(170)
    turtle.left(90)
    turtle.forward()
    turtle.left(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.forward(95)
    turtle.end_fill()

# Function to fly balloons
def fly_balloons():
    colors = ["red", "orange", "brown", "green", "blue", "purple", "grey"]
    turtle.penup()
    turtle.goto(10, -50)
    turtle.pendown()
    for each_color in colors:
        angle = 360 / len(colors)
        turtle.color(each_color)
        turtle.circle(10)
        turtle.right(angle)
        turtle.forward(10)

# Function to light candles
def light_candle():
    positions = [-60, -30, 0, 30, 60]
    colors = ["red", "blue", "yellow", "green", "orange"]
    for i, pos in enumerate(positions):
        turtle.penup()
        turtle.goto(pos, 20)
        turtle.color(colors[i])
        turtle.pendown()
        turtle.forward(20)

# Function to display rotating messages
def show_message(messages):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(0, 100)  # Position above the cake
    text_turtle.color("white")
    for message in messages:
        text_turtle.clear()
        text_turtle.write(message, font=("Verdana", 16, "normal"), align="center")
        time.sleep(2)

# Function to display and hide the initial "Happy Birthday To You!" message
def show_birthday_title():
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.goto(0, 100)
    title_turtle.color("white")
    title_turtle.pendown()
    title_turtle.write("Happy Birthday To You!", font=("Verdana", 16, "normal"), align="center")
    time.sleep(3)  # Keep the message for 3 seconds
    title_turtle.clear()  # Clear the title before showing messages

# Setup the turtle screen
bg = turtle.Screen()
bg.bgcolor("black")
turtle.speed(1)

# Play the music automatically
play_music()

# Execute the turtle drawings automatically
# Start with the original turtle drawing code
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(330)

turtle.penup()
turtle.goto(-160, -150)
turtle.color("white")
turtle.pendown()
turtle.forward(305)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("white")
turtle.pendown()
turtle.forward(280)

turtle.penup()
turtle.goto(-72, -90)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Light candles
light_candle()

# Fly balloons
fly_balloons()

# Show the "Happy Birthday To You!" message first
show_birthday_title()

# Define the messages to show in sequence
messages = [
    "Today is...",
    "as beautiful as other days",
    "but you realize",
    "another year has gone",
    "in a blink of the eyes",
    "however...",
    "Do you know..?",
    "today is just special",
    "so special to you",
    "that's why...",
    "Let's make it...",
    "the best celebration ever",
    "and let me share...",
    "a piece of happiness to you",
    "I made all this...",
    "as a birthday present to you",
    "thanks for being there",
    "thanks for the friendship we made",
    "thanks for everything",
    "I wish you all the best",
    "May your life be at ease",
    "May all your wishes come true",
    "Happy Birthday Xola Mathembisa!"
]

# Show rotating messages above the cake after the title disappears
show_message(messages)

# Hide the turtle
turtle.hideturtle()

# Keep the turtle screen open
bg.mainloop()
