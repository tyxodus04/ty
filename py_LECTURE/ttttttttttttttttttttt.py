import pygame
import sys
import random

# 초기화
pygame.init()

# 게임 창 설정
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Puzzle Game")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 퍼즐 조각의 크기 및 간격 설정
piece_size = 100
piece_margin = 5

# 퍼즐 조각의 개수 설정
rows = 3
cols = 3

# 퍼즐 조각의 초기 위치 설정
pieces = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 이동 가능한 방향
valid_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 퍼즐을 섞기
def shuffle():
    for i in range(1000):
        move = random.choice(valid_moves)
        move_piece(*move)

# 빈 공간 찾기
def find_blank():
    for i in range(rows):
        for j in range(cols):
            if pieces[i][j] == 8:
                return i, j

# 조각 이동
def move_piece(row, col):
    blank_row, blank_col = find_blank()
    if 0 <= row + blank_row < rows and 0 <= col + blank_col < cols:
        pieces[blank_row][blank_col], pieces[blank_row + row][blank_col + col] = pieces[blank_row + row][blank_col + col], pieces[blank_row][blank_col]

# 게임 루프
shuffle()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_piece(0, 1)
            elif event.key == pygame.K_RIGHT:
                move_piece(0, -1)
            elif event.key == pygame.K_UP:
                move_piece(1, 0)
            elif event.key == pygame.K_DOWN:
                move_piece(-1, 0)

    # 화면 그리기
    screen.fill(white)
    for i in range(rows):
        for j in range(cols):
            if pieces[i][j] == 8:  # 빈 조각은 그리지 않음
                continue
            pygame.draw.rect(screen, black, (j * (piece_size + piece_margin), i * (piece_size + piece_margin), piece_size, piece_size))
            font = pygame.font.Font(None, 36)
            text = font.render(str(pieces[i][j] + 1), True, white)
            screen.blit(text, (j * (piece_size + piece_margin) + piece_size / 2 - 15, i * (piece_size + piece_margin) + piece_size / 2 - 15))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
