# Class  EX
from tabulate import tabulate
import csv

class Student:
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self._grade = None
        self.grade = grade
    
    def __str__(self):
        return f"Name: {self.first} Lastname: {self.last}. Grade: [{self.grade}]"
    
    @staticmethod
    def full_info():
        header = ["Name", "Lastname", "Grade"]
        table = []
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append([row['Name'], row['Lastname'], row['Grade']])
        display_table = tabulate(table, header, tablefmt='grid')
        return display_table
        
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if (10 <= value <= 100):
            self._grade = value
        else:
            self._grade = None
            raise ValueError
    
    def add_student(self):
        fields = ["Name", "Lastname","Grade"]
        rows = [{'Name': self.first, 'Lastname': self.last, 'Grade': self.grade}]
        with open('students.csv', 'a', newline='') as students_file:
            writer = csv.DictWriter(students_file, fieldnames=fields)
            if students_file.tell() == 0:
                writer.writeheader()
            writer.writerows(rows)
    
