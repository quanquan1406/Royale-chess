import pygame
from Controller.GameController import GameController

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT = 600, 700
GRID_SIZE = WIDTH // 9
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turn-Based Strategy Game")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load hình ảnh quân cờ
images = {
    "rook_1": pygame.image.load("assets/Blackrook.png"),
    "rook_2": pygame.image.load("assets/Blackrook.png"),
    "bishop_1": pygame.image.load("assets/Blackrook.png"),
    "bishop_2": pygame.image.load("assets/Blackrook.png"),
    "pawn_1": pygame.image.load("assets/Blackrook.png"),
    "pawn_2": pygame.image.load("assets/Blackrook.png"),
    "queen_1": pygame.image.load("assets/Blackrook.png"),
    "queen_2": pygame.image.load("assets/Blackrook.png"),
}

# Resize hình ảnh
for key in images:
    images[key] = pygame.transform.scale(images[key], (GRID_SIZE, GRID_SIZE))

# Khởi tạo game
game = GameController()


def draw_board():
    """Vẽ bàn cờ 9x9"""
    for row in range(9):
        for col in range(9):
            color = WHITE if (row + col) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_pieces():
    """Vẽ quân cờ trên bàn cờ"""
    for row in range(9):
        for col in range(9):
            piece = game.board.grid[row][col]
            if piece:
                key = f"{piece.type}_{piece.player}"
                screen.blit(images[key], (col * GRID_SIZE, row * GRID_SIZE))


def draw_towers():
    """Vẽ tháp chính & tháp phụ bằng hình chữ nhật tạm thời."""
    for tower in game.board.towers:
        if tower.active:  # Chỉ vẽ tháp còn hoạt động
            x, y = tower.position
            color = (255, 0, 0) if tower.tower_type == "main" else (0, 0, 255)  # Đỏ cho tháp chính, xanh cho tháp phụ
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def draw_selection_menu():
    """Vẽ giao diện chọn quân"""
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 100, WIDTH, 100))  # Nền đen
    font = pygame.font.Font(None, 36)
    text = font.render("Chọn quân: 1-Rook  2-Bishop  3-Pawn  4-Queen", True, WHITE)
    screen.blit(text, (20, HEIGHT - 80))


def get_grid_position(mouse_x, mouse_y):
    """Chuyển tọa độ chuột thành vị trí bàn cờ"""
    if mouse_y >= 600:  # Nếu click vào khu vực chọn quân
        return None
    return mouse_x // GRID_SIZE, mouse_y // GRID_SIZE


# Game loop
running = True
selected_piece = None
selected_unit = None  # Để chọn quân khi đặt cờ

while running:
    screen.fill(BLACK)
    draw_board()
    draw_pieces()
    draw_towers()
    draw_selection_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = get_grid_position(*event.pos)

            if y is None:  # Click vào menu chọn quân
                selected_unit = event.pos[0] // (WIDTH // 4)  # Xác định quân cờ theo vị trí
                continue

            if selected_piece:
                if game.move_piece(x, y):
                    selected_piece = None
            else:
                if game.select_piece(x, y):
                    selected_piece = (x, y)

        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                selected_unit = event.key - pygame.K_1  # Chọn quân tương ứng
                print(f"Selected unit: {selected_unit}")

    pygame.display.flip()

pygame.quit()
