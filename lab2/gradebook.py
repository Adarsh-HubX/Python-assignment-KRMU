
"""
GradeBook Analyzer - Automated Student Grade Analysis System
Author: Adarsh Rathore
Date: 5 November 2025
Purpose: Analyze student grades, compute statistics, assign letter grades, and generate reports
"""

import csv
import statistics
from pathlib import Path


def print_welcome():
    """Display welcome message and usage menu"""
    print("\n" + "="*60)
    print("       WELCOME TO GRADEBOOK ANALYZER v1.0")
    print("="*60)
    print("\nThis tool helps you analyze student grades efficiently!")
    print("\nFeatures:")
    print("  • Calculate grade statistics (mean, median, min, max)")
    print("  • Assign letter grades automatically")
    print("  • Filter pass/fail students")
    print("  • Generate formatted grade reports\n")


def get_input_method():
    """Ask user to choose between manual input or CSV file"""
    while True:
        print("How would you like to input student data?")
        print("1. Manual entry (type names and marks)")
        print("2. Load from CSV file")
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice in ['1', '2']:
            return choice
        print("❌ Invalid choice. Please enter 1 or 2.\n")


def manual_data_entry():
    """Collect student marks manually from user input - Task 2"""
    marks = {}
    print("\n--- MANUAL DATA ENTRY ---\n")
    
    # Task 2: Ask user how many students are in the class
    while True:
        try:
            num_students = int(input("How many students are in the class? "))
            if num_students <= 0:
                print("❌ Please enter a positive number.\n")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.\n")
    
    print()
    
    # Task 2: Take input for each student
    for i in range(num_students):
        while True:
            name = input(f"Student {i+1} - Enter name: ").strip()
            if not name:
                print("❌ Name cannot be empty.\n")
                continue
            
            try:
                mark = float(input(f"Enter marks for {name}: ").strip())
                if not (0 <= mark <= 100):
                    print("❌ Marks must be between 0 and 100.\n")
                    continue
                marks[name] = mark
                print(f"✓ Added {name}: {mark}\n")
                break
            except ValueError:
                print("❌ Please enter a valid number.\n")
    
    return marks


def load_csv_data():
    """Load student data from a CSV file"""
    print("\n--- CSV FILE IMPORT ---\n")
    
    while True:
        filepath = input("Enter CSV file path (e.g., students.csv): ").strip()
        
        if not Path(filepath).exists():
            print(f"❌ File '{filepath}' not found.\n")
            continue
        
        try:
            marks = {}
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                if reader.fieldnames is None:
                    print("❌ CSV file is empty.\n")
                    continue
                
                # Handle flexible column names
                name_col = next((col for col in reader.fieldnames if col.lower() in ['name', 'student', 'student_name']), reader.fieldnames[0])
                mark_col = next((col for col in reader.fieldnames if col.lower() in ['marks', 'score', 'grade']), reader.fieldnames[1] if len(reader.fieldnames) > 1 else None)
                
                if mark_col is None:
                    print("❌ CSV must have at least 2 columns (name and marks).\n")
                    continue
                
                for row in reader:
                    try:
                        name = row[name_col].strip()
                        mark = float(row[mark_col].strip())
                        
                        if 0 <= mark <= 100 and name:
                            marks[name] = mark
                    except (ValueError, KeyError):
                        continue
            
            if not marks:
                print("❌ No valid student records found in CSV.\n")
                continue
            
            print(f"✓ Successfully loaded {len(marks)} students from CSV\n")
            return marks
        
        except Exception as e:
            print(f"❌ Error reading file: {e}\n")


def calculate_average(marks_dict):
    """Calculate average marks - Task 3"""
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    """Calculate median marks - Task 3"""
    if not marks_dict:
        return 0
    return statistics.median(marks_dict.values())


def find_max_score(marks_dict):
    """Find maximum marks - Task 3"""
    if not marks_dict:
        return 0
    max_student = max(marks_dict, key=marks_dict.get)
    return marks_dict[max_student], max_student


def find_min_score(marks_dict):
    """Find minimum marks - Task 3"""
    if not marks_dict:
        return 0
    min_student = min(marks_dict, key=marks_dict.get)
    return marks_dict[min_student], min_student


def assign_grade(mark):
    """Assign letter grade based on mark using if-elif-else - Task 4"""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'


def create_grades_dict(marks_dict):
    """Create dictionary with grades for all students - Task 4"""
    grades = {name: assign_grade(mark) for name, mark in marks_dict.items()}
    return grades


def get_grade_distribution(grades_dict):
    """Count students per grade category - Task 4"""
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        distribution[grade] += 1
    return distribution


def get_pass_fail_students(marks_dict):
    """Filter students using list comprehension - Task 5"""
    # passed_students with marks >= 40
    passed = [name for name, mark in marks_dict.items() if mark >= 40]
    # failed_students with marks < 40
    failed = [name for name, mark in marks_dict.items() if mark < 40]
    return passed, failed


def display_statistics(marks_dict, grades_dict):
    """Display statistical analysis - Task 3"""
    avg = calculate_average(marks_dict)
    median = calculate_median(marks_dict)
    max_score, max_student = find_max_score(marks_dict)
    min_score, min_student = find_min_score(marks_dict)
    
    print("\n" + "="*60)
    print("STATISTICAL ANALYSIS")
    print("="*60)
    print(f"Total Students: {len(marks_dict)}")
    print(f"Average Score: {avg:.2f}")
    print(f"Median Score: {median:.2f}")
    print(f"Highest Score: {max_score:.2f} ({max_student})")
    print(f"Lowest Score: {min_score:.2f} ({min_student})")


def display_grade_distribution(grades_dict):
    """Display grade distribution - Task 4"""
    distribution = get_grade_distribution(grades_dict)
    
    print("\n" + "="*60)
    print("GRADE DISTRIBUTION")
    print("="*60)
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = distribution[grade]
        percentage = (count / len(grades_dict) * 100) if grades_dict else 0
        print(f"Grade {grade}: {count:2d} students ({percentage:5.1f}%)")


def display_pass_fail_summary(marks_dict):
    """Display pass/fail analysis - Task 5"""
    passed, failed = get_pass_fail_students(marks_dict)
    
    print("\n" + "="*60)
    print("PASS/FAIL SUMMARY")
    print("="*60)
    print(f"Passed (≥40): {len(passed)} students")
    if passed:
        print(f"  → {', '.join(passed)}")
    
    print(f"Failed (<40): {len(failed)} students")
    if failed:
        print(f"  → {', '.join(failed)}")


def display_results_table(marks_dict, grades_dict):
    """Display formatted results table using f-strings - Task 6"""
    print("\n" + "="*60)
    print("RESULTS TABLE")
    print("="*60)
    print(f"{'Name':<20} {'Marks':>10} {'Grade':>8}")
    print("-" * 60)
    
    for name in sorted(marks_dict.keys()):
        mark = marks_dict[name]
        grade = grades_dict[name]
        print(f"{name:<20} {mark:>10.2f} {grade:>8}")
    
    print("=" * 60)


def export_to_csv(marks_dict, grades_dict):
    """Export results to CSV with custom filename"""
    # Ask user for custom filename
    while True:
        filename = input("\nEnter the filename for CSV export (without .csv): ").strip()
        
        if not filename:
            print("❌ Filename cannot be empty.\n")
            continue
        
        # Add .csv extension if not already present
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Check if file already exists
        if Path(filename).exists():
            overwrite = input(f"File '{filename}' already exists. Overwrite? (yes/no): ").strip().lower()
            if overwrite not in ['yes', 'y']:
                print("❌ Export cancelled.\n")
                return
        
        break
    
    # Export to CSV
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Student Name', 'Marks', 'Grade'])
            for name in sorted(marks_dict.keys()):
                writer.writerow([name, marks_dict[name], grades_dict[name]])
        print(f"✓ Results successfully exported to '{filename}'\n")
    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}\n")


def analyze_gradebook(marks_dict):
    """Main analysis function"""
    if not marks_dict:
        print("❌ No student data available for analysis.")
        return
    
    # Task 4: Create grades dictionary
    grades_dict = create_grades_dict(marks_dict)
    
    # Task 3: Display statistics
    display_statistics(marks_dict, grades_dict)
    
    # Task 4: Display grade distribution
    display_grade_distribution(grades_dict)
    
    # Task 5: Display pass/fail summary
    display_pass_fail_summary(marks_dict)
    
    # Task 6: Display results table
    display_results_table(marks_dict, grades_dict)
    
    # Export to CSV option
    while True:
        export = input("Would you like to export results to CSV? (yes/no): ").strip().lower()
        if export in ['yes', 'y']:
            export_to_csv(marks_dict, grades_dict)
            break
        elif export in ['no', 'n']:
            break
        else:
            print("❌ Please enter 'yes' or 'no'.\n")


def main_menu_loop():
    """Main CLI loop for repeated analysis - Task 6"""
    print_welcome()
    
    while True:
        method = get_input_method()
        
        # Task 2: Get data (manual or CSV)
        if method == '1':
            marks = manual_data_entry()
        else:
            marks = load_csv_data()
        
        if marks:
            # Perform analysis
            analyze_gradebook(marks)
        
        # Task 6: Menu-based loop for repeated runs
        while True:
            choice = input("\n" + "-"*60)
            print("\nWhat would you like to do?")
            print("1. Analyze another set of grades")
            print("2. Exit program")
            choice = input("\nEnter your choice (1 or 2): ").strip()
            
            if choice == '1':
                break
            elif choice == '2':
                print("\n" + "="*60)
                print("Thank you for using GradeBook Analyzer!")
                print("="*60 + "\n")
                return
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")


# Task 1: Project setup and initialization
if __name__ == "__main__":
    main_menu_loop()
