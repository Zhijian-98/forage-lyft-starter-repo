from battery.battery import Battery
from datetime import datetime

class Spindler_batter(Battery):
    def __init__(self, last_sevice_date, current_date):
        self.last_service_date = last_sevice_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False