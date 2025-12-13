from dataclasses import dataclass

@dataclass
class ScheduleItem:
    """Represents a single course schedule entry"""
    crn: str
    course_code: str
    course_title: str
    instructor: str
    credits: str
    days: str
    time: str
    location: str
    
    def get_key(self) -> str:
        """Returns a unique key for this schedule item (CRN)"""
        return self.crn
    
    def __str__(self):
        """Returns formatted string representation of the schedule item"""
        return (f"CRN: {self.crn:<8} | {self.course_code:<10} | {self.course_title:<40} | "
                f"{self.instructor:<20} | {self.credits} cr | {self.days:<5} | "
                f"{self.time:<15} | {self.location}")
    
    def print(self):
        """Prints formatted details of this schedule item"""
        print(self.__str__())
    
    def get_course_code(self) -> str:
        """Returns the course code"""
        return self.course_code
    
    def get_instructor(self) -> str:
        """Returns the instructor name"""
        return self.instructor
    
    def get_crn(self) -> str:
        """Returns the CRN (Course Reference Number)"""
        return self.crn
    
    def matches_course_code(self, code: str) -> bool:
        """Check if this item matches the given course code (case-insensitive)"""
        return self.course_code.lower() == code.lower()
    
    def matches_instructor(self, name: str) -> bool:
        """Check if this item's instructor contains the given name (case-insensitive, partial match)"""
        return name.lower() in self.instructor.lower()