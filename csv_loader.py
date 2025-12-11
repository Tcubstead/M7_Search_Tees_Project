"""
csv_loader.py
Loads course data from CSV files into Schedule objects.
Uses csv.DictReader for robust CSV parsing.
"""

import csv
from schedule_item import ScheduleItem

# Load schedule from CSV file
def load_schedule_from_csv(filename, schedule):

    count = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Auto-detect CSV format
            fieldnames = [f.strip() for f in reader.fieldnames]
            
            # Format 1: Simple format (crn, course_code, title, instructor)
            if 'crn' in fieldnames and 'course_code' in fieldnames:
                for row in reader:
                    if not any(row.values()):
                        continue
                    item = ScheduleItem(
                        crn=row['crn'].strip(),
                        course_code=row['course_code'].strip(),
                        title=row['title'].strip(),
                        instructor=row['instructor'].strip()
                    )
                    schedule.add_item(item)
                    count += 1
            
            # Format 2: Real course data (Class Nbr, Subject, Catalog, Component, Instructor)
            elif 'Class Nbr' in fieldnames or 'Class_Nbr' in fieldnames:
                for row in reader:
                    if not any(row.values()):
                        continue
                    
                    # Extract fields with fallbacks
                    class_nbr = row.get('Class Nbr', row.get('Class_Nbr', '')).strip()
                    subject = row.get('Subject', '').strip()
                    catalog = row.get('Catalog', '').strip()
                    component = row.get('Component', '').strip()
                    instructor = row.get('Instructor', 'Staff').strip()
                    
                    # Skip if no class number
                    if not class_nbr:
                        continue
                    
                    # Build course code
                    course_code = f"{subject}{catalog}" if subject and catalog else "UNKNOWN"
                    
                    # Build title from available info
                    title = f"{subject} {catalog}"
                    if component:
                        title += f" ({component})"
                    
                    item = ScheduleItem(
                        crn=class_nbr,
                        course_code=course_code,
                        title=title,
                        instructor=instructor if instructor else "Staff"
                    )
                    schedule.add_item(item)
                    count += 1
            
            else:
                raise ValueError(f"CSV format not recognized. Available fields: {fieldnames}")
        
        return count
    
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {filename}")
    except Exception as e:
        raise Exception(f"Error loading CSV: {str(e)}")

# Create a sample CSV file for testing
def create_sample_csv(filename):

    sample_data = [
        {'crn': '12345', 'course_code': 'CS101', 'title': 'Introduction to Computer Science', 'instructor': 'Dr. Smith'},
        {'crn': '12346', 'course_code': 'CS102', 'title': 'Data Structures', 'instructor': 'Dr. Johnson'},
        {'crn': '12347', 'course_code': 'CS201', 'title': 'Algorithms', 'instructor': 'Dr. Williams'},
        {'crn': '12348', 'course_code': 'CS202', 'title': 'Database Systems', 'instructor': 'Dr. Brown'},
        {'crn': '12349', 'course_code': 'CS301', 'title': 'Operating Systems', 'instructor': 'Dr. Davis'},
        {'crn': '12350', 'course_code': 'CS302', 'title': 'Computer Networks', 'instructor': 'Dr. Miller'},
        {'crn': '12351', 'course_code': 'CS401', 'title': 'Artificial Intelligence', 'instructor': 'Dr. Wilson'},
        {'crn': '12352', 'course_code': 'CS402', 'title': 'Machine Learning', 'instructor': 'Dr. Moore'},
        {'crn': '12353', 'course_code': 'MATH201', 'title': 'Discrete Mathematics', 'instructor': 'Dr. Taylor'},
        {'crn': '12354', 'course_code': 'MATH301', 'title': 'Linear Algebra', 'instructor': 'Dr. Anderson'},
        {'crn': '12355', 'course_code': 'CS103', 'title': 'Software Engineering', 'instructor': 'Dr. Smith'},
        {'crn': '12356', 'course_code': 'CS203', 'title': 'Web Development', 'instructor': 'Dr. Johnson'},
        {'crn': '12357', 'course_code': 'CS303', 'title': 'Mobile App Development', 'instructor': 'Dr. Williams'},
        {'crn': '12358', 'course_code': 'CS403', 'title': 'Cloud Computing', 'instructor': 'Dr. Brown'},
        {'crn': '12359', 'course_code': 'CS404', 'title': 'Cybersecurity', 'instructor': 'Dr. Davis'},
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['crn', 'course_code', 'title', 'instructor'])
            writer.writeheader()
            writer.writerows(sample_data)
        print(f"Sample CSV created: {filename}")
        print(f"Note: This is test data. Your main file 'courses_2023.csv' has 521 real courses.")
        return True
    except Exception as e:
        print(f"Error creating sample CSV: {str(e)}")
        return False