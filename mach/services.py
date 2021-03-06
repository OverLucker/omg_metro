from mach.models import ScheduleGateway, MessageGateway, PlacesGateway


class ServiceLayer:
    @classmethod
    def get_all_messages(cls, *args, **kwargs):
        return MessageGateway.get_last_10(*args, **kwargs)

    @classmethod
    def get_all_places(cls, *args, **kwargs):
        return PlacesGateway.get(*args, **kwargs)

    @classmethod
    def create_new_message(cls, *args, **kwargs):
        return MessageGateway.insert(*args, **kwargs)

    @classmethod
    def get_all_schedules(cls, *args, **kwargs):
        return ScheduleGateway.get_current(*args, **kwargs)
