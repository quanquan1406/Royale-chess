import pygame
from Model.Board import Board
from Model.Rook import Rook
from Model.Bishop import Bishop
from Model.Pawn import Pawn
from Model.Queen import Queen


class GameController:
    def __init__(self):
        """
        Khởi tạo game controller:
        - Bàn cờ 9x9
        - Lượt chơi (player 1 bắt đầu)
        - Danh sách quân cờ của mỗi người chơi
        - Kiểm tra trạng thái phase (di chuyển / đặt quân)
        """
        self.board = Board()
        self.current_player = 1  # Người chơi 1 đi trước
        self.phase = "move"  # Phase đầu tiên là di chuyển
        self.selected_piece = None  # Quân cờ đang chọn

    def select_piece(self, x, y):
        """
        Chọn quân cờ để di chuyển.
        """
        piece = self.board.grid[y][x]
        if piece and piece.player == self.current_player:
            self.selected_piece = piece
            return True
        return False

    def move_piece(self, x, y):
        """
        Di chuyển quân cờ nếu hợp lệ.
        """
        if self.selected_piece:
            if self.board.move_piece(self.selected_piece, x, y):
                self.selected_piece = None
                return True
        return False

    def place_piece(self, piece_type, x, y):
        """
        Đặt quân cờ mới trên bàn cờ (chỉ trong phase đặt quân).
        """
        if self.phase == "place":
            if piece_type == "rook" and self.board.towers[self.current_player]["rook"]:
                piece = Rook(x, y, self.current_player, "rook")
            elif piece_type == "bishop" and self.board.towers[self.current_player]["bishop"]:
                piece = Bishop(x, y, self.current_player, "bishop")
            elif piece_type == "pawn" and self.board.towers[self.current_player]["pawn"]:
                piece = Pawn(x, y, self.current_player, "pawn")
            elif piece_type == "queen" and not hasattr(self, "queen_placed"):
                piece = Queen(x, y, self.current_player, "queen")
                self.queen_placed = True
            else:
                return False  # Không thể đặt quân này

            if self.board.place_piece(piece, x, y):
                self.end_turn()
                return True
        return False

    def end_turn(self):
        """
        Kết thúc lượt, chuyển phase hoặc đổi người chơi.
        """
        if self.phase == "move":
            self.phase = "place"
        else:
            self.phase = "move"
            self.current_player = 3 - self.current_player  # Đổi lượt chơi

    def check_game_over(self):
        """
        Kiểm tra điều kiện thắng.
        """
        winner = self.board.is_game_over()
        if winner:
            print(f"Player {winner} wins!")
            return True
        return False