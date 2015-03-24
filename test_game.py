from random import randint
import pygame
import sys
from game.game_map import GameMap
from game.monster import Monster
from game.player_character import PlayerCharacter

__author__ = 'TriD'

pygame.init()
screen = pygame.display.set_mode((800, 600))

game_map = GameMap()
player_character = PlayerCharacter()
monster = Monster()
game_state = 'running'
last_tick = pygame.time.get_ticks()
monster_update = 0
font = pygame.font.SysFont('monospace', 48)
label_win = font.render("You Win", 1, (255, 0, 0))
label_lose = font.render("You Lose", 1, (255, 0, 0))


def init_level():
    global map_file, line, player_x, player_y, monster_x, monster_y
    with open('res/maps/map.txt') as map_file:
        while True:
            line = map_file.readline()
            if line == '\n':
                break
            game_map.map_data.append(list(line))
        player_x, player_y = map_file.readline().split(',')
        player_character.x, player_character.y = int(player_x), int(player_y)
        monster_x, monster_y = map_file.readline().split(',')
        monster.x, monster.y = int(monster_x), int(monster_y)


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYUP and game_state == 'running':
            if event.key == pygame.K_LEFT:
                if game_map.map_data[player_character.y][player_character.x - 1] != '1':
                    player_character.x -= 1
            if event.key == pygame.K_RIGHT:
                if game_map.map_data[player_character.y][player_character.x + 1] != '1':
                    player_character.x += 1
            if event.key == pygame.K_UP:
                if game_map.map_data[player_character.y - 1][player_character.x] != '1':
                    player_character.y -= 1
            if event.key == pygame.K_DOWN:
                if game_map.map_data[player_character.y + 1][player_character.x] != '1':
                    player_character.y += 1


def monster_can_move():
    can_move = False
    can_move = can_move or (game_map.map_data[monster.y][monster.x - 1] != '1')
    can_move = can_move or (game_map.map_data[monster.y][monster.x + 1] != '1')
    can_move = can_move or (game_map.map_data[monster.y - 1][monster.x] != '1')
    can_move = can_move or (game_map.map_data[monster.y + 1][monster.x] != '1')
    return can_move


def move_monster():
    global monster_update
    global last_tick
    current_tick = pygame.time.get_ticks()
    monster_update += current_tick - last_tick
    last_tick = current_tick
    if monster_update < 1000:
        return

    monster_update -= 1000
    moved = False

    # Just assume that monster is locked and we don't want to stuck here
    if not monster_can_move():
        return
    while not moved:
        i = randint(0, 4)
        if i == 0 and game_map.map_data[monster.y][monster.x - 1] != '1':
            monster.x -= 1
            moved = True
        elif i == 1 and game_map.map_data[monster.y][monster.x + 1] != '1':
            monster.x += 1
            moved = True
        elif i == 2 and game_map.map_data[monster.y - 1][monster.x] != '1':
            monster.y -= 1
            moved = True
        elif i == 3 and game_map.map_data[monster.y + 1][monster.x] != '1':
            monster.y += 1
            moved = True


def check_status():
    global game_state
    if game_map.map_data[player_character.y][player_character.x] == '3':
        game_state = 'win'
    if player_character.x == monster.x and player_character.y == monster.y:
        game_state = 'lose'


def draw():
    game_map.draw(screen)
    if game_state == 'win':
        screen.blit(label_win, (0, 0))
    if game_state == 'lose':
        screen.blit(label_lose, (0, 0))
    player_character.draw(screen)
    monster.draw(screen)
    pygame.display.flip()


init_level()

while True:
    screen.fill((0, 0, 0))
    process_events()
    if game_state == 'running':
        move_monster()
        check_status()
    draw()