#Thomas Cubstead
#M7_Search_Trees_Project
#main
#12/10/25
#This program implements a course schedule system using both a Binary Search Tree (BST) and an AVL tree.

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


def search_by_instructor(bst_schedule, avl_schedule):
    """Search for courses by instructor"""
    print_header("Search by Instructor")
    instructor = input("Enter instructor name: ").strip()
    
    print(f"\nSearching in BST...")
    items = bst_schedule.find_by_instructor(instructor)
    
    if items:
        print(f"\n✓ Found {len(items)} course(s):")
        for item in items:
            print(f"  {item}")
    else:
        print(f"\n✗ No courses found for instructor: {instructor}")


def display_tree_heights(bst_schedule, avl_schedule):
    """Display height information for both trees"""
    print_header("Tree Height Information")
    
    bst_height = bst_schedule.get_tree_height()
    avl_height = avl_schedule.get_tree_height()
    bst_count = bst_schedule.get_item_count()
    avl_count = avl_schedule.get_item_count()
    
    print(f"BST (Binary Search Tree):")
    print(f"  Items: {bst_count}")
    print(f"  Height: {bst_height}")
    if bst_count > 0:
        print(f"  Height/log₂(n): {bst_height / max(1, bst_count.bit_length() - 1):.2f}")
    
    print(f"\nAVL (Balanced Tree):")
    print(f"  Items: {avl_count}")
    print(f"  Height: {avl_height}")
    if avl_count > 0:
        print(f"  Height/log₂(n): {avl_height / max(1, avl_count.bit_length() - 1):.2f}")
    
    print(f"\nHeight Difference: {abs(bst_height - avl_height)} edges")


def compare_heights(bst_schedule, avl_schedule):
    """Compare BST and AVL tree heights with analysis"""
    print_header("BST vs AVL Height Comparison")
    
    bst_height = bst_schedule.get_tree_height()
    avl_height = avl_schedule.get_tree_height()
    n = bst_schedule.get_item_count()
    
    if n == 0:
        print("No data loaded. Please load data first (Option 1).")
        return
    
    import math
    optimal_height = math.floor(math.log2(n))
    avl_max_theoretical = math.ceil(1.44 * math.log2(n + 2))
    
    print(f"Number of Nodes: {n}")
    print(f"Optimal Height (⌊log₂(n)⌋): {optimal_height}")
    print(f"AVL Maximum Theoretical: {avl_max_theoretical} (≤ 1.44 × log₂(n+2))")
    print(f"\nBST Height: {bst_height}")
    print(f"AVL Height: {avl_height}")
    print(f"\nDifference: {abs(bst_height - avl_height)} edges")
    
    # Calculate efficiency ratios
    bst_efficiency = (optimal_height / bst_height * 100) if bst_height > 0 else 100
    avl_efficiency = (optimal_height / avl_height * 100) if avl_height > 0 else 100
    
    print(f"\n{'─'*80}")
    print("Analysis:")
    print(f"{'─'*80}")
    
    print(f"\n1. BST Performance:")
    print(f"   • Height: {bst_height} (vs optimal {optimal_height})")
    print(f"   • Height excess: {bst_height - optimal_height} edges")
    print(f"   • Efficiency: {bst_efficiency:.1f}% of optimal")
    print(f"   • The BST height depends on insertion order (CRN sequence)")
    print(f"   • Worst case: O(n) for degenerate tree (becomes linked list)")
    print(f"   • Average case: O(log n) for random insertions")
    
    print(f"\n2. AVL Performance:")
    print(f"   • Height: {avl_height} (vs optimal {optimal_height})")
    print(f"   • Height excess: {avl_height - optimal_height} edges")
    print(f"   • Efficiency: {avl_efficiency:.1f}% of optimal")
    print(f"   • AVL maintains balance: height ≤ 1.44 × log₂(n+2)")
    print(f"   • Guaranteed O(log n) for all operations")
    print(f"   • Self-balancing through rotations")
    
    print(f"\n3. Comparison:")
    if bst_height == avl_height:
        print(f"   • Both trees have the same height!")
        print(f"   • This suggests the CRNs created a naturally balanced BST.")
        print(f"   • With {n} courses, this is somewhat unusual.")
    elif bst_height > avl_height:
        diff_pct = ((bst_height - avl_height) / avl_height * 100) if avl_height > 0 else 0
        speedup = bst_height / avl_height if avl_height > 0 else 1
        print(f"   • BST is {bst_height - avl_height} edges taller ({diff_pct:.1f}% taller)")
        print(f"   • AVL's balancing reduced tree height significantly")
        print(f"   • AVL search is approximately {speedup:.1f}x faster in worst case")
        print(f"   • With {n} courses, this difference is substantial!")
    else:
        print(f"   • Unexpected: BST is shorter than AVL")
        print(f"   • This suggests the CRNs were in optimal insertion order")
    
    print(f"\n4. Practical Impact on {n} Courses:")
    print(f"   • BST worst-case search: ~{bst_height} comparisons")
    print(f"   • AVL worst-case search: ~{avl_height} comparisons")
    if bst_height > avl_height:
        saved = bst_height - avl_height
        print(f"   • AVL saves up to {saved} comparisons per search!")
        print(f"   • For 1000 searches: ~{saved * 1000:,} fewer comparisons")
    
    print(f"\n5. Why The Difference Exists:")
    print(f"   • CRNs (Class Numbers) determine insertion order")
    print(f"   • If CRNs are sequential/sorted → BST degenerates")
    print(f"   • If CRNs are random → BST stays more balanced")
    print(f"   • AVL guarantees balance regardless of CRN pattern")
    print(f"   • Real course data often has patterns (sorted sections, etc.)")


def display_statistics(bst_schedule, avl_schedule):
    """Display detailed statistics for both trees"""
    print_header("Schedule Statistics")
    
    print("BST Schedule:")
    bst_schedule.display_statistics()
    
    print("\nAVL Schedule:")
    avl_schedule.display_statistics()


def create_sample_csv_menu():
    """Handle creating a sample CSV"""
    print_header("Create Sample CSV")
    filename = input("Enter filename (or press Enter for 'courses.csv'): ").strip()
    
    if not filename:
        filename = "courses.csv"
    
    if os.path.exists(filename):
        response = input(f"\nFile '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled.")
            return
    
    if create_sample_csv(filename):
        print(f"\n✓ Sample CSV created successfully!")
        print(f"  You can now load it using option 1.")
    else:
        print(f"\n✗ Failed to create sample CSV.")

def main():
    """Main program loop"""
    # Initialize both tree types
    bst_schedule = Schedule(BSTMap())
    avl_schedule = Schedule(AVLTreeMap())
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            load_data_menu(bst_schedule, avl_schedule)
        elif choice == '2':
            print_header("All Courses (BST)")
            bst_schedule.display_all()
        elif choice == '3':
            print_header("All Courses (AVL)")
            avl_schedule.display_all()
        elif choice == '4':
            search_by_crn(bst_schedule, avl_schedule)
        elif choice == '5':
            search_by_course_code(bst_schedule, avl_schedule)
        elif choice == '6':
            search_by_instructor(bst_schedule, avl_schedule)
        elif choice == '7':
            display_tree_heights(bst_schedule, avl_schedule)
        elif choice == '8':
            compare_heights(bst_schedule, avl_schedule)
        elif choice == '9':
            display_statistics(bst_schedule, avl_schedule)
        elif choice == '10':
            create_sample_csv_menu()
        elif choice == '0':
            print_header("Thank you for using Course Schedule System!")
            print("Goodbye!\n")
            break
        else:
            print("\n✗ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
