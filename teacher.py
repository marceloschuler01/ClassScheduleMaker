
class Teacher:

    def __init__(self, name: str, available_times: list[str]=None):
        self.name = name
        self.available_times = available_times
        self.class_time: str = None
        self.already_tried = []

    def set_class_time(self, time):
        self.class_time = time
        self.already_tried.append(time)

    def is_in_a_time(self):
        return False if self.class_time is None else True

    def has_only_one_time_available(self) -> bool:
        return len(self.available_times) == 1

    '''def can_you_spontaneously_change_your_time(self) -> ClassTime | None:
        if self.has_only_one_time_available():
            return None
        available_times = self.available_times.copy()
        available_times_not_tried = list(set(available_times) - set(self.already_tried))
        for time in available_times_not_tried:
            if time.is_available():
                return time
    '''
