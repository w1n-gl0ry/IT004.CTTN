import pandas as pd
import os  

# Đường dẫn đến folder chứa các file excel
folder_path = 'F:\SQL\Phần 2'

extra_files = ['Sở.xlsx', 'Phòng.xlsx', 'Loại hình.xlsx', 'Loại trường.xlsx', 'Cấp.xlsx']

extra_file_name = 'table_phu.sql' 

with open(os.path.join(folder_path, extra_file_name), 'w', encoding='utf-8') as f:
    f.write("USE truonghoc;" + "\n")

for file in extra_files:
    df_ef = pd.read_excel(os.path.join(folder_path, file), sheet_name='Sheet1')
    with open(os.path.join(folder_path, extra_file_name), 'a', encoding='utf-8') as f:        
        if file == 'Sở.xlsx':
            for index, row in df_ef.iterrows():
                insert_sql = f"INSERT INTO SO_GD_DT (MA_SO, TEN_SO) VALUES ('{row['Mã Sở']}', '{row['Tên Sở']}');\n"
                f.write(insert_sql)
        if file == 'Phòng.xlsx':
            for index, row in df_ef.iterrows():
                insert_sql = f"INSERT INTO PHONG_GD_DT (MA_PHONG, TEN_PHONG, MA_SO) VALUES ('{row['Mã Phòng']}', '{row['Tên Phòng']}', '{row['Mã Sở']}');\n"
                f.write(insert_sql)
        if file == 'Loại hình.xlsx':
            for index, row in df_ef.iterrows():
                insert_sql = f"INSERT INTO LOAIHINH (MA_LOAI_HINH, TEN_LOAI_HINH) VALUES ('{row['Mã loại hình']}', '{row['Tên loại hình']}');\n"
                f.write(insert_sql)
        if file == 'Loại trường.xlsx':
            for index, row in df_ef.iterrows():
                insert_sql = f"INSERT INTO LOAITRUONG (MA_LOAI_TRUONG, TEN_LOAI_TRUONG) VALUES ('{row['Mã loại trường']}', '{row['Tên loại trường']}');\n"
                f.write(insert_sql)
        if file == 'Cấp.xlsx':
            for index, row in df_ef.iterrows():
                insert_sql = f"INSERT INTO CAP_HOC (MA_CAP, TEN_CAP) VALUES ('{row['Mã cấp']}', '{row['Tên cấp']}');\n"
                f.write(insert_sql)
# Đọc tất cả các file excel trong folder và lưu vào một danh sách
file_list = [file for file in os.listdir(folder_path) if file.endswith('.xlsx') and file not in extra_files]

# Lặp qua từng file trong danh sách và tạo file sql tương ứng
for file in file_list:
    # Đọc dữ liệu từ file excel
    df = pd.read_excel(os.path.join(folder_path, file), sheet_name='Sheet1')
    
    # Lấy tên file và thay đổi phần mở rộng thành .sql
    sql_file_name = os.path.splitext(file)[0] + '.sql'
    
    # Ghi dữ liệu vào file sql vừa tạo
    with open(os.path.join(folder_path, sql_file_name), 'w', encoding='utf-8') as f:
 
        # Lặp qua từng hàng trong dataframe và tạo câu lệnh INSERT
        for index, row in df.iterrows():

            # Tạo câu lệnh INSERT
            newRow = row
            insert_sql = f"INSERT IGNORE INTO TRUONG (MATRUONG, TENTRUONG, MASO, MAPHONG, DIACHI, MA_LOAI_HINH, MA_LOAI_TRUONG, CAP) VALUES ('{newRow['Mã trường']}', '{newRow['Tên trường']}', '{newRow['Sở GD&ĐT']}', '{newRow['Phòng GD&ĐT']}', '{newRow['Địa chỉ']}', '{newRow['Loại hình']}', '{newRow['Loại trường']}', '{newRow['Cấp']}');\n"

            # Ghi câu lệnh INSERT vào file sql
            insert_sql = insert_sql.replace("'nan'", "null")
            
            # Ghi câu lệnh INSERT vào file sql
            f.write(insert_sql)