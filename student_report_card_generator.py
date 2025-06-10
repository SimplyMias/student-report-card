def get_student_info():
    name = input("Enter Student Name: ")
    roll_no = input("Enter roll number: ")
    return name, roll_no

def get_marks():
    marks = []
    for i in range(1,6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks
    
def calculate_total_nd_percentage(marks):
    total = sum(marks)
    percentage = total/5
    return total, percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"
    
def print_report(name, roll_no, marks, total, percentage, grade ):
    print("\n-----Student Report Card-----")
    print("Name: ",name)
    print("Roll no: ",roll_no)
    print("Marks: ",marks)
    print("Total: ",total)
    print("Percentage: ",percentage)
    print("Grade: ",grade)
    print("---------------------------")


name, roll_no = get_student_info()
marks  = get_marks()
total, percentage = calculate_total_nd_percentage(marks)
grade = calculate_grade(percentage)
print_report(name, roll_no, marks, total, percentage, grade)

    

