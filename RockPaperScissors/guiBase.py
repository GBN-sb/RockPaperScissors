import pygame
import os
import time
import random
import linecache
import re
# variables

# screen
height = 400
width = 800
size = [width, height]
screen = pygame.display.set_mode(size)

bgColour = [0, 0, 0]
bgColour2 = [0, 255, 0]

fps = 60
# ----------------------------------------------------------------------------

# Headings
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 40)

label = myfont.render("Rock, Paper, Scissors!", True, (255, 255, 255))
labelRect = label.get_rect()
labelRect.center = (width // 2, height // 9)

labelUser = myfont.render("Rock, Paper, Scissors!", True, (255, 255, 255))
labelRect = label.get_rect()
labelRect.center = (width // 2, height // 9)
# ----------------------------------------------------------------------------

# images
image_pos_height = 270
image_height = 100
image_width = 100
ROCK_IMAGE = pygame.image.load(os.path.join('Assets', 'rock.png'))
ROCK = pygame.transform.scale(ROCK_IMAGE, (image_width, image_height))
PAPER_IMAGE = pygame.image.load(os.path.join('Assets', 'paper.png'))
PAPER = pygame.transform.scale(PAPER_IMAGE, (image_width, image_height))
SCISSOR_IMAGE = pygame.image.load(os.path.join('Assets', 'scissor.png'))
SCISSOR = pygame.transform.scale(SCISSOR_IMAGE, (image_width, image_height))
# ----------------------------------------------------------------------------

# Button displays
button_width = 75
button_height = 25
button_pos_width = 25
colour = (128, 128, 128)
myfontFour = pygame.font.SysFont("Monospace", 16)
save_heading = myfontFour.render("Save", True, (255, 255, 255))
save_heading_rect = save_heading.get_rect()
save_heading_rect = (button_pos_width + 15, 322)
load_heading = myfontFour.render("Load", True, (255, 255, 255))
load_heading_rect = load_heading.get_rect()
load_heading_rect = (button_pos_width + 15, 362)
# -----------------------------------------------------------------------------

# display result
user = None
list = ["Rock", "Paper", "Scissor"]
myfontTwo = pygame.font.SysFont("monospace", 35)
resultLabel = myfontTwo.render("", True, (255, 255, 255))
resultLabelRect = resultLabel.get_rect()


def result(run, user, resultLabel, resultLabelRect, userScore, computerScore):

    computer = list[random.randint(0, 2)]
    if computer == user:
        resultVar = "Draw: pick again"
        draw_result(resultVar, resultLabel, resultLabelRect,
                    userScore, computerScore)
        return(resultLabel, resultLabelRect)
    else:
        resultVar = checkWinner(user, computer)
        draw_result(resultVar, resultLabel, resultLabelRect,
                    userScore, computerScore)
        return(resultVar)


def checkWinner(user, computer):
    winner = ""
    if user == "Rock" and computer == "Scissor":
        winner = "user"
        return("User Wins")
    elif user == "Scissor" and computer == "Paper":
        winner = "user"
        return("User Wins")
    elif user == "Paper" and computer == "Rock":
        winner = "user"
        return("User Wins")
    else:
        winner = "computer"
        return("Computer Wins")


def draw_result(resultVar, resultLabel, resultLabelRect, userScore, computerScore):
    resultLabel = myfontTwo.render(resultVar, True, (255, 255, 255))
    resultLabelRect = resultLabel.get_rect()
    resultLabelRect.center = (width // 2, height // 2)
    draw_window(resultLabel, resultLabelRect, userScore, computerScore)
# ----------------------------------------------------------------------------


# Scores
myfontThree = pygame.font.SysFont("Monospace", 20)

user_heading = myfontThree.render("User", True, (255, 255, 255))
user_heading_rect = user_heading.get_rect()
user_heading_rect = (40, 50)

computer_heading = myfontThree.render("Computer", True, (255, 255, 255))
computer_heading_rect = computer_heading.get_rect()
computer_heading_rect = (680, 50)


def print_score(userScore, computerScore):
    user_score_heading = myfontThree.render(
        str(userScore), True, (255, 255, 255))
    user_score_heading_rect = user_score_heading.get_rect()
    user_score_heading_rect = (57, 75)
    screen.blit(user_score_heading, user_score_heading_rect)
    computer_score_heading = myfontThree.render(
        str(computerScore), True, (255, 255, 255))
    computer_score_heading_rect = computer_score_heading.get_rect()
    computer_score_heading_rect = (720, 75)
    screen.blit(computer_score_heading, computer_score_heading_rect)
# ----------------------------------------------------------------------------

# Load/save


def save_score(userScore, computerScore):
    new_file = "newSave.txt"
    with open(new_file, 'w') as f:
        # new line
        f.write(str(userScore) + "\n" + str(computerScore))


def load_user_score():
    file = "newsave.txt"
    temp = linecache.getline(file, 1)
    # removes the save formatting
    temp = re.sub('[\W_]+', '', temp)
    print(temp)
    return int(temp)


def load_computer_score():
    file = "newsave.txt"
    temp = linecache.getline(file, 2)
    temp = re.sub('[\W_]+', '', temp)
    print(temp)
    return int(temp)
# ----------------------------------------------------------------------------

# Window


def draw_window(resultLabel, resultLabelRect, userScore, computerScore):
    screen.fill(bgColour)
    screen.blit(user_heading, user_heading_rect)
    screen.blit(resultLabel, resultLabelRect)
    screen.blit(computer_heading, computer_heading_rect)
    pygame.draw.rect(screen, colour, pygame.Rect(
        button_pos_width, 360, button_width, button_height))
    pygame.draw.rect(screen, colour, pygame.Rect(
        button_pos_width, 320, button_width, button_height))
    screen.blit(save_heading, save_heading_rect)
    screen.blit(load_heading, load_heading_rect)
    print_score(userScore, computerScore)
    screen.blit(label, labelRect)
    screen.blit(ROCK, (150, image_pos_height))
    screen.blit(PAPER, (360, image_pos_height))
    screen.blit(SCISSOR, (600, image_pos_height))
    pygame.display.update()
# ----------------------------------------------------------------------------

# Collisions


def image_collison_rock(ROCK):
    ROCK = pygame.Rect(image_width, image_width,
                       image_height, image_height)
    ROCK.x = 150
    ROCK.y = image_pos_height
    return(ROCK)


def image_collison_paper(PAPER):
    PAPER = pygame.Rect(image_width, image_width,
                        image_height, image_height)
    PAPER.x = 360
    PAPER.y = image_pos_height
    return(PAPER)


def image_collison_scissor(SCISSOR):
    SCISSOR = pygame.Rect(image_width, image_width,
                          image_height, image_height)
    SCISSOR.x = 600
    SCISSOR.y = image_pos_height
    return(SCISSOR)


def save_collision(save_heading):
    save_heading = pygame.Rect(
        button_pos_width, 360, button_width, button_height)
    save_heading.x = button_pos_width
    save_heading.y = 322
    return(save_heading)


def load_collision(load_heading):
    load_heading = pygame.Rect(
        button_pos_width, 320, button_width, button_height)
    load_heading.x = button_pos_width
    load_heading.y = 362
    return(load_heading)
# ----------------------------------------------------------------------------

# Main


def main():
    clock = pygame.time.Clock()
    run = True
    userScore = 0
    computerScore = 0
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            draw_window(resultLabel, resultLabelRect, userScore, computerScore)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if image_collison_rock(ROCK).collidepoint(mouse_pos):
                user = "Rock"
                print('rock was pressed')
                temp = result(run, user, resultLabel, resultLabelRect,
                              userScore, computerScore)
                if temp == "User Wins":
                    userScore += 1
                elif temp == "Computer Wins":
                    computerScore += 1
                # ensures mouse only clicks once
                time.sleep(1)
            if image_collison_paper(PAPER).collidepoint(mouse_pos):
                user = "Paper"
                print('paper was pressed')
                temp = result(run, user, resultLabel, resultLabelRect,
                              userScore, computerScore)
                if temp == "User Wins":
                    userScore += 1
                elif temp == "Computer Wins":
                    computerScore += 1
                time.sleep(1)
            if image_collison_scissor(SCISSOR).collidepoint(mouse_pos):
                user = "Scissor"
                print('scissor was pressed')
                temp = result(run, user, resultLabel, resultLabelRect,
                              userScore, computerScore)
                if temp == "User Wins":
                    userScore += 1
                elif temp == "Computer Wins":
                    computerScore += 1
                time.sleep(1)
            if save_collision(save_heading).collidepoint(mouse_pos):
                print("save")
                save_score(userScore, computerScore)
                time.sleep(1)
            if load_collision(load_heading).collidepoint(mouse_pos):
                print("load")
                userScore = load_user_score()
                computerScore = load_computer_score()
                time.sleep(1)
    pygame.quit()


if __name__ == '__main__':
    main()
