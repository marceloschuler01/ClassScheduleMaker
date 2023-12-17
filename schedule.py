from class_time import ClassTime
from teacher import Teacher
from time_without_solution_error import TimeWithoutSolutionError

class Schedule:

    def __init__(self, times: list[ClassTime], teachers: list[Teacher]):
        self.schedule: list[ClassTime] = times
        self.teachers: list[Teacher] = teachers

    def make_schedule(self) -> list[ClassTime]:

        self._schedule_teachers_that_have_only_one_time_available()
        empty_times = self._get_empty_times()

        while len(empty_times) > 0:


            time_to_handle = self._get_time_with_less_teacher_available(empty_times)
            teacher = self._find_best_teacher_for_time(time_to_handle)

            time_to_handle.set_teacher(teacher)
            teacher.set_class_time(time_to_handle.time)

            empty_times = self._get_empty_times()

        return self.schedule

    def _get_time_with_less_teacher_available(self, times) -> ClassTime:

        with_less = times[0]
        for time in times:
            if len(time.get_teachers_available_not_tried()) < len(with_less.get_teachers_available_not_tried()):
                with_less = time
        return with_less

    def _schedule_teachers_that_have_only_one_time_available(self) -> None:
        for teacher in self.teachers:
            if teacher.has_only_one_time_available():
                time = self.get_time(teacher.available_times[0])
                time.set_teacher(teacher)

    def _schedule_times_with_only_one_available_teacher(self) -> None:
        for time in self.schedule:
            teacher = time.return_teacher_if_there_is_only_one_available()
            if teacher:
                time.set_teacher(teacher)
                teacher.set_class_time(time)

    def _get_empty_times(self) -> list[ClassTime]:
        empty_times = []
        for time in self.schedule:
            if time.is_available():
                empty_times.append(time)
        return empty_times

    def get_time(self, time):
        for _time in self.schedule:
            if _time.time == time:
                return _time
        raise KeyError

    def _find_best_teacher_for_time(self, time):
        candidates: list[Teacher] = []

        for teacher in self.teachers:
            if time.time in teacher.available_times:
                candidates.append(teacher)

        for teacher in candidates:
            if not teacher.is_in_a_time():
                return teacher

        # There is no available teacher for the time let's rearrange
        for teacher in candidates:
            old_class_time_of_the_teacher = teacher.class_time
            old_class_time = self.get_time(old_class_time_of_the_teacher)
            new_teacher_for_the_old_class_time = old_class_time.can_you_spontaneously_change_the_teacher()
            if new_teacher_for_the_old_class_time is not None:
                old_class_time.set_teacher(new_teacher_for_the_old_class_time)
                new_teacher_for_the_old_class_time.set_class_time(old_class_time_of_the_teacher)

                return teacher

        raise TimeWithoutSolutionError("Não foi possível encontrar professor para a aula de {}".format(time.time))

