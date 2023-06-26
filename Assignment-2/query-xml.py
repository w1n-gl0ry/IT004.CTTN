#!/usr/bin/python3
import xml.etree.ElementTree as ET
import glob
import random


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

    for student in students:
        ho_ten = student.find("ho_ten").text
        diem_tb = student.find("diem_tb").text
        print(f"""Học sinh: {ho_ten} 
Điểm TB: {diem_tb}
              """)

# Path to the folder containing XML files
xml_folder_path = "./XML/"

# Read all XML files in the folder
xml_data = read_xml_files(xml_folder_path)

# Get a random XML file
random_xml_file, random_xml_root = random.choice(xml_data)

# Enter score thresholds from the user
low_score = float(input("Low score: "))
high_score = float(input("High score: "))

# Filter and print the list of students within the score range in the random XML file
print(f"\n--- {random_xml_file} ---")
filtered_students = filter_students_by_score(random_xml_root, low_score, high_score)
print_students(filtered_students)
