class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
            else:
                pass
        else:
            pass
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips()) if self.trips() else 0
    
    def best_visitor(self):
        if not self.trips():
            return None
        else:
            visitor_list = []
            for visitor in self.visitors():
                visitor_list.append((visitor, visitor.total_visits_at_park(self)))
            visitor_list.sort(key = lambda x: x[1], reverse= True)
            return visitor_list[0][0]
        
    @classmethod
    def most_visited(cls):
        park_list = []
        for park in cls.all:
            park_list.append([park, park.total_visits()])
        park_list.sort(key = lambda x:x[1], reverse = True)
        return park_list[0][0] if park_list[0][0] != 0 else None




def format_check(string):
    month_list = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    date_list = ["1st", "2nd", "3rd"] + [f'{n}th' for n in range(4, 21)] + ["21st", "22nd", "23rd"] + [f'{n}th' for n in range(24,31)] + ["31st"]
    word_list = string.split()
    if word_list[0] in month_list:
        if word_list[1] in date_list:
            return True
    else:
        return False

class Trip:
    all= []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            if format_check(start_date):
                self._start_date = start_date
        else:
            pass

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            if format_check(end_date):
                self._end_date = end_date
        else:
            pass

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            pass
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            pass



class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 15):
            self._name = name
        else:
            pass
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        if park in self.national_parks():
            return len([trip for trip in self.trips() if trip.national_park is park])
        else:
            return 0