from datetime import datetime


class Account:
    def __init__(self):
        self.ten = ""
        self.sodu = 0.0
        self.lich_su = []

    def nhap_du_lieu(self):
        self.ten = input("Nhập tên chủ tài khoản: ").strip()
        while True:
            try:
                self.sodu = float(input("Nhập số dư ban đầu: "))
                if self.sodu < 0:
                    print("Số dư không được âm!")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập số!")

    def gui_tien(self):
        try:
            so_tien = float(input("Nhập số tiền cần gửi: "))
        except ValueError:
            print("Số tiền không hợp lệ!")
            return

        if so_tien <= 0:
            print("Số tiền gửi phải > 0!")
            return

        self.sodu += so_tien
        self.lich_su.append(
            {"loai": "Gửi tiền", "so_tien": so_tien, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        print(f"Gửi tiền thành công. Số dư: {self.sodu:,.0f} VND")

    def rut_tien(self):
        try:
            so_tien = float(input("Nhập số tiền cần rút: "))
        except ValueError:
            print("Số tiền không hợp lệ!")
            return

        if so_tien <= 0:
            print("Số tiền rút phải > 0!")
            return

        if so_tien > self.sodu:
            print("Số dư không đủ!")
            return

        self.sodu -= so_tien
        self.lich_su.append(
            {"loai": "Rút tiền", "so_tien": so_tien, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        )
        print(f"Rút tiền thành công. Số dư: {self.sodu:,.0f} VND")

    def xem_so_du(self):
        print(f"Số dư hiện tại: {self.sodu:,.0f} VND")

    def xem_lich_su(self):
        if len(self.lich_su) == 0:
            print("Chưa có giao dịch nào!")
            return

        print("\nLỊCH SỬ GIAO DỊCH")
        for i, gd in enumerate(self.lich_su, 1):
            print(f"{i}. {gd['loai']} - {gd['so_tien']:,.0f} VND - {gd['time']}")


def menu_giao_dich(tk: Account):
    while True:
        print("\n2. Giao dịch")
        print("a. Gửi tiền")
        print("b. Rút tiền")
        print("c. Xem số dư")
        print("d. Xem lịch sử giao dịch")
        print("e. Quay về")

        chon = input("Chọn (a/b/c/d/e): ").strip().lower()
        if chon == "a":
            tk.gui_tien()
        elif chon == "b":
            tk.rut_tien()
        elif chon == "c":
            tk.xem_so_du()
        elif chon == "d":
            tk.xem_lich_su()
        elif chon == "e":
            break
        else:
            print("Lựa chọn không hợp lệ!")


def main():
    tk = None

    while True:
        print("1. Tạo tài khoản")
        print("2. Giao dịch")
        print("3. Kết thúc")

        chon = input("Chọn (1/2/3): ").strip()

        if chon == "1":
            tk = Account()
            tk.nhap_du_lieu()
            print("Tạo tài khoản thành công!")

        elif chon == "2":
            if tk is None:
                print("Bạn chưa tạo tài khoản. Hãy chọn 1 trước!")
            else:
                menu_giao_dich(tk)

        elif chon == "3":
            print("Kết thúc!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()