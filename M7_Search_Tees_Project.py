#Thomas Cubstead
#M7_Search_Trees_Project
#main
#12/10/25
#

"""
main.py
Main program for Course Schedule System with BST and AVL tree comparison.
Provides interactive menu for data management and tree height analysis.
"""

import os
from SearchTrees import BSTMap, AVLTreeMap
from schedule import Schedule
from schedule_item import ScheduleItem
from csv_loader import load_schedule_from_csv, create_sample_csv


def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*80}")
    print(f"{title.center(80)}")
    print(f"{'='*80}\n")


def display_menu():
    """Display the main menu"""
    print_header("Course Schedule System - BST vs AVL Comparison")
    print("1.  Load Data from CSV")
    print("2.  Display All Courses (BST)")
    print("3.  Display All Courses (AVL)")
    print("4.  Search by CRN")
    print("5.  Search by Course Code")
    print("6.  Search by Instructor")
    print("7.  Display Tree Heights")
    print("8.  Compare BST vs AVL Heights")
    print("9.  Display Statistics")
    print("10. Create Sample CSV")
    print("0.  Exit")
    print(f"{'='*80}")


def load_data_menu(bst_schedule, avl_schedule):
    """Handle loading data from CSV"""
    print_header("Load Data from CSV")
    filename = input("Enter CSV filename (or press Enter for 'courses_2023.csv'): ").strip()
    
    if not filename:
        filename = "courses_2023.csv"
    
    if not os.path.exists(filename):
        print(f"\nError: File '{filename}' not found.")
        print("Tip: Use option 10 to create a sample CSV file.")
        return False
    
    try:
        # Create new tree maps and schedules
        new_bst = BSTMap()
        new_avl = AVLTreeMap()
        temp_bst_schedule = Schedule(new_bst)
        temp_avl_schedule = Schedule(new_avl)
        
        # Load into BST
        print(f"\nLoading into BST...")
        bst_count = load_schedule_from_csv(filename, temp_bst_schedule)
        
        # Load into AVL
        print(f"Loading into AVL...")
        avl_count = load_schedule_from_csv(filename, temp_avl_schedule)
        
        # Update schedules
        bst_schedule.tree_map = new_bst
        avl_schedule.tree_map = new_avl
        
        print(f"\n✓ Successfully loaded {bst_count} courses into both trees!")
        print(f"  BST Height: {bst_schedule.get_tree_height()}")
        print(f"  AVL Height: {avl_schedule.get_tree_height()}")
        
        return True
    
    except Exception as e:
        print(f"\nError loading data: {str(e)}")
        return False


def search_by_crn(bst_schedule, avl_schedule):
    """Search for a course by CRN"""
    print_header("Search by CRN")
    crn = input("Enter CRN: ").strip()
    
    print(f"\nSearching in BST...")
    item = bst_schedule.find_by_crn(crn)
    
    if item:
        print(f"\n✓ Found:")
        print(f"  {item}")
    else:
        print(f"\n✗ No course found with CRN: {crn}")


def search_by_course_code(bst_schedule, avl_schedule):
    """Search for courses by course code"""
    print_header("Search by Course Code")
    code = input("Enter course code: ").strip()
    
    print(f"\nSearching in BST...")
    items = bst_schedule.find_by_course_code(code)
    
    if items:
        print(f"\n✓ Found {len(items)} course(s):")
        for item in items:
            print(f"  {item}")
    else:
        print(f"\n✗ No courses found with code: {code}")


