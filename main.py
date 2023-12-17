from teacher import Teacher
from schedule import Schedule
from class_time import ClassTime
from time_without_solution_error import TimeWithoutSolutionError

import pandas as pd

def main():

    filename = input('Digite o nome do arquivo com a definição dos horários: ')

    times_available_teachers = pd.read_excel(filename)
    times_available_teachers = times_available_teachers.replace(pd.NA, None)

    teacher_times = {}
    horarios = list(times_available_teachers['Horarios'].astype('str'))

    for col in times_available_teachers.columns[1:]:
        times = times_available_teachers.loc[times_available_teachers[col] == 'x', 'Horarios'].astype(str).tolist()
        teacher_times[col] = times

    print(teacher_times)

    teachers = []

    for teacher in teacher_times:
        teacher_object = Teacher(name=teacher, available_times=teacher_times[teacher])
        teachers.append(teacher_object)

    times = []

    for time in horarios:
        time_object = ClassTime(time=time, all_teachers=teachers)
        times.append(time_object)

    schedule = Schedule(times=times, teachers=teachers)

    try:
        times = schedule.make_schedule()
        for time in times:
            print('Horário das {} com o professor {}'.format(time.time, time._teacher.name))

        scheds = []
        for time in times:
            sched = {}
            sched['Horário'] = time.time
            sched['Professor'] = time.get_teacher().name
            scheds.append(sched)
        _df = pd.DataFrame(scheds)
        _df = _df.set_index('Horário')
        _df.to_excel('Grade de Horários.xlsx')

    except TimeWithoutSolutionError as e:
        print(str(e))



if __name__ == '__main__':
    main()
