from schedule_item import ScheduleItem

class Schedule:
    def __init__(self, tree_map):
        self.tree_map = tree_map

    def add_item(self, schedule_item):
        crn = schedule_item.get_crn()
        self.tree_map.insert(crn, schedule_item)

    def remove_item(self, crn):
        print(f"Note: Removal not implemented in tree-based version")

    def find_by_crn(self, crn):
        return self.tree_map.search(crn)

    def find_by_course_code(self, course_code):
        results = []
        for crn, item in self.tree_map.inorder_items():
            if instructor.lower() in item.get_instructor().lower():
                results.append(item)
        return results