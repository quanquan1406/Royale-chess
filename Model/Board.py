from Model.Tower import Tower

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(9)]

        # Danh sách tháp (mỗi người chơi có 1 tháp chính + 3 tháp phụ)
        self.towers = [
            Tower(1, (4, 0), "main"),  # Tháp chính của Player 1
            Tower(1, (2, 0), "rook"),
            Tower(1, (4, 1), "bishop"),
            Tower(1, (6, 0), "pawn"),

            Tower(2, (4, 8), "main"),  # Tháp chính của Player 2
            Tower(2, (2, 8), "rook"),
            Tower(2, (4, 7), "bishop"),
            Tower(2, (6, 8), "pawn")
        ]

    def place_piece(self, piece, x, y):
        """
        Đặt một quân cờ vào vị trí (x, y) nếu ô trống.
        """
        if self.grid[y][x] is None:
            self.grid[y][x] = piece
            piece.x, piece.y = x, y
            return True
        return False  # Không thể đặt nếu ô đã có quân

    def move_piece(self, piece, new_x, new_y):
        """
        Di chuyển quân cờ từ vị trí hiện tại đến vị trí mới nếu hợp lệ.
        """
        valid_moves = piece.get_valid_moves(self.grid)
        if (new_x, new_y) in valid_moves:
            self.grid[piece.y][piece.x] = None  # Xóa vị trí cũ
            if self.grid[new_y][new_x] is not None:  # Nếu có quân đối phương
                captured_piece = self.grid[new_y][new_x]
                self.remove_piece(captured_piece)
            self.grid[new_y][new_x] = piece  # Di chuyển quân
            piece.x, piece.y = new_x, new_y
            return True
        return False

    def remove_piece(self, piece):
        """
        Loại bỏ quân cờ khỏi bàn.
        """
        self.grid[piece.y][piece.x] = None
        if piece.name in self.towers[piece.player]:  # Nếu là tháp
            self.towers[piece.player][piece.name] = False  # Mất quyền đặt quân đó

    def is_tower_destroyed(self, player):
        """
        Kiểm tra nếu tất cả tháp phụ của người chơi bị hạ.
        """
        return all(not status for status in self.towers[player].values())

    def is_game_over(self):
        """
        Kiểm tra điều kiện thắng:
        - Nếu một người chơi không còn quân trên bàn & tất cả tháp phụ bị hạ -> Thua.
        - Nếu tháp chính bị hạ -> Thua.
        """
        player_1_alive = any(piece for row in self.grid for piece in row if piece and piece.player == 1)
        player_2_alive = any(piece for row in self.grid for piece in row if piece and piece.player == 2)

        if not player_1_alive and self.is_tower_destroyed(1):
            return 2  # Player 2 thắng
        if not player_2_alive and self.is_tower_destroyed(2):
            return 1  # Player 1 thắng

        return None  # Chưa kết thúc