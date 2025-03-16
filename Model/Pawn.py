from Model.Piece import Piece

class Pawn(Piece):
    def get_valid_moves(self, board):
        """
        Trả về danh sách nước đi hợp lệ của quân Pawn.
        - Có thể tiến về phía trước 1 ô.
        - Có thể đi chéo 1 ô để tấn công quân địch.
        - Không thể đi lùi.

        :param board: Trạng thái bàn cờ (9x9)
        :return: Danh sách các nước đi hợp lệ [(new_x, new_y), ...]
        """
        moves = []
        direction = 1 if self.player == 1 else -1  # Player 1 đi xuống, Player 2 đi lên

        # Đi thẳng về phía trước nếu ô phía trước trống
        new_x, new_y = self.x, self.y + direction
        if 0 <= new_y < 9 and board[new_y][new_x] is None:
            moves.append((new_x, new_y))

        # Đi chéo để tấn công (nếu có quân đối phương)
        for dx in [-1, 1]:  # Chéo trái hoặc chéo phải
            new_x, new_y = self.x + dx, self.y + direction
            if 0 <= new_x < 9 and 0 <= new_y < 9:
                if board[new_y][new_x] is not None and board[new_y][new_x].player != self.player:
                    moves.append((new_x, new_y))

        return moves