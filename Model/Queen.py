from Model.Piece import Piece

class Queen(Piece):
    def get_valid_moves(self, board):
        """
        Trả về danh sách nước đi hợp lệ của quân Queen.
        - Di chuyển như Rook (1 ô ngang hoặc dọc, không thể đi lùi).
        - Di chuyển như Bishop (1 ô chéo hoặc ngang, không thể đi lùi).
        - Di chuyển như Pawn (tiến thẳng hoặc chéo để tấn công, không thể đi lùi).

        :param board: Trạng thái bàn cờ (9x9)
        :return: Danh sách các nước đi hợp lệ [(new_x, new_y), ...]
        """
        moves = []
        direction = 1 if self.player == 1 else -1  # Player 1 đi xuống, Player 2 đi lên

        # Giống Rook: Di chuyển ngang & dọc 1 ô (không lùi)
        for dx, dy in [(1, 0), (-1, 0), (0, direction)]:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < 9 and 0 <= new_y < 9:
                if board[new_y][new_x] is None or board[new_y][new_x].player != self.player:
                    moves.append((new_x, new_y))

        # Giống Bishop: Di chuyển chéo 1 ô hoặc ngang (không lùi)
        for dx, dy in [(1, direction), (-1, direction), (1, 0), (-1, 0)]:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < 9 and 0 <= new_y < 9:
                if board[new_y][new_x] is None or board[new_y][new_x].player != self.player:
                    moves.append((new_x, new_y))

        return moves