"""
DE: 01
Author: CA20B1_53521_NguyenTanViet
Date: 01/10/2021

Problem:
      Câu 2 (6.0 điểm). Để thực hiện quản lý mặt hàng của một kho hàng, người ta xây dựng một class
                        có tên là MatHang với các thông tin như sau:

Các thuộc tính: mã mặt hàng, tên mặt hàng, số lượng, đơn giá
Các phương thức chính: khởi tạo, sử dụng chỉ thị @properties cho phương thức có tên là thành tiền.
Với: thành tiền = số  lượng * đơn giá

     Câu 2.1 (1.0 điểm): Tạo một class với các thông tin được miêu tả như trên;

     Câu 2.2 (0.5 điểm): Tạo một menu để lựa chọn thực hiện công việc cho các
                          câu sau: Câu 2.3, Câu 2.4, Câu 2.5 và Câu 2.6

     Câu 2.3 (1.5 điểm): Nhập dữ liệu vào chương trình

         Các dữ liệu của class được lưu trong file văn bản đầu vào, có cấu trúc như sau:

                        Mã mặt hàng|Tên mặt hàng|Số lượng|Đơn giá

         Ví dụ một dòng thông tin cho một mặt hàng:

                        MH01|Gạo Lài sữa|3|17000

         Anh (chị) tự cho các thông tin của các mặt hàng với ít nhất 5 dòng thông tin cho 5 mặt hàng.

     Câu 2.4 (1.0 điểm): Hiển thị tất cả các thông tin của các mặt hàng ra màn hình (bao gồm cả thông tin về Thành tiền).
                  Trong trường hợp chưa có thông tin của mặt hàng nào thì thông báo “Bạn cần nhập thông tin về mặt hàng”.

     Câu 2.5 (1.0 điểm): Hiển thị thông tin của mặt hàng có Đơn giá cao nhất ra màn hình (bao gồm cả thông tin về Thành tiền)

     Câu 2.6 (1.0 điểm): Từ các thông tin của các mặt hàng, anh (chị) hãy ghi tất cả các thông tin của các mặt hàng
                  có Số lượng từ 5 trở lên (bao gồm cả thông tin về Thành tiền) ra file văn bản với mỗi mặt hàng là
                  một dòng thông tin(cấu trúc tương tự file văn bản đầu vào).

Solution:

"""

def Cau02():
    data = []  # list chua cac doi tuong
    n = 0  # so luong mat hang

    class MatHang:
        def __inif__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia =dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():

        # mo file
        f = open("CA20B1_53521_NguyenTanViet_int.txt", mode="r", encoding="utf-8")
        # doc du lieu va dua vao class
        n = int(f.readline())
        # n la so luong mat hang

        for i in range(0, n):
            row_data = f.readline().split("|")
            mat_hang = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang)  # dua du lieu vao data cac object

        # dong file
        f.close()
        print("==")*10
        print(" > Hoang thanh viec nhap du lieu tu file: CA20B1_53521_NguyenTanViet_int.txt ")

    def cv24():
        print("==") * 20
        if len(data) == 0:
            print("ban can chon thong tin ve mat hang")
        else:
            # da co thong tin xu ly
            print("\nIn thong tin cac mat hang:\n")
            print("==") * 20
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}"  \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))

    def cv25():
        if len(data) == 0:
            print("ban can chon nhap thong tin mat hang")
        else:
            # ghi du lieu
            f = open("CA20B1_53521_NguyenTanViet_out.txt", mode="w", encoding="utf-8")

            f.write(str(len(data)) + "\n")

            for i in data:
                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \

            f.close()
            print(" hoan thanh ghi ra file: CA20B1_53521_NguyenTanViet_out.txt ")
            print("=="*20)

    def cau25():
        """hien thi mat hang co don gia cao nhat"""
        print("==== Mat Hang Dat Nhat ====")
        # tim ra mat hang co don gia cao nhat
        MatHangDatNhat = data[0]
        for i in data:
            if i.don_gia > MatHangDatNhat.don_gia:
                MatHangDatNhat = i
        # hien thi mat hang co don gia cao nhat
        MatHangDatNhat_str = MatHangDatNhat.ma_mat_hang + "|" + MatHangDatNhat.ten_mat-hang + "|" + str(MatHangDatNhat)
        + "|" + str(MatHangDatNhat.don_gia) + "|" + str(MatHangDatNhat.thanh_tien)
        print(MatHangDatNhat_str)
        print("==") * 20

    while True:
        print("---MENU---")
        print("1, Nhap du lieu tu file.")
        print("2, In du lieu ra mang hinh.")
        print("3, In mat hang don gia cao nhat.")
        pring("4, Ghi thong tin tu file.")
        pring("Ban chon cong viec, Bam k de thoat: ")
        if cv == "1":
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "3":
            cv25()
        elif cv == "4":
            cv25()
        elif cv.upper() == "k":
            break





