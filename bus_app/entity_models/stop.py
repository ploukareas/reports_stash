import datetime


class stop:
    def __init__(self, stop_name, location, bus_stop_id=None):
        self.bus_stop_id = bus_stop_id  if bus_stop_id is not None else None
        self.stop_name = stop_name  
        self.location = location 

    def __repr__(self) -> str:
        return f"Stop details:[ bus_stop_id: {self.bus_stop_id}, stop_name: {self.stop_name}, location: {self.location} ]"