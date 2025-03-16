# 🎭 Royale Chess - Turn-based Strategy Game  

## 🏰 Giới Thiệu  
**Royale Chess** là một trò chơi chiến thuật theo lượt dành cho hai người chơi, diễn ra trên **bàn cờ 9x9**.  
Mỗi người chơi điều khiển một đội quân gồm **ba tháp phụ** (Rook, Bishop, Pawn) và **một tháp chính**.  
Người chơi cần khéo léo sử dụng quân cờ để **kiểm soát bàn cờ, tiêu diệt quân đối phương và bảo vệ căn cứ của mình**.  

---

## 🎯 Mục Tiêu  
**Chiến thắng khi thỏa mãn một trong hai điều kiện sau:**  
1. **Đối phương không còn khả năng chiến đấu**  
   - **Tất cả 3 tháp phụ + Queen bị hạ**  
   - **Trên bàn cờ không còn quân nào của họ**  

2. **Tháp chính của đối phương bị hạ**  

---

## 🏁 Cách Chơi  

### 📌 1. Bố Cục Bàn Cờ  
- **Bàn cờ 9x9**, mỗi người chơi có **một tháp chính ở giữa hàng cuối** và **ba tháp phụ đặt ở vị trí chiến lược**.  
- **Hai người chơi được phân biệt bằng màu sắc:**  
  - **Người chơi 1 (Player 1)** – 🔵 *Màu Xanh*  
  - **Người chơi 2 (Player 2)** – 🔴 *Màu Đỏ*  

---

### 📌 2. Các Loại Quân Cờ & Luật Di Chuyển  
Mỗi người chơi có **3 loại quân** được đặt từ **tháp phụ tương ứng** và **một quân Queen đặc biệt**:  

| **Quân Cờ** | **Tháp Phụ** | **Luật Di Chuyển** | **Lưu Ý** |
|-------------|-------------|--------------------|-----------|
| **Rook (Xe)** | Tháp 1 | Tiến 1 ô ngang hoặc dọc, không thể đi lùi | Quân cờ tấn công trực diện, kiểm soát bàn cờ |
| **Bishop (Tượng)** | Tháp 2 | Tiến 1 ô chéo hoặc ngang, không thể đi lùi | Đa dụng hơn Rook, có thể lách qua quân địch |
| **Pawn (Tốt)** | Tháp 3 | Tiến 1 ô thẳng hoặc chéo | Đơn vị cơ bản, dễ triển khai |
| **Queen (Hậu)** | Chỉ được đặt 1 lần duy nhất | Di chuyển như Rook + Bishop + Pawn, không thể đi lùi | Lá bài chiến thuật quan trọng |

---

### 📌 3. Luật Chơi  

#### 🔹 **Mỗi lượt, người chơi có 2 giai đoạn (Phase):**  

#### **Phase 1: Di Chuyển**  
- **Bắt buộc phải di chuyển ít nhất một quân cờ nếu có thể.**  
- **Nếu không có quân nào trên bàn, bỏ qua Phase 1.**  
- Nếu quân cờ di chuyển vào **ô có quân địch**, **quân địch bị loại khỏi bàn cờ**.  
- Nếu quân cờ di chuyển vào **tháp đối phương**, **tháp đó bị hạ gục** và đối phương **mất quyền đặt quân từ tháp đó**.  

#### **Phase 2: Đặt Quân**  
- **Người chơi có thể đặt một quân mới** từ **tháp chưa bị phá hủy**.  
- **Quân cờ chỉ được đặt ở hàng cuối của người chơi**.  
- **Queen chỉ được đặt một lần duy nhất trong suốt trò chơi**.  

---

### 📌 4. Điều Kiện Thắng  
**Trò chơi kết thúc khi một trong hai điều kiện sau xảy ra:**  

1. **Một người chơi không còn khả năng chiến đấu:**  
   - **3 tháp phụ + Queen bị phá hủy**.  
   - **Không còn quân cờ nào trên bàn**.  

2. **Tháp chính bị hạ:**  
   - **Bất kỳ quân cờ nào di chuyển vào vị trí của tháp chính đối phương**, người chơi đó **thắng ngay lập tức**.  

---

🚀 **Sẵn sàng chiến đấu & thể hiện chiến thuật của bạn!** ♟️🔥  
