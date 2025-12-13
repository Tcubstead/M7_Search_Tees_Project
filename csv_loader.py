import csv
from schedule_item import ScheduleItem


def load_schedule_from_csv(filename=None, schedule=None):
    """
    Load course schedule data from a CSV file into a Schedule object.
    
    Args:
        filename (str, optional): Path to the CSV file. Defaults to 'courses_2023.csv'
        schedule (Schedule): Schedule object to populate
        
    Returns:
        int: Number of courses loaded
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        ValueError: If CSV has invalid data or missing required columns
    """
    # Default to courses_2023.csv if no filename provided
    if filename is None or filename.strip() == '':
        filename = 'courses_2023.csv'
    
    count = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            # Use DictReader to automatically parse headers
            reader = csv.DictReader(csvfile)
            
            # Strip whitespace from header names
            reader.fieldnames = [field.strip() if field else field for field in reader.fieldnames]
            
            # Check which format the CSV is using
            # Format 1: Simple format (crn, course_code, etc.)
            # Format 2: courses_2023.csv format (Class Nbr, Subject, etc.)
            has_simple_format = 'crn' in reader.fieldnames or 'CRN' in reader.fieldnames
            has_2023_format = 'Class Nbr' in reader.fieldnames
            
            if not has_simple_format and not has_2023_format:
                raise ValueError(f"CSV format not recognized. Found columns: {reader.fieldnames}")
            
            # Process each row
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                try:
                    # Strip whitespace from all fields
                    row = {k: v.strip() if v else '' for k, v in row.items()}
                    
                    # Map fields based on format
                    if has_2023_format:
                        # Map courses_2023.csv columns to ScheduleItem fields
                        crn = str(row.get('Class Nbr', ''))
                        course_code = f"{row.get('Subject', '')}{row.get('Catalog', '')}"
                        course_title = f"{row.get('Subject', '')} {row.get('Catalog', '')} - {row.get('Component', '')}"
                        instructor = row.get('Instructor', 'TBA')
                        credits = row.get('Units', row.get('Total Credits', '0'))
                        days = row.get('Days', '')
                        
                        # Combine start and end times
                        start_time = row.get('Mtg Start', '')
                        end_time = row.get('Mtg End', '')
                        time = f"{start_time}-{end_time}" if start_time and end_time else ''
                        
                        location = row.get('Room', 'TBA')
                    else:
                        # Use simple format columns
                        crn = row.get('crn', row.get('CRN', ''))
                        course_code = row.get('course_code', row.get('Course Code', ''))
                        course_title = row.get('course_title', row.get('Course Title', ''))
                        instructor = row.get('instructor', row.get('Instructor', ''))
                        credits = row.get('credits', row.get('Credits', ''))
                        days = row.get('days', row.get('Days', ''))
                        time = row.get('time', row.get('Time', ''))
                        location = row.get('location', row.get('Location', ''))
                    
                    # Validate required fields are not empty
                    if not crn:
                        print(f"Warning: Row {row_num} missing CRN/Class Nbr, skipping...")
                        continue
                    
                    # Create ScheduleItem from row data
                    item = ScheduleItem(
                        crn=crn,
                        course_code=course_code,
                        course_title=course_title,
                        instructor=instructor,
                        credits=credits,
                        days=days,
                        time=time,
                        location=location
                    )
                    
                    # Add to schedule
                    schedule.add_course(item)
                    count += 1
                    
                except KeyError as e:
                    print(f"Warning: Row {row_num} missing field {e}, skipping...")
                except Exception as e:
                    print(f"Warning: Error processing row {row_num}: {e}, skipping...")
            
            return count
            
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {e}")


def create_sample_csv(filename='courses.csv'):
    """
    Create a sample CSV file with course schedule data.
    
    Args:
        filename (str): Name of the CSV file to create
        
    Returns:
        bool: True if successful, False otherwise
    """
    sample_data = [
        {
            'crn': '12345',
            'course_code': 'CS101',
            'course_title': 'Introduction to Computer Science',
            'instructor': 'Dr. Smith',
            'credits': '3',
            'days': 'MWF',
            'time': '9:00-9:50',
            'location': 'Room 101'
        },
        {
            'crn': '12346',
            'course_code': 'CS102',
            'course_title': 'Data Structures',
            'instructor': 'Dr. Johnson',
            'credits': '4',
            'days': 'TR',
            'time': '10:30-12:00',
            'location': 'Room 202'
        },
        {
            'crn': '12347',
            'course_code': 'MATH201',
            'course_title': 'Calculus I',
            'instructor': 'Prof. Williams',
            'credits': '4',
            'days': 'MWF',
            'time': '11:00-11:50',
            'location': 'Room 305'
        },
        {
            'crn': '12348',
            'course_code': 'CS201',
            'course_title': 'Algorithms',
            'instructor': 'Dr. Smith',
            'credits': '3',
            'days': 'TR',
            'time': '13:00-14:30',
            'location': 'Room 101'
        },
        {
            'crn': '12349',
            'course_code': 'CS301',
            'course_title': 'Database Systems',
            'instructor': 'Dr. Davis',
            'credits': '3',
            'days': 'MWF',
            'time': '14:00-14:50',
            'location': 'Room 203'
        },
        {
            'crn': '12350',
            'course_code': 'CS102',
            'course_title': 'Data Structures',
            'instructor': 'Dr. Johnson',
            'credits': '4',
            'days': 'MWF',
            'time': '15:00-15:50',
            'location': 'Room 202'
        },
        {
            'crn': '12351',
            'course_code': 'ENG101',
            'course_title': 'English Composition',
            'instructor': 'Prof. Martinez',
            'credits': '3',
            'days': 'TR',
            'time': '9:00-10:30',
            'location': 'Room 401'
        },
        {
            'crn': '12352',
            'course_code': 'PHYS101',
            'course_title': 'General Physics',
            'instructor': 'Dr. Brown',
            'credits': '4',
            'days': 'MWF',
            'time': '10:00-10:50',
            'location': 'Room 501'
        }
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['crn', 'course_code', 'course_title', 'instructor', 
                         'credits', 'days', 'time', 'location']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sample_data)
            
        return True
        
    except Exception as e:
        print(f"Error creating sample CSV: {e}")
        return False


def validate_csv_format(filename):
    """
    Validate that a CSV file has the correct format without loading data.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        tuple: (is_valid, message)
    """
    required_columns = {'crn', 'course_code', 'course_title', 'instructor', 
                       'credits', 'days', 'time', 'location'}
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Check if all required columns exist
            if not required_columns.issubset(reader.fieldnames):
                missing = required_columns - set(reader.fieldnames)
                return False, f"Missing required columns: {missing}"
            
            # Count rows
            row_count = sum(1 for _ in reader)
            
            return True, f"Valid format with {row_count} data rows"
            
    except FileNotFoundError:
        return False, f"File '{filename}' not found"
    except Exception as e:
        return False, f"Error reading file: {e}"