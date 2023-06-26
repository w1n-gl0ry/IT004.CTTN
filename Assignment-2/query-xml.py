#!/usr/bin/python3
import xml.etree.ElementTree as ET
import glob
from prettytable import PrettyTable

def read_xml_files(xml_folder_path):
    xml_files = glob.glob(xml_folder_path + "*.xml")
    xml_data = []

    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        xml_data.append((xml_file, root))

    return xml_data

def filter_students_by_score(root, low_score, high_score):
    xpath_query = ".//student"
    filtered_students = root.findall(xpath_query)
    return filtered_students

def print_students(students):
    if not students:
        print("No students within the given score range.")
        return

    table = PrettyTable()
    table.field_names = ["STT", "Học sinh", "Điểm TB"]
    
    for i, student in enumerate(students, start=1):
        ho_ten = student.find("ho_ten").text
        diem_tb = student.find("diem_tb").text
        table.add_row([i, ho_ten, diem_tb])

    print(table)

# Path to the folder containing XML files
xml_folder_path = "./XML/"

# Read all XML files in the folder
xml_data = read_xml_files(xml_folder_path)

# List all XML files and prompt the user to choose one
print("Available XML files:")
for i, (xml_file, _) in enumerate(xml_data):
    print(f"{i+1}. {xml_file}")
selected_index = int(input("Enter the index of the XML file to process: ")) - 1

# Get the selected XML file and its root
selected_xml_file, selected_xml_root = xml_data[selected_index]

# Enter score thresholds from the user
low_score = float(input("Low score: "))
high_score = float(input("High score: "))

# Filter and print the list of students within the score range in the selected XML file
print(f"\n--- {selected_xml_file} ---")
filtered_students = filter_students_by_score(selected_xml_root, low_score, high_score)
print_students(filtered_students)
