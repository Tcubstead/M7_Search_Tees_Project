from schedule_item import ScheduleItem

class Schedule:
    # Manages course schedules using a tree-based backend (AVL or BST)
    
    def __init__(self, tree_map):
        self.tree_map = tree_map
    
    # Add item to schedule
    def add_item(self, schedule_item):
        crn = schedule_item.get_crn()
        self.tree_map.insert(crn, schedule_item)
    
    # Add course to schedule (alias for add_item)
    def add_course(self, schedule_item):
        self.add_item(schedule_item)
    
    # Remove item by CRN (placeholder)
    def remove_item(self, crn):
        print(f"Note: Removal not implemented in tree-based version")
    
    # Find item by CRN
    def find_by_crn(self, crn):
        return self.tree_map.search(crn)
    
    # Find items by course code
    def find_by_course_code(self, course_code):
        results = []
        for crn, item in self.tree_map.inorder_items():
            if item.get_course_code().upper() == course_code.upper():
                results.append(item)
        return results
    
    # Find items taught by a specific instructor
    def find_by_instructor(self, instructor):
        results = []
        for crn, item in self.tree_map.inorder_items():
            if instructor.lower() in item.get_instructor().lower():
                results.append(item)  # Fixed typo: appened -> append
        return results
    
    # Get all items sorted by CRN
    def get_all_items(self):
        return [item for crn, item in self.tree_map.inorder_items()]
    
    # Get height of the tree
    def get_tree_height(self):
        return self.tree_map.height()
    
    # Get number of items in schedule
    def get_item_count(self):
        count = 0
        for _ in self.tree_map.inorder_items():
            count += 1
        return count
    
    # Display schedule items in sorted order
    def display_all(self):
        items = self.get_all_items()
        if not items:
            print("No items in schedule")
            return
        
        print(f"\n{'=' * 120}")
        print(f"Total Courses: {len(items)}")
        print(f"{'=' * 120}")
        print(f"{'CRN':<10} {'Code':<12} {'Title':<45} {'Instructor':<25} {'Cr':<4} {'Days':<6} {'Time':<16} {'Location'}")
        print(f"{'-' * 120}")
        
        for item in items:
            print(f"{item.crn:<10} {item.course_code:<12} {item.course_title:<45} "
                  f"{item.instructor:<25} {item.credits:<4} {item.days:<6} "
                  f"{item.time:<16} {item.location}")
        
        print(f"{'=' * 120}\n")
    
    # Display statistics about the schedule and tree structure
    def display_statistics(self):
        count = self.get_item_count()
        height = self.get_tree_height()
        
        print(f"\n{'=' * 80}")
        print("Schedule Statistics")
        print(f"{'=' * 80}")
        print(f"Total Courses: {count}")
        print(f"Tree Height: {height}")
        print(f"Tree Type: {type(self.tree_map).__name__}")
        
        if count > 0:
            import math
            optimal_height = math.floor(math.log2(count))
            print(f"Optimal Height: {optimal_height}")
            print(f"Height Efficiency: {(optimal_height / height * 100):.1f}%" if height > 0 else "N/A")
        
        print(f"{'=' * 80}\n")