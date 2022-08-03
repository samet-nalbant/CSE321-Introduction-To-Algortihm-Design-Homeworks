class Course:
    def __init__(self,start_init,finish_init):
        self.start = start_init
        self.finish = finish_init
        
def find_max_course(courses):
    count = 1
    n = len(courses)
    i = 0
    for j in range(n):
        if courses[j].start >= courses[i].finish:
            i = j
            count += 1
    return count


def order_by_finish_time(courses):
    for i in range(0,len(courses)):
        for j in range(i, len(courses)):
            if courses[i].finish > courses[j].finish :
                temp = courses[i]
                courses[i] = courses[j]
                courses[j] = temp


course_list = [Course(1,2),Course(3,4),Course(0,6),Course(5,7),Course(8,9),Course(5,9)]

print("Maximum number of courses a student can attandend: {}".format(find_max_course(course_list)))