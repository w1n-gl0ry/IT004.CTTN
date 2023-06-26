#!/usr/bin/python3
import mysql.connector  # Importing the MySQL connector library
import time  # Importing the time module
import xml.etree.ElementTree as ET  # Importing the ElementTree module from the XML library
from prettytable import PrettyTable  # Importing the PrettyTable library
import os  # Importing the os module

# Function to query and export data
def query_and_export_data():
    # Getting input from the user
    database_name = input("Database name: ")
    school_name = input("School name: ")
    academic_year = input("Academic year: ")
    academic_rank = input("Academic rank: ")

    # Connecting to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nguyenduy1012",
        database=database_name
    )
    cursor = connection.cursor()

    # Performing the query
    query = """
    SELECT HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
    FROM TRUONG AS TR
    INNER JOIN HOC ON TR.MATR = HOC.MATR
    INNER JOIN HS ON HOC.MAHS = HS.MAHS
    WHERE TR.TENTR = %s AND HOC.NAMHOC = %s AND HOC.XEPLOAI = %s
    """
    start_time = time.time()  # Measuring the start time of the query
    cursor.execute(query, (school_name, academic_year, academic_rank))
    end_time = time.time()  # Measuring the end time of the query
    elapsed_time = end_time - start_time

    rows = cursor.fetchall()

    # Closing the connection
    cursor.close()
    connection.close()

    # Creating the XML folder if it doesn't exist
    folder_path = "./XML/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Creating the XML file name based on the input information and folder path
    xml_filename = f"{folder_path}{database_name}-{school_name}-{academic_year}-{academic_rank}.xml"

    # Creating and writing data to the XML file
    root = ET.Element("Student_Lists")
    table = PrettyTable()
    table.field_names = ["Họ", "Tên", "NTNS", "Điểm TB", "Xếp loại", "Kết quả"]

    counter = 0  # Counter to keep track of the number of names printed

    for row in rows:
        student = ET.SubElement(root, "student")
        full_name = row[0] + " " + row[1]
        ET.SubElement(student, "ho_ten").text = full_name
        ET.SubElement(student, "ntns").text = row[2].strftime("%Y-%m-%d")  # Converting date to string
        ET.SubElement(student, "diem_tb").text = str(row[3])
        ET.SubElement(student, "xep_loai").text = row[4]
        ET.SubElement(student, "ket_qua").text = row[5]

        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])

        counter += 1

        if counter % 50 == 0:  # Print the table every 50 names
            print(table)
            table.clear_rows()

        if counter >= 100:  # Reset the counter and break if 100 names have been printed
            counter = 0
            break

    if counter > 0:  # Print the remaining names if any
        print(table)

    tree = ET.ElementTree(root)
    tree.write(xml_filename, encoding="utf-8", xml_declaration=True)

    print("\nBảng chứa dữ liệu đã được truy vấn")  # Print the queried data table
    print(f"\nThời gian truy vấn: {elapsed_time} giây")  # Print the query time
    print(f"Dữ liệu đã được xuất ra file: {xml_filename}")  # Print the exported file path

    return elapsed_time


# Calling the query_and_export_data() function to perform the query and export data for the first database
truy_van1 = query_and_export_data()

# Calling the query_and_export_data() function to perform the query and export data for the second database
truy_van2 = query_and_export_data()

# Comparing the query times of the two databases and printing the result
if truy_van1 > truy_van2:
    print('Thời gian truy vấn ở database TRUONGHOC2 nhanh hơn database TRUONGHOC1')
elif truy_van1 == truy_van2:
    print('Thời gian truy vấn ở database TRUONGHOC1 bằng database TRUONGHOC2')
else:
    print('Thời gian truy vấn ở database TRUONGHOC1 nhanh hơn database TRUONGHOC2')
