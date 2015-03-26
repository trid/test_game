from random import randint
import pygame
import sys
from game.game_map import GameMap
from game.monster import Monster
from game.player_character import PlayerCharacter
from game.video import Video

__author__ = 'TriD'


video = Video()
game_map = GameMap()
player_character = PlayerCharacter()
monster = Monster()
game_state = 'running'
last_tick = pygame.time.get_ticks()
monster_update = 0
next_level = None


def init_level(level_name):
    global map_file, next_level, game_map
    game_map.map_data = []
    with open('res/maps/' + level_name) as map_file:
        while True:
            line = map_file.readline()
            if line == '\n':
                break
            game_map.map_data.append(list(line))
        player_x, player_y = map_file.readline().split(',')
        player_character.x, player_character.y = int(player_x), int(player_y)
        monster_x, monster_y = map_file.readline().split(',')
        monster.x, monster.y = int(monster_x), int(monster_y)
        map_file.readline()
        next_level = map_file.readline()


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
        if next_level:
            init_level(next_level)
        else:
            game_state = 'win'
    if player_character.x == monster.x and player_character.y == monster.y:
        game_state = 'lose'


video.drawing_objects.append(game_map)
video.drawing_objects.append(player_character)
video.drawing_objects.append(monster)

init_level('map.txt')

while True:
    process_events()
    if game_state == 'running':
        move_monster()
        check_status()
    video.game_state = game_state
    video.draw()