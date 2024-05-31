if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
    
    # Step 2: Extract all grades
    grades = sorted(set([student[1] for student in nested_list]))

    # Step 3: Find the second lowest grade
    second_lowest_grade = grades[1]

    # Step 4: Collect names of students with the second lowest grade
    second_lowest_students = sorted([student[0] for student in nested_list if student[1] == second_lowest_grade])

    # Step 5: Print the names of students with the second lowest grade
    for name in second_lowest_students:
        print(name)
