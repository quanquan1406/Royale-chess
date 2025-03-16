class Piece:
    def __init__(self, x, y, player, piece_type):
        """
        Khởi tạo một quân cờ.

        :param x: Vị trí cột (0-8)
        :param y: Vị trí hàng (0-8)
        :param player: Người chơi sở hữu quân cờ (1 hoặc 2)
        :param piece_type: Loại quân cờ (Pawn, Rook, Bishop, Queen)
        """
        self.x = x
        self.y = y
        self.player = player
        self.piece_type = piece_type

    def get_valid_moves(self, board):
        """
        Trả về danh sách các nước đi hợp lệ của quân cờ.
        (Hàm này sẽ được override bởi các lớp con)

        :param board: Trạng thái bàn cờ (9x9)
        :return: Danh sách các nước đi hợp lệ [(new_x, new_y), ...]
        """
        return []

    def is_valid_move(self, new_x, new_y, board):
        """
        Kiểm tra xem nước đi có hợp lệ không.

        :param new_x: Vị trí cột mới
        :param new_y: Vị trí hàng mới
        :param board: Trạng thái bàn cờ
        :return: True nếu hợp lệ, False nếu không
        """
        return (new_x, new_y) in self.get_valid_moves(board)

    def move(self, new_x, new_y, board):
        """
        Thực hiện di chuyển quân cờ nếu nước đi hợp lệ.

        :param new_x: Vị trí cột mới
        :param new_y: Vị trí hàng mới
        :param board: Trạng thái bàn cờ
        :return: True nếu di chuyển thành công, False nếu không
        """
        if self.is_valid_move(new_x, new_y, board):
            self.x = new_x
            self.y = new_y
            return True
        return False