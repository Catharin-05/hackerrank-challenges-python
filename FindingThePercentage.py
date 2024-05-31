if __name__ == '__main__':
    #input
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #finding the average of the entered query name
    query_name = input()
    query_marks = student_marks[query_name]
    average = sum(query_marks)/len(query_marks)
    print(format(average,".2f"))
