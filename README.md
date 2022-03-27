# Nghiên Cứu Khoa Học Đại Học Thủ Dầu Một 2021 - 2022
## _Tên đề tài: XÂY DỰNG MÔ HÌNH HỆ TƯ VẤN TÌM VIỆC ONLINE CHO SINH VIÊN TRONG TRẠNG THÁI BÌNH THƯỜNG MỚI_

## Giới thiệu

GVHD: `Dương Thị Kim Chi`
Sinh viên thực hiện: `Hoàng Kim Tuyến | D18HT01`

Hệ thống gợi ý (Recommender System) là 1 nhánh con của hệ thống lọc thông tin (Infomation filtering system), nhằm tìm cách dự đoán việc đánh giá (rating) của người dùng (user) sẽ đưa ra cho 1 sản phẩm (item). Chúng chủ yếu được dùng trong các ứng dụng thương mại điện tử.

Ví dụ như: Giới thiệu các sản phẩm trên Amazon, các bài hát trên Spotify, các bộ phim trên Netflix hay các bài viết trên Medium, …

Thực chất, vấn đề của hệ gợi ý là xác định ánh xạ (u, i) -> R, trong đó u là biểu diễn cho 1 người dùng, i biểu diễn cho 1 sản phẩm và R là đánh giá của u lên i. Sau đó, các đánh giá của người dùng u lên tất cả các sản phẩm i tương ứng sẽ được sắp xếp, và lấy N sản phẩm có đánh giá cao nhất để đưa ra gợi ý cho người dùng u.

Khái niệm ‘đánh giá’ ở đây là khá trừu tượng, có thể được đo lường bằng hành động của người dùng như mua sản phẩm, click chuột vào sản phẩm, hoặc click vào “không hiển thị lại”, …

Hệ gợi ý thường được phân thành các loại sau:
- Lọc dựa trên nội dung (Content-base filtering)
- Lọc cộng tác (Collaborative filtering)
- Phương pháp lai ghép (Hybrid Method)

Tùy thuộc vào việc hệ thống có học từ dữ liệu hay không, lại chia thành các loại sau:
- Dựa trên bộ nhớ
- Dựa trên mô hình

Phương pháp lọc cộng tác hay hệ thống lọc cộng tác là phương pháp phân tích dữ liệu người dùng để tìm ra mối tương quan giữa các đối tượng người dùng. Lọc cộng tác hoạt động bằng cách xây dựng một cơ sở dữ liệu, lưu trữ dưới dạng ma trận người dùng (users) - sản phẩm (items) và mỗi dòng của nó là một vectơ.

Sau đó, phân tích dữ liệu, tính toán sự tương đồng giữa các users với nhau để đưa ra gợi ý. Ý tưởng quan trọng của phương pháp này là những người dùng tương tự có xu hướng sử dụng những sản phẩm tương tự (Singh & Pramod, 2019).

Ví dụ: Nếu khách hàng A thích các sản phẩm tương tự khách hàng B thì phương pháp lọc cộng tác sẽ đoán rằng khách hàng A có khả năng sẽ thích các sản phẩm khác mà khách hàng B đã thích/mua và ngược lại.

## Ưu điểm
- Phương pháp này có khả năng dự đoán được sở thích và nhu cầu của người dùng để đưa ra gợi ý các sản phẩm phù hợp với từng khách hàng mà không cần hiểu sản phẩm.
- Gợi ý dựa trên trải nghiệm của người dùng tương tự khác nên có thể gợi ý được những sản phẩm mới phù hợp sở thích mới.
- Phương pháp này rất phù hợp với những hệ thống lớn có nhiều đánh giá từ phía người dùng
## Nhược điểm
- Không thể gợi ý nếu khách hàng chưa có dữ liệu về lịch sử tương tác mặt hàng.
- Khi lượng sản phẩm lớn và số lượng khách hàng đánh giá không nhiều thì phương pháp này không hiệu quả.
- Phương pháp này cũng không thể gợi ý được các sản phẩm mới hoặc những sản phẩm chưa được ai đánh giá.
- Phương pháp này sẽ cho độ chính xác kém nếu như sở thích của người dùng thay đổi.

Ngày nay, phương pháp này được sử dụng khá phổ biến trên các trang nền tảng lớn như Shopee, Lazada, Youtube, Amazone, . . . bởi tính đơn giản và một lượng dữ liệu sẵn có từ người dùng trên các ứng dụng này.