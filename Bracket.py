# import turtle
#
# # Set up the turtle and screen
# t = turtle.Turtle()
# t.speed(0)
# s = turtle.Screen()
# s.bgcolor('white')
#
# # Define some constants for the bracket dimensions
# BRACKET_WIDTH = 500
# BRACKET_HEIGHT = 800
# MATCH_WIDTH = 100
# MATCH_HEIGHT = 50
#
# # Draw the bracket outline
# t.penup()
# t.goto(-BRACKET_WIDTH/2, BRACKET_HEIGHT/2)
# t.pendown()
# t.goto(-BRACKET_WIDTH/2, -BRACKET_HEIGHT/2)
# t.goto(BRACKET_WIDTH/2, -BRACKET_HEIGHT/2)
# t.goto(BRACKET_WIDTH/2, BRACKET_HEIGHT/2)
# t.goto(-BRACKET_WIDTH/2, BRACKET_HEIGHT/2)
#
# # Draw the first round of matches
# for i in range(8):
#     t.penup()
#     t.goto(-BRACKET_WIDTH/4, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.pendown()
#     t.goto(-BRACKET_WIDTH/4 + MATCH_WIDTH, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.goto(-BRACKET_WIDTH/4 + MATCH_WIDTH, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT - MATCH_HEIGHT/2 - MATCH_HEIGHT)
#     t.goto(-BRACKET_WIDTH/4, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT - MATCH_HEIGHT/2 - MATCH_HEIGHT)
#     t.goto(-BRACKET_WIDTH/4, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT - MATCH_HEIGHT/2)
#
# # Draw the second round of matches
# for i in range(4):
#     t.penup()
#     t.goto(0, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.pendown()
#     t.goto(0 + MATCH_WIDTH, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.goto(0 + MATCH_WIDTH, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT*2 - MATCH_HEIGHT/2)
#     t.goto(0, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT*2 - MATCH_HEIGHT/2)
#     t.goto(0, BRACKET_HEIGHT/2)
#
# # Draw the third round of matches (semi-finals)
# for i in range(2):
#     t.penup()
#     t.goto(BRACKET_WIDTH/4 - MATCH_WIDTH/2, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.pendown()
#     t.goto(BRACKET_WIDTH/4 + MATCH_WIDTH/2, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT - MATCH_HEIGHT/2)
#     t.goto(BRACKET_WIDTH/4 + MATCH_WIDTH/2, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT*2 - MATCH_HEIGHT/2)
#     t.goto(BRACKET_WIDTH/4 - MATCH_WIDTH/2, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT*2 - MATCH_HEIGHT/2)
#     t.goto(BRACKET_WIDTH/4 - MATCH_WIDTH/2, BRACKET_HEIGHT/2 - i*MATCH_HEIGHT*2 - MATCH_HEIGHT - MATCH_HEIGHT/2)
#
# # Draw the final match
# t.penup()
# t.goto(-MATCH_WIDTH/2, 0)
# t.pendown()
# t.goto(MATCH_WIDTH/2, 0)
# t.goto(MATCH_WIDTH/2, -MATCH_HEIGHT)
# t.goto(-MATCH_WIDTH/2, -MATCH_HEIGHT)
# t.goto(-MATCH_WIDTH/2, 0)
#
# # Hide the turtle and keep the window open
# t.hideturtle()
# turtle.mainloop()


# import turtle
#
# # Set up the turtle and screen
# t = turtle.Turtle()
# t.speed(0)
# s = turtle.Screen()
# s.bgcolor('white')
#
# # Define some constants for the bracket dimensions
# BRACKET_WIDTH = 500
# BRACKET_HEIGHT = 800
# MATCH_WIDTH = 100
# MATCH_HEIGHT = 50
#
# # Draw the bracket outline
# t.penup()
# t.goto(-BRACKET_WIDTH / 2, BRACKET_HEIGHT / 2)
# t.pendown()
# t.goto(-BRACKET_WIDTH / 2, -BRACKET_HEIGHT / 2)
# t.goto(BRACKET_WIDTH / 2, -BRACKET_HEIGHT / 2)
# t.goto(BRACKET_WIDTH / 2, BRACKET_HEIGHT / 2)
# t.goto(-BRACKET_WIDTH / 2, BRACKET_HEIGHT / 2)
#
# # Create a list of the countries in the first round of matches
# countries = ['Russia', 'Saudi Arabia', 'Egypt', 'Uruguay', 'Morocco', 'Iran', 'Portugal', 'Spain',
#              'France', 'Australia', 'Argentina', 'Iceland', 'Peru', 'Denmark', 'Croatia', 'Nigeria']
#
# # Draw the first round of matches and display the country names
# for i in range(8):
#     t.penup()
#     t.goto(-BRACKET_WIDTH / 4, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.pendown()
#     t.goto(-BRACKET_WIDTH / 4 + MATCH_WIDTH, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.goto(-BRACKET_WIDTH / 4 + MATCH_WIDTH, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 2 - MATCH_HEIGHT)
#     t.goto(-BRACKET_WIDTH / 4, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 2 - MATCH_HEIGHT)
#     t.goto(-BRACKET_WIDTH / 4, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 2)
#
#     t.penup()
#     t.goto(-BRACKET_WIDTH / 4 - MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT / 4)
#     t.write(countries[i * 2], align='center', font=('Arial', 16, 'normal'))
#     t.goto(-BRACKET_WIDTH / 4 + MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT - MATCH_HEIGHT/4)
#
# # Draw the second round of matches and display the country names
# for i in range(4):
#     t.penup()
#     t.goto(0, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.pendown()
#     t.goto(0 + MATCH_WIDTH, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.goto(0 + MATCH_WIDTH, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT * 2 - MATCH_HEIGHT / 2)
#     t.goto(0, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT * 2 - MATCH_HEIGHT / 2)
#     t.goto(0, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#
#     t.penup()
#     t.goto(-MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT / 4)
#     t.write(countries[i * 4 + 2], align='center', font=('Arial', 16, 'normal'))
#     t.goto(MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT / 4)
#     t.write(countries[i * 4 + 3], align='center', font=('Arial', 16, 'normal'))
#
# # Draw the third round of matches (semi-finals) and display the country names
# for i in range(2):
#     t.penup()
#     t.goto(BRACKET_WIDTH / 4 - MATCH_WIDTH / 2,
#            BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.pendown()
#     t.goto(BRACKET_WIDTH / 4 + MATCH_WIDTH / 2,
#            BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#     t.goto(BRACKET_WIDTH / 4 + MATCH_WIDTH / 2,
#            BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT * 2 - MATCH_HEIGHT / 2)
#     t.goto(BRACKET_WIDTH / 4 - MATCH_WIDTH / 2,
#            BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT * 2 - MATCH_HEIGHT / 2)
#     t.goto(BRACKET_WIDTH / 4 - MATCH_WIDTH / 2,
#            BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT - MATCH_HEIGHT / 2)
#
#     t.penup()
#     t.goto(BRACKET_WIDTH / 4 - MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT / 4)
#     t.write(countries[i * 4 + 4], align='center', font=('Arial', 16, 'normal'))
#     t.goto(BRACKET_WIDTH / 4 + MATCH_WIDTH / 2, BRACKET_HEIGHT / 2 - i * MATCH_HEIGHT * 2 - MATCH_HEIGHT / 4)
#     t.write(countries[i*4 + 4], align='center', font=('Arial', 16, 'normal'))
#
# # Draw the final match and display the country names
# t.penup()
# t.goto(-MATCH_WIDTH/2, 0)
# t.pendown()
# t.goto(MATCH_WIDTH/2, 0)
# t.goto(MATCH_WIDTH/2, -MATCH_HEIGHT)
# t.goto(-MATCH_WIDTH/2, -MATCH_HEIGHT)
# t.goto(-MATCH_WIDTH/2, 0)
#
# t.penup()
# t.goto(-MATCH_WIDTH/2, -MATCH_HEIGHT/4)
# t.write(countries[6], align='center', font=('Arial', 16, 'normal'))
# t.goto(MATCH_WIDTH/2, -MATCH_HEIGHT/4)
# t.write(countries[7], align='center', font=('Arial', 16, 'normal'))
#
# # Hide the turtle and keep the window open
# t.hideturtle()
# turtle.mainloop()


