from Model.Piece import Piece

class Bishop(Piece):
    def get_valid_moves(self, board):
        """
        Trả về danh sách nước đi hợp lệ của quân Bishop.
        - Di chuyển 1 ô theo đường chéo hoặc ngang.
        - Không thể đi lùi.

        :param board: Trạng thái bàn cờ (9x9)
        :return: Danh sách các nước đi hợp lệ [(new_x, new_y), ...]
        """
        moves = []
        direction = 1 if self.player == 1 else -1  # Player 1 đi xuống, Player 2 đi lên

        # Di chuyển chéo
        for dx in [-1, 1]:
            new_x, new_y = self.x + dx, self.y + direction
            if 0 <= new_x < 9 and 0 <= new_y < 9 and board[new_y][new_x] is None:
                moves.append((new_x, new_y))

        # Di chuyển ngang (trái/phải)
        for dx in [-1, 1]:
            new_x = self.x + dx
            if 0 <= new_x < 9 and board[self.y][new_x] is None:
                moves.append((new_x, self.y))

        return moves