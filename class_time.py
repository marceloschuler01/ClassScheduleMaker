from teacher import Teacher
import random
from time_without_solution_error import TimeWithoutSolutionError

class ClassTime:

    def __init__(self, time, all_teachers):
        self.time: str = time
        self._teacher: Teacher = None
        self.available_teachers: list[Teacher] = self._evaluate_available_teachers(all_teachers)
        self._already_tried: list[Teacher] = []

    def set_teacher(self, teacher):
        self._teacher = teacher
        self._already_tried.append(teacher)

    def get_teacher(self):
        return self._teacher

    def get_teachers_available_not_tried(self):
        return list(set(self.available_teachers) - set(self._already_tried))

    def _evaluate_available_teachers(self, teachers: list[Teacher]):
        available_teachers = []
        for teacher in teachers:
            if self.time in teacher.available_times:
                available_teachers.append(teacher)
        if len(available_teachers) == 0:
            raise TimeWithoutSolutionError
        return available_teachers

    def is_available(self):
        return self._teacher is None

    def return_teacher_if_there_is_only_one_available(self) -> Teacher | None:
        if len(self.available_teachers) == 1:
            teacher = self.available_teachers[0]
            if teacher.is_in_a_time() and teacher.has_only_one_time_available():
                raise TimeWithoutSolutionError
            return teacher

    def can_you_spontaneously_change_the_teacher(self) -> Teacher | None:
        available_teachers = self.available_teachers.copy()
        available_teachers_not_tried = list(set(available_teachers) - set(self._already_tried))
        for teacher in available_teachers_not_tried:
            if not teacher.is_in_a_time():
                return teacher

    '''def change_teacher(self, teacher: Teacher):
        if teacher in self.available_teachers:

            if self._teacher.has_only_one_time_available():
                return None

            current_teacher_available_times = self.teacher.avaible_times.copy()
            current_teacher_available_times.remove(self.time)

            self._teacher = teacher

            return random.choice(current_teacher_avaible_times)
        return None'''
