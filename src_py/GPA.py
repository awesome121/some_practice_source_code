"""GPA calculator          Name: Jimmy         Time: Night 3/11/2018"""  

def main():
    """This program includes tree functions 
    grade_point_average, grade_point_value and is_pass
    For example:
         name:'surname givenname givenname'
         grade:'A,B,C+'
    """
    name = input('Student Name: ')
    name_list = name.split()
    
    if len(name_list) == 1:
        print('Sorry name format invalid')
        
    else:
        last_name = name_list[0].upper()
        given_name_length = len(name_list) - 1
        given_name = ''
        for item in name_list[1:]:
            given_name = given_name + ' ' + item
        name_output = last_name + given_name.title()
    
        grade = input('Student grades: ')
        is_pass(grade)
        grade_list = grade.split(',')
        grade_point_average_output = grade_point_average(grade_list)
        output = '{}, GPA = {:.2f}'.format(name_output,
                                          grade_point_average_output)
        
        print(output)
        
        
def is_pass(grade):
    """Take grade and check if it is passed"""
    grade_ = grade.upper()
    return grade_ in 'A+ A A- B+ B B- C+ C C- R'
    

def grade_point_average(grade_list):
    """Calculate the average points from 
    grade_point_value(grade_list) function
    """
    if grade_list == []:
        return None
    else:
        grade_point_list = []
        for grade in grade_list:
            grade_point = grade_point_value(grade)
            grade_point_list.append(grade_point)

        average = sum(grade_point_list) / len(grade_list)
        return float(average)
    

def grade_point_value(grade):
    """Take a letter grade as a string and return a corresponding integer"""
    grade_upper = grade.upper()
    if grade_upper in 'A+, A, or A-':
        return 8
    elif grade_upper in 'B+, B, or B-':
        return 5
    elif grade_upper in 'C+, C, or C-':
        return 2
    elif grade_upper in 'R':
        return 1
    elif grade_upper in 'D or E':
        return -1
    elif grade_upper in 'X':
        return -3
        

main()