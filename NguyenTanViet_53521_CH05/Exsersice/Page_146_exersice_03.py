"""
Author: NGUYEN TAN VIET
Date: 09/10/2021
Program: exersice_03_page_146.py
Problem:
     Phương pháp đột biến là gì? Giải thích tại sao các phương thức đột biến thường trả về
                                   giá trị Không có

Solution:
    Phương pháp đột biến và giá trị Không có
Các hàm và phương thức được kiểm tra trong các chương trước trả về một giá trị mà người gọi có thể
sau đó sử dụng để hoàn thành công việc của nó. Các đối tượng có thể thay đổi (chẳng hạn như danh sách)
có một số phương thức dành riêng hoàn toàn để sửa đổi trạng thái bên trong của đối tượng.
Những phương pháp như vậy được gọi là phương pháp đột biến. Bài kiểm tra xin là các phương pháp danh sách chèn,
nối, mở rộng, bật và sắp xếp. Bởi vì một sự thay đổi trạng thái là tất cả
điều đó được mong muốn, một phương thức mutator thường không trả về giá trị quan tâm cho người gọi (nhưng lưu ý rằng
pop là một ngoại lệ đối với quy tắc này). Tuy nhiên, Python tự động trả về giá trị đặc biệt Không có
ngay cả khi một phương thức không trả về một giá trị rõ ràng. Chúng tôi đề cập đến điều này bây giờ chỉ như một cảnh báo
chống lại loại lỗi sau. Giả sử bạn quên rằng việc sắp xếp đó làm thay đổi danh sách và thay vào đó bạn
nhầm tưởng rằng nó xây dựng và trả về một danh sách mới, được sắp xếp và để lại danh sách ban đầu không được sắp xếp.
Sau đó, bạn có thể viết mã như sau để nhận được những gì bạn nghĩ là kết quả mong muốn:

"""