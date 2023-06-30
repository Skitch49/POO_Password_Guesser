import datetime

class Date:
    date = ''

    def __init__(self, date):
        self.date = date

    def display_date(self):
        day, month, year = self.date.split('/')
        return f"{day}/{month}/{year}"
      
    def display_day(self):
        day, month, year = self.date.split('/')
        date_obj = datetime.datetime(int(year), int(month), int(day))
        return date_obj.strftime("%d")
        
    def display_month(self):
        day, month, year = self.date.split('/')
        date_obj = datetime.datetime(int(year), int(month), int(day))
        return date_obj.strftime("%B")

    def display_year(self):
        day, month, year = self.date.split('/')
        date_obj = datetime.datetime(int(year), int(month), int(day))
        return date_obj.strftime("%y")
    
    def polymorphysme(self):
        print('le polymorphysme c\'est génial')



