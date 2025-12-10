from dataclasses import dataclass


@dataclass
class ScheduleItem:
    #Represents a single course schedule entry
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str
    
    def get_key(self) -> str:
        #Returns a unique key for this schedule item
        return f"{self.subject}_{self.catalog}_{self.section}"
    
    def print(self):
        #Prints formatted details of this schedule item
        print(f"{self.subject:<8} {self.catalog:<8} {self.section:<8} "
              f"{self.component:<10} {self.session:<8} {self.units:<6} "
              f"{self.tot_enrl:<8} {self.cap_enrl:<8} {self.instructor}")