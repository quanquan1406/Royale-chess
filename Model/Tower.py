class Tower:
    def __init__(self, player, position, tower_type):
        """
        Khởi tạo một tháp trong trò chơi.

        :param player: Người chơi sở hữu tháp (1 hoặc 2).
        :param position: Vị trí của tháp trên bàn cờ (tuple (x, y)).
        :param tower_type: Loại tháp ('main', 'rook', 'bishop', 'pawn').
        """
        self.player = player  # Người chơi sở hữu tháp
        self.position = position  # Vị trí trên bàn cờ
        self.tower_type = tower_type  # Loại tháp
        self.active = True  # Mặc định tháp chưa bị phá hủy

    def destroy(self):
        """Hủy tháp (đánh dấu là không còn hoạt động)."""
        self.active = False

    def __repr__(self):
        return f"Tower(player={self.player}, type={self.tower_type}, pos={self.position}, active={self.active})"