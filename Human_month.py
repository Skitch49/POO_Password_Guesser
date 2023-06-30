from Date import Date
import datetime

class Human_month(Date):
    
    def __init__(self, date):
        super().__init__(date)

    def display_human_month(self, language='fr'):
        day, month, year = self.date.split('/')
        date_obj = datetime.datetime(int(year), int(month), int(day))
        if language == 'fr':
            french_months = {
                1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril', 5: 'mai', 6: 'juin',
                7: 'juillet', 8: 'août', 9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'
            }
            month_number = int(date_obj.strftime("%m"))
            return french_months[month_number]
        else:
            english_months = {
                1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
            }
            month_number = int(date_obj.strftime("%m"))
            return english_months[month_number]
        
    