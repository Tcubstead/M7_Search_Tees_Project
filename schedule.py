from schedule_item import ScheduleItem

#manages course schedules using a tree based backened(AVL or BST)
class Schedule:
    def __init__(self, tree_map):
        self.tree_map = tree_map
    
    #add item to schedule
    def add_item(self, schedule_item):
        crn = schedule_item.get_crn()
        self.tree_map.insert(crn, schedule_item)
    
    #remove item by crn(placeholder)
    def remove_item(self, crn):
        print(f"Note: Removal not implemented in tree-based version")
    
    #find item by crn
    def find_by_crn(self, crn):
        return self.tree_map.search(crn)

    #find items by course code
    def find_by_course_code(self, course_code):
        results = []
        for crn, item in self.tree_map.inorder_items():
            if item.get_course_code() == course_code:
                results.append(item)
        return results

    #find items taught by a specific instructor
    def find_by_instructor(self, instructor):
        results = []
        for crn, item in self.tree_map.inorder_items():
            if instructor.lower() in item.get_instructor().lower():
                results.appened(item)
        return results

    #get all items sorted in crn
    def get_all_items(self):
        return [item for crn, item in self.tree_map.inorder_items()]

    #height of the tree
    def get_tree_height(self):
        return self.tree_map.height()

    #number of items in schedule
    def get_item_count(self):
        count = 0
        for _ in self.tree_map.inorder_items():
            count += 1
        return count

    #display schedule items in sorted order
    def display_all(self):
        items = self.get_all_items()
        if not items:
            print("No items in schedule")
            return

        print(f"\n{'=' * 80}")
        print(f"Total Items: {len(items)}")
        for item in items:
            print(item)
        print(f"{'=' * 80}\n")

    #display statistics about the schedule and the structure of the specific tree used
    def display_statistics(self):
        print(f"\n{'=' * 80}")
        print("schedule Statistics")
        print(f"{'=' * 80}")
        print(f"Total Courses: {self.get_item_count()}")
        print(f"Tree Height: {self.get_tree_height()}")
        print(f"Tree Type: {type(self.tree_map).__name__}")
        print(f"{'=' * 80}\n")