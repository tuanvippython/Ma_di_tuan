def is_valid_move(x, y, sol, N):
    """
    Kiểm tra nước đi có hợp lệ hay không
    """
    return x >= 0 and y >= 0 and x < N and y < N and sol[x][y] == -1


def print_solution(sol):
    """
    In ra ma trận giải pháp
    """
    for row in sol:
        print(row)


def solve_knight_tour(N):
    """
    Tìm giải pháp cho bài toán mã đi tuần bằng backtracking
    """
    # Khởi tạo ma trận giải pháp
    sol = [[-1 for _ in range(N)] for _ in range(N)]

    # Khởi tạo vị trí bắt đầu là (0, 0)
    sol[0][0] = 0

    # Khởi tạo 2 mảng lưu tọa độ các bước đi của mã
    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    # Bắt đầu tìm kiếm giải pháp
    if not solve_knight_tour_util(0, 0, 1, sol, x_move, y_move, N):
        print("Không tìm thấy giải pháp")
    else:
        print_solution(sol)


def solve_knight_tour_util(x, y, move_num, sol, x_move, y_move, N):
    """
    Hàm đệ quy để tìm kiếm giải pháp
    """
    # Kiểm tra xem đã đi hết các ô trên bàn cờ chưa
    if move_num == N * N:
        return True

    # Duyệt qua các bước đi của mã
    for i in range(8):
        next_x = x + x_move[i]
        next_y = y + y_move[i]

        # Kiểm tra nước đi có hợp lệ hay không
        if is_valid_move(next_x, next_y, sol, N):
            # Đánh dấu ô hiện tại là đã đi qua
            sol[next_x][next_y] = move_num

            # Gọi đệ quy để tìm giải pháp tiếp theo
            if solve_knight_tour_util(next_x, next_y, move_num + 1, sol, x_move, y_move, N):
                return True

            # Nếu không tìm thấy giải pháp, trả lại giá trị ban đầu cho ô hiện tại
            sol[next_x][next_y] = -1

    # Nếu không có bước đi nào hợp lệ, trả về False
    return False
n=int(input("Nhập vaò kích cỡ bàn cờ: "))
solve_knight_tour(n)