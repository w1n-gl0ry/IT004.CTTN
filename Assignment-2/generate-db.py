from mysql.connector import Error
from tqdm import tqdm
from faker import Faker
import pandas
import openpyxl
import random
import datetime
import mysql.connector
import itertools

# List of surnames
sur_name = [
    "Nguyễn",
    "Trần",
    "Lê",
    "Phạm",
    "Hoàng",
    "Huỳnh",
    "Phan",
    "Vũ",
    "Võ",
    "Đặng",
    "Bùi",
    "Đỗ",
    "Hồ",
    "Ngô",
    "Dương",
    "Lý",
    "Thanh",
    "Trương",
    "Đinh",
    "Trịnh",
    "Bùi",
    "Mạc",
    "Đoàn",
    "Hà",
    "Vương",
    "Quách",
    "Cao",
    "Đồng",
    "Đỗ",
    "Ngô",
    "Trịnh",
    "Bạch",
    "Tạ",
    "Bành",
    "Phùng",
    "Tiêu",
    "Mã",
    "Lưu",
    "Từ",
    "Lục",
    "Diệp",
    "Lăng",
    "Lỗ",
    "Hứa",
    "Ninh",
    "Khuất",
    "Lai",
    "Lô",
    "Mông",
    "Bắc"
]
# List of middle names
middle_name = [
    "Anh",
    "Ân",
    "Bình",
    "Cẩm",
    "Châu",
    "Chi",
    "Duy",
    "Gia",
    "Hoài",
    "Hương",
    "Huy",
    "Huyền",
    "Kỳ",
    "Lan",
    "Lâm",
    "Linh",
    "Lý",
    "Mai",
    "Minh",
    "Mỹ",
    "Nam",
    "Ngọc",
    "Nhật",
    "Nhi",
    "Như",
    "Oanh",
    "Phương",
    "Quang",
    "Quỳnh",
    "Sơn",
    "Thái",
    "Thảo",
    "Thanh",
    "Thành",
    "Thi",
    "Thu",
    "Thủy",
    "Thúy",
    "Tiến",
    "Trâm",
    "Triệu",
    "Trung",
    "Tú",
    "Tuấn",
    "Tường",
    "Uyên",
    "Vân",
    "Vi",
    "Việt",
    "Vinh",
    "Vũ",
    "Xuân",
    "Yến",
    "Yến",
    "Zoe",
    "Hà",
    "Hải",
    "Hạnh",
    "Hiền",
    "Hòa",
    "Hoa",
    "Hưng",
    "Hương",
    "Huy",
    "Huyền",
    "Khanh",
    "Khôi",
    "Khải",
    "Khánh",
    "Kiên",
    "Kim",
    "Lan",
    "Linh",
    "Lâm",
    "Long",
    "Mai",
    "Minh",
    "My",
    "Nam",
    "Nga",
    "Ngọc",
    "Nguyên",
    "Nhân",
    "Nhã",
    "Nhi",
    "Nhung",
    "Oanh",
    "Phương",
    "Quân",
    "Quang",
    "Quỳnh"
]
# List of names
name = [
    "An",
    "Anh",
    "Ân",
    "Âu",
    "Bảo",
    "Bình",
    "Cường",
    "Chi",
    "Châu",
    "Chung",
    "Dũng",
    "Đạt",
    "Đức",
    "Đan",
    "Điệp",
    "Đoàn",
    "Đông",
    "Đông",
    "Đức",
    "Giang",
    "Hà",
    "Hải",
    "Hạnh",
    "Hiền",
    "Hòa",
    "Hoa",
    "Hoài",
    "Hoàng",
    "Hoan",
    "Hương",
    "Hùng",
    "Hường",
    "Huy",
    "Huyền",
    "Khanh",
    "Khôi",
    "Khải",
    "Khánh",
    "Khoa",
    "Kiên",
    "Kim",
    "Lam",
    "Lan",
    "Linh",
    "Lâm",
    "Long",
    "Lý",
    "Mai",
    "Minh",
    "My",
    "Nam",
    "Nga",
    "Ngân",
    "Ngọc",
    "Nguyên",
    "Nhân",
    "Nhã",
    "Nhi",
    "Nhiên",
    "Nhung",
    "Oanh",
    "Phong",
    "Phương",
    "Quân",
    "Quang",
    "Quỳnh",
    "Sơn",
    "Sương",
    "Thanh",
    "Thảo",
    "Thắm",
    "Thị",
    "Thu",
    "Thuần",
    "Thúy",
    "Thùy",
    "Thành",
    "Thắng",
    "Thăng",
    "Thiên",
    "Trà",
    "Trâm",
    "Triều",
    "Trang",
    "Trung",
    "Trọng",
    "Tú",
    "Tùng",
    "Tuyết",
    "Uyên",
    "Vi",
    "Việt",
    "Vân",
    "Vũ",
    "Xuân",
    "Yến"
]

# Function to generate linear IDs
def generate_linear_ids(total):
    ids = []
    current_id = 45204005843  # Starting ID

    while len(ids) < total:
        id_str = str(current_id).zfill(12)  # Zero-padding ID to 12 digits
        ids.append(id_str)
        current_id += 1

    return ids


linear_ids = generate_linear_ids(1000000)
random.shuffle(linear_ids)

# function to connect to mysql_server
def connect(host, user, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=120000000  
        )
        print("Connection successful")
    except Error as err:
        print(f"Connection Error: '{err}'")
        
    return connection

# function to execute query from my_sql
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.executemany(query, data)
        else:
            cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Query Execution Error: '{err}'")

# try to connect to the database truonghoc1 and truonghoc2
connection = connect('localhost', 'root', 'Nguyenduy1012', 'TRUONGHOC1')
connection_2 = connect('localhost', 'root', 'Nguyenduy1012', 'TRUONGHOC2')

# random of 100 school ID's 
ma_truong = [79000701, 79000702, 79000703, 79000704, 79000705, 79000706, 79000707, 79000708, 79000709, 79000710, 79000711, 79000712, 79000713, 79000714, 79000715, 79000716, 79000717, 79000718, 79000719, 79000720, 79000721, 79000722, 79000723, 79000724, 79000725, 79000726, 79000727, 79000728, 79000729, 79000730, 79000731, 79000732, 79000733, 79000734, 79000735, 79000736, 79000737, 79000738, 79000739, 79000740, 79000741, 79000742, 79000743, 79000744, 79000745, 79000746, 79000747, 79000748, 79000749, 79000750, 79000751, 79000752, 79000753, 79000754, 79000755, 79000756, 79000757, 79000758, 79000759, 79000760, 79000761, 79000762, 79000763, 79000764, 79000765, 79000767, 79000768, 79000769, 79000771, 79000772, 79000773, 79000774, 79000775, 79000776, 79000777, 79000779, 79000780, 79000781, 79000783, 79000784, 79000785, 79000786, 79000788, 79000791, 79000793, 79000794, 79000795, 79000796, 79000797, 79000798, 79000799, '790007A1', '790007A2', '790007A4', '790007A5', '790007A6', '790007A7', '790007A8', '790007A9', '790007B0']
# random of 100 school name's  that equivalent to it's ID
ten_truong = ['THPT Bùi Thị Xuân', 'THPT Trưng Vương', 'THPT Giồng Ông Tố', 'THPT Nguyễn Thị Minh Khai', 'THPT Lê Quý Đôn', 'THPT Nguyễn Trãi', 'Phổ thông Năng khiếu thể thao Olympic', 'THPT Hùng Vương', 'THPT Mạc Đĩnh Chi', 'THPT Bình Phú', 'THPT Lê Thánh Tôn', 'THPT Lương Văn Can', 'THPT Ngô Gia Tự', 'THPT Tạ Quang Bửu', 'THPT Nguyễn Huệ', 'THPT Nguyễn Khuyến', 'THPT Nguyễn Du', 'THPT Nguyễn Hiền', 'THPT Võ Trường Toản', 'THPT Thanh Đa', 'THPT Võ Thị Sáu', 'THPT Gia Định', 'THPT Phan Đăng Lưu', 'THPT Gò Vấp', 'THPT Nguyễn Công Trứ', 'THPT Phú Nhuận', 'THPT Tân Bình', 'THPT Nguyễn Chí Thanh', 'THPT Trần Phú', 'THPT Nguyễn Thượng Hiền', 'THPT Thủ Đức', 'THPT Nguyễn Hữu Huân', 'THPT Tam Phú', 'THPT Củ Chi', 'THPT Quang Trung', 'THPT An Nhơn Tây', 'THPT Trung Phú', 'THPT Trung Lập', 'THPT Nguyễn Hữu Cầu', 'THPT Lý Thường Kiệt', 'THPT Bình Chánh', 'THPT Ten Lơ Man', 'THPT Marie Curie', 'THPT Trần Khai Nguyên', 'THPT Nguyễn An Ninh', 'THPT Nam Kỳ Khởi Nghĩa', 'THPT Nguyễn Thái Bình', 'THPT Nguyễn Trung Trực', 'THPT Hàn Thuyên', 'THPT Hoàng Hoa Thám', 'THPT Thăng Long', 'THPT Phước Long', 'THPT Bà Điểm', 'THPT Tân Phong', 'THPT Trường Chinh', 'THPT Phú Hòa', 'THPT Tân Thông Hội', 'THPT Tây Thạnh', 'THPT Long Trường', 'THPT Nguyễn Văn Cừ', 'THPT Nguyễn Hữu Tiến', 'THPT Bình Khánh', 'THPT Cần Thạnh', 'THPT Trần Hưng Đạo', 'THPT Hiệp Bình', 'Tiểu học THCS và THPT Quốc Văn Sài Gòn', 'THPT Trần Quang Khải', 'THPT Vĩnh Lộc', 'THPT Việt Âu', 'THPT Việt Nhật', 'THPT Hưng Đạo', 'TH - THCS - THPT Chu Văn An', 'Trung học Thực hành Đại học Sư phạm', 'Phổ thông Năng Khiếu - ĐHQG Tp. HCM', 'THPT Lý Thái Tổ', 'THPT Trần Quốc Tuấn', 'THPT An Dương Vương', 'THPT Trần Nhân Tông', 'THPT Đông Dương', 'THPT Phước Kiển', 'THPT Nhân Việt', 'THPT An Nghĩa', 'THPT Phú Lâm', 'Trung học cơ sở và trung học phổ thông Phùng Hưng', 'THPT Nguyễn Hữu Cảnh', 'THPT Nguyễn Văn Linh', 'Phân hiệu THPT Lê Thị Hồng Gấm', 'THPT Nguyễn Thị Diệu', 'THPT Quốc Trí', 'THPT Vĩnh Viễn', 'THCS - THPT Trần Cao Vân', 'THPT Bách Việt', 'THPT Việt Mỹ Anh', 'THCS và THPT Nam Việt', 'THPT Văn Lang', 'THPT Bình Hưng Hòa', 'THPT Bình Tân', 'THPT Nguyễn Tất Thành', 'THPT Nguyễn Văn Tăng', 'THPT Trần Văn Giàu']
# random of 100 school address's that equivalent to it's ID
dia_chi_truong = ['73 - 75 Bùi Thị Xuân', '3 Nguyễn Bỉnh Khiêm', '200/10 Nguyễn Thị Định', '275 Điện Biên Phủ', '110 Nguyễn Thị Minh Khai Phường 6 Quận 3 TP.Hồ Chí Minh', '364 Nguyễn Tất Thành', 'Đại học Thể dục thể thao TP. Hồ Chí Minh\nKhu phố 6 - phường Linh Trung - Quận Thủ Đức - TP. Hồ Chí Minh', '124 Hùng Vương', '04 Tân Hòa Đông', '102 Đường Trần Văn Kiểu Phường 1  Quận 6 TPHCM', '124 đường 17', '173 Phạm Hùng', '360E Bến Bình Đông', '909 Tạ Quang Bửu', 'Đường Nguyễn Văn Tăng Kp Châu Phúc Cẩm P.LTM Q9', '50 Thành Thái', 'XX-1 Đồng Nai', '3 Dương Đình Nghệ-P8-Q11', '482 Đường Nguyễn Thị Đặng - Khu Phố 1', '186 Nguyễn Xí phường 26 quận Bình Thạnh TP.HCM', '95 Đinh Tiên Hoàng', '195/29 Xô Viết Nghệ Tĩnh', '27 Nguyễn Văn Đậu', '90A Nguyễn Thái Sơn', '97 Quang Trung Phường 8 Quận Gò Vấp TP.HCM', 'Số 5 Hoàng Minh Giám', '19 Hoa Bằng', '1A Nguyễn Hiến Lê', '18 Lê Thúc Hoạch', '544 Cách Mạng Tháng 8', '166/24 Đặng Văn Bi', '11 Đoàn Kết', '31 Phú Châu Kp5', 'Tỉnh lộ 8 Khu phố 1', 'Ấp Phước An', '227Đường Tỉnh lộ 7 Ấp Chợ Cũ Xã An Nhơn Tây Huyện Củ Chi TP.HCM', '1318 tỉnh lộ 8 Ấp 12', '91/3 Trung Lập Ấp Trung Bình.', 'Tô Ký Ấp Mỹ Huề Xã Trung Chánh Huyện Hóc Môn TP. HCM.', 'Đường Nam Thới 2 Ấp Nam Thới Xã Thới Tam Thôn', 'D17/1D Huỳnh Văn Trí', '8 Trần Hưng Đạo Phường Phạm Ngũ Lão Quận 1 Tp.Hồ Chí Minh', '159 Nam Kỳ Khởi Nghĩa', '225 Nguyễn Tri Phương', '93 Trần Nhân Tôn', '269/8 Nguyễn Thị Nhỏ', '913-915 Lý Thường Kiệt', '9/168 Lê Đức Thọ', '37 Đặng Văn Ngữ', '6 Hoàng Hoa Thám', '114-116 Hải Thượng Lãn Ông', 'Dương Đình Hội Khu phố 6 - Phường Phước Long B - Q.9', 'Số7 Nguyễn Thị Sóc Ấp Bắc Lânxã Bà Điểm Huyện Hóc Môn', '19F Nguyễn Văn Linh', '1 DN11 Khu phố 4', 'Số 25 đường Huỳnh Thị Bẵng Ấp Phú Lợi', 'Ấp Bàu Sim', '27 Đường C2', '309 Võ Văn Hát Kp Phước Hiệp phường Long Trường Quận 9 Tp. Hồ Chí Minh', '100A ấp 6 xã Xuân Thới Thương Huyện Hóc Môn', '9A Ấp 7', 'Ấp Bình An', '346 Đường Duyên Hải - Khu Phố Miễu Ba - Thị trấn Cần Thạnh - huyện Cần Giờ', '88/955E Lê Đức Thọ', 'Số 63 đường Hiệp Bình khu phố 6', '300 Hòa     Bình', '343D Lạc Long Quân', '87 Đường Số 3 Kdc Vĩnh Lộc Phường Bình Hưng Hòa B Bình Tân TP.HCM', '30/2 Quốc lộ 1A', '371 Nguyễn Kiệm', '103 Nguyễn Văn Đậu', 'Số 7 Đường Số 1 Khu Phố 1', '280 An Dương Vương Phường 4 Quận 5 Tp. Hồ Chí Minh', '153 Nguyễn Chí Thanh', '1/22/2a Nguyễn Oanh', '236/10-12 Thái Phiên', 'đường số 3khu phố 6 phường Trường Thọ quận Thủ Đức', '66 Tân Hóa', '114/37/12A-E Đường số 10', 'Số 1163 Đường Lê Văn Lương Ấp 3', '41-39 Đoàn Hồng Phước', 'Ấp An Nghĩa', '12-24 đường số 3 chợ Phú Lâm', '14A Đường số 1 Phường 16 Quận Gò vấp TP Hồ Chí Minh', '845 Hương Lộ 2', 'Số 02 Đường 3154 Phạm Thế Hiển  Phường 07 Quận 08', '147 Pasteur', '12 Trần Quốc Toản', '313 Nguyễn Văn Luông', '73/7 Lê Trọng Tấn - Phường Sơn Kỳ Quận Tân Phú', '126 Tô Hiệu', '653 Quốc lộ 13 Kp3', '252 Lạc Long Quân', '25 21/1-3 23/7-9 Dương Đức Hiền', '02-04 Tân Thành', '79/19 Đường Số 4 Kp7 P.BHH Q.Bình Tân', '117/4H Hồ Văn Long', '249C Nguyễn Văn Luông', 'Đường số 1 KP Tái Định Cư Long Bửu', '203/40 Đường Trục Phường 13Quận Bình Thạnh TP.Hồ Chí Minh']

# generate a list that has data is format to excute command
data = [(ma_truong[i], ten_truong[i], dia_chi_truong[i]) for i in range(100)]
# command format
query = "INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s, %s, %s);"

# excute query to insert data to Truong table in TRUONGHOC1 database
execute_query(connection, query, data)
# excute query to insert data to Truong table in TRUONGHOC2 database
execute_query(connection_2, query, data)

# print(ma_truong) -> for debug purpose

# generate a list of 1 milion student ID's
ma_hs = list(range(22520000, 32520001))

# random student ID's, school ID's, name of school, and it's address
random.shuffle(ma_hs)
random.shuffle(ma_truong)
random.shuffle(ten_truong)
random.shuffle(dia_chi_truong)

# Dictionary of districts and wards
quan_huyen = {
'Thành phố Đông Hà': ['Phường 1', 'Phường 2', 'Phường 3', 'Phường 4', 'Phường 5', 'Phường Đông Giang', 'Phường Đông Lễ',
'Phường Đông Lương', 'Phường Đông Thanh', 'Phường Đông Thịnh', 'Phường Đông Vinh',
'Phường Đông Xá'],
'Thị xã Quảng Trị': ['Phường 1', 'Phường 2', 'Phường An Đôn', 'Phường Bến Quan', 'Phường Đông Hà', 'Phường Đông Lễ',
'Phường Đông Lương', 'Phường Đông Thanh', 'Phường Đông Thịnh', 'Phường Đông Vinh',
'Phường Đông Xá', 'Phường Đông Yên', 'Phường Hải Lệ', 'Phường Hải Quế', 'Phường Hòa Thuận',
'Phường Vĩ Dạ'],
'Huyện Vĩnh Linh': ['Thị trấn Cửa Tùng', 'Thị trấn Khe Sanh', 'Xã Trung Hải', 'Xã Vĩnh An', 'Xã Vĩnh Chấp',
'Xã Vĩnh Giang', 'Xã Vĩnh Hà', 'Xã Vĩnh Hiền', 'Xã Vĩnh Hòa', 'Xã Vĩnh Kim', 'Xã Vĩnh Lâm',
'Xã Vĩnh Long', 'Xã Vĩnh Nam', 'Xã Vĩnh Ô', 'Xã Vĩnh Sơn', 'Xã Vĩnh Tân', 'Xã Vĩnh Thái',
'Xã Vĩnh Thành', 'Xã Vĩnh Thủy', 'Xã Vĩnh Trung', 'Xã Vĩnh Tú', 'Xã Vĩnh Yên'],
'Huyện Hướng Hóa': ['Thị trấn Khe Tre', 'Thị trấn Tân Hóa', 'Xã Cam Chính', 'Xã Cam Hiếu', 'Xã Cam Lộ', 'Xã Cam Nghĩa',
'Xã Cam Thành', 'Xã Cam Thanh', 'Xã Cam Thủy', 'Xã Cam Tuyền', 'Xã Húc', 'Xã Hướng Lập',
'Xã Hướng Linh', 'Xã Hướng Phùng', 'Xã Hướng Sơn', 'Xã Hướng Tân', 'Xã Hướng Việt',
'Xã Hướng Vĩnh', 'Xã Hướng Xuân'],
'Huyện Gio Linh': ['Thị trấn Gio Linh', 'Xã Gio An', 'Xã Gio Bình', 'Xã Gio Châu', 'Xã Gio Hà', 'Xã Gio Hải',
'Xã Gio Linh', 'Xã Gio Mai', 'Xã Gio Mỹ', 'Xã Gio Phong', 'Xã Gio Quang', 'Xã Gio Sơn',
'Xã Gio Thành', 'Xã Gio Việt', 'Xã Gio Xuyên', 'Xã Gioi Thạch'],
}

# Setting up date variables
date = datetime.date(year=2000, month=1, day=1)
date_ = datetime.date(year=2005, month=12, day=31)
fake = Faker()
data = []

# command format
query = "INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s, %s, %s, %s, %s, %s);"

# a loop that generate a list of 1 milion format data to pass to cmd 
for i in tqdm(range(1000000)):
    ho = random.choice(sur_name) 
    ten = random.choice(middle_name) + " " + random.choice(name)
    birth_day = fake.date_between(start_date=date, end_date=date_)
    ma_huyen = list(quan_huyen.keys())
    random.shuffle(ma_huyen)
    tinh = 'Quảng Trị'
    huyen = random.choice(ma_huyen)
    xa = random.choice(quan_huyen[huyen])
    dia_chi = f'{xa}, {huyen}, Tỉnh {tinh}'
    data.append((str(ma_hs[i]), ho, ten, linear_ids[i], str(birth_day), dia_chi))

size = 100000
total = 1000000

# excute query to my_sql each time (total: 10 times)
for start in tqdm(range(0, total, size)):
    end = min(start + size, total)
    
    b_data = data[start:end]

    execute_query(connection, query, b_data)
    execute_query(connection_2, query, b_data)

# random school_ID's
random.shuffle(ma_truong)
data = []

# a loop that generate a list of 1 milion format data's and contain variable's to insert to HOC table
for i in tqdm(range(1000000)):
    ma_tr = random.choice(ma_truong)
    nam = str(random.randint(2020, 2023))
    diem_tb = (random.random()) * 10

    if (diem_tb > 9):
        rank = "Xuất sắc"
    elif (diem_tb > 8):
        rank = "Giỏi"
    elif (diem_tb > 7):
        rank = "Khá"
    elif (diem_tb > 5):
        rank = "Trung bình"
    else:
        rank = "Yếu"

    if (diem_tb < 5):
        result = 'Chưa hoàn thành'
    else:
        result = 'Hoàn thành'

    data.append((str(ma_tr), str(ma_hs[i]), nam, round(diem_tb, 2), rank, result))

# command format
query = "INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES (%s, %s, %s, %s, %s, %s);"

# print(data) -> for debug purpose only

size = 100000
total = 1000000

# excute query to my_sql each time (total: 10 times)
for start in tqdm(range(0, total, size)):
    end = min(start + size, total)
    
    b_data = data[start:end]

    execute_query(connection, query, b_data)
    execute_query(connection_2, query, b_data)
    
# Successfully import it
print('Done')
