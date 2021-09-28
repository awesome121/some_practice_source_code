def messy_string(data):
    """Take a list of string and return the number of non-string"""
    count = 0
    for i in range(len(data)):
        element_as_list = list(data[i])
        for character in element_as_list:
            if type(character) != str:
                count += 1
    return count
print(messy_string(['x', 'y2y', 'zz%z']))


def scale_up(nums, scale_factor):
    """Scale up each element in the list nums by given scale_factor"""
    for num in nums:
        num = num * scale_factor

marks = [55.3, 37.4, 85.2]
print('Marks:', marks)
scale_up(marks, 1.2)
print('Scale maeks:', marks)



def BMI():
    """To calculate your body index"""
    weight_float = float(input('Please type up your weight(kg): '))
    height_float = float(input('Now please type up your height(cm): '))
    height = height_float / 100
    body_mass_index = weight_float / (height ** 2)
    BMI_ = str(body_mass_index)
    print('\nThank you very much!\n\nYour Body Mass Index is: ' + BMI_)
BMI()





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




def maximum(data):
    """find the maximum num in the list using iteration"""
    current_max = data[0]
    for num in data:
        if num >= current_max:
            current_max = num
    return  current_max



def minimum(data):
    """find the minimum num in the list using iteration"""
    current_min = data[0]
    for num in data:
        if num <= current_min:
            current_min = num
    return current_min



def max_and_min(data):
    """find the max and min in a list of data using one iteration"""
    current_max = data[0]
    current_min = data[0]
    for num in data:
        if num >= current_max:
            current_max = num
        elif num <= current_min:
            current_min = num
    return current_max, current_min



def sum_sqaured(data):
    """Find the sum of the data of squared elements using iteration"""
    total = 0
    for element in data:
        total += element * element
    return total
print(sum_sqaured([1, 2,3]))



def nearest_pair(data):
    """Find the nearest pair in a list of data,
    if more than one pair, return the first one
    """
    
    for i in range():
        if data[i] - data[0] < £º



def test_something(something):
    """This pfunction is just testing boolean"""
    if True:
        print('YES')
    else:
        print('HUh?')
something = False
test_something(something)



consonant 
moving the first letter to the end of the word and adding the string "eeoow", eg, turtle -> urtleteeoow



    
non-consonant 
the English word followed by "meeoow", eg, egg -> eggmeeoow and 121word -> 121wordmeeoow

def english_sentence(string):
    """Take a string of latin words and return it with English version"""
    alist = []
    string_list = string.rstrip().split(' ')
    string_list_lower = [item.lower() for item in string_list]
    for item in string_list_lower:
        english_version = english_word(item)   
        alist.append(english_version)
    return ' '.join(alist)
    
    
def english_word(item):
    """Take a latin word and return its english version"""
    if not item[0].isalpha():
        result = item[:-6]
    elif item[-6:] == 'meeoow' and item[0] in 'aeiou':
        word1 = 'm' + item[:-6]
        word2 = item[:-6]
        result = '({} or {})'.format(word1, word2)    
    elif item[-5:] == 'eeoow' and item[-6] not in 'aeiou':
        result = item[-6] + item[0:-6]
    return result

    
    
sentence = "oneeoow oneeoow oneeoow "
english = english_sentence(sentence)
print(english)



def cat_latin_from_sentence(string):
    """Take a string and return it with latin version"""
    alist = []
    string_list = string.split(' ')
    string_list_lower = [item.lower() for item in string_list]
    for item in string_list_lower:
        latin_version = cat_latin_word(item)   
        alist.append(latin_version)
    return ' '.join(alist)
            
            
            
    
def cat_latin_word(item):
    """convert a word into latin version"""
    if item[0] in 'aeiou':
        result = item + 'meeoow'
    elif not item[0].isalpha():
        result = item + 'meeoow'
    else:
        result = item[1:] + item[0] + 'eeoow'
    return result
cat_latin = cat_latin_from_sentence('Frank said "Wow" this test sucks!')                                                                
print(cat_latin)





"""A limited version of the conversion function from Latin to English
   Jimmy
   Dawn 16/11/2018
"""
def file_in_english(filename, character_limit):
    """A limited version of the conversion from Latin to English"""
    content = open(filename)
    result = ''
    line_with_newline = content.readline()
    length = 0
    while length < character_limit and line_with_newline != '':
        string = line_with_newline.rstrip()
        string_english = english_sentence(string) + '\n'
        result = result + string_english
        length += len(string_english)
        line_with_newline = content.readline()
    if length > character_limit:
        result_list = result.rstrip().split('\n')
        result_list[-1] = '-Output limit exceeded-'
        result = '\n'.join(result_list)
    elif length == character_limit:
        result_list = result.split('\n')
        result_list[-1] = '-Output limit exceeded-'
        result = '\n'.join(result_list)        
    return result
            
            
    
        
        
def english_sentence(string):
    """Take a string of latin words and return it with English version"""
    alist = []
    string_list = string.rstrip().split(' ')
    string_list_lower = [item.lower() for item in string_list]
    for item in string_list_lower:
        english_version = english_word(item)   
        alist.append(english_version)
    return ' '.join(alist)
    
    
def english_word(item):
    """Take a latin word and return its english version"""
    if not item[:1].isalpha():
        result1 = item[:-6]
        result2 = 'm' + item[:-6]
        result = '({} or {})'.format(result2, result1)
    elif item[-6:] == 'meeoow' and item[0] in 'aeiou':
        word1 = 'm' + item[:-6]
        word2 = item[:-6]
        result = '({} or {})'.format(word1, word2)    
    elif item[-5:] == 'eeoow' and item[-6] not in 'aeiou':
        result = item[-6] + item[0:-6]
    return result

ans = file_in_english('C:/Users/Administrator/Desktop/big_test.txt', 8)
print(ans)
	
ans = file_in_english('C:/Users/Administrator/Desktop/big_test.txt', 390)
print(ans)
	
	
	
ans = file_in_english('C:/Users/Administrator/Desktop/test1.txt', 10000)
print(ans)







"""A limited version of the conversion function from Latin to English
   Jimmy
   Dawn 16/11/2018
"""
def file_in_english(filename, character_limit):
    """A limited version of the conversion from Latin to English"""
    import urllib.request
    web_page = urllib.request.urlopen(filename)
    line_with_newline = web_page.readline().decode("utf-8")
    result = ''
    length = 0
    while length < character_limit and line_with_newline != '':
        string = line_with_newline.rstrip()
        string_english = english_sentence(string) + '\n'
        result = result + string_english
        length += len(string_english)
        line_with_newline = web_page.readline().decode("utf-8")
    if length > character_limit:
        result_list = result.rstrip().split('\n')
        result_list[-1] = '-Output limit exceeded-'
        result = '\n'.join(result_list)
    elif length == character_limit:
        result_list = result.split('\n')
        result_list[-1] = '-Output limit exceeded-'
        result = '\n'.join(result_list)        
    return result
            
            
    
        
        
def english_sentence(string):
    """Take a string of latin words and return it with English version"""
    alist = []
    string_list = string.rstrip().split(' ')
    string_list_lower = [item.lower() for item in string_list]
    for item in string_list_lower:
        english_version = english_word(item)   
        alist.append(english_version)
    return ' '.join(alist)
    
    
def english_word(item):
    """Take a latin word and return its english version"""
    if not item[:1].isalpha():
        result1 = item[:-6]
        result2 = 'm' + item[:-6]
        result = '({} or {})'.format(result2, result1)
    elif item[-6:] == 'meeoow' and item[0] in 'aeiou':
        word1 = 'm' + item[:-6]
        word2 = item[:-6]
        result = '({} or {})'.format(word1, word2)    
    elif item[-5:] == 'eeoow' and item[-6] not in 'aeiou':
        result = item[-6] + item[0:-6]
    return result

url = "https://quiz2018.csse.canterbury.ac.nz/pluginfile.php/23427/question/questiontext/95066/7/30347/big_test.txt"
print(file_in_english(url, 390))



def print_half_number(number):
    """Prints a number halved with exception."""
    try:
        half = number / 2
        print(half)
    except:
        print("Invalid number used!")

print_half_number('four')





"""This program is to graph the data average and max     Jimmy    1/12/2018"""
from datetime import date
LIMIT_VALUE = 50
EXCCEDED_DAY_INFORMATION = '{} days out of {} exceeded 50 ug/m3.'


def main():
    """The main function of this program"""
    lines_loaded, filename = open_function()
    load_file(filename, lines_loaded)
    lines_ready_process_list = line_ready_to_process(lines_loaded)
    summary_tuple_list = summarise_daily(lines_ready_process_list)
    exceeded_day_num(summary_tuple_list)
    print('=-'*30 + '\n' + 'Graph of Daily Maximums\n' + '=-'*30)
    display_maximum_graph(summary_tuple_list)
    print('\n' + '=-'*30 + '\n' + 'Graph of Daily Averages\n' + '=-'*30)
    display_average_graph(summary_tuple_list)
    
    
     
def open_function():
    """Open a file and get data"""
    is_opened = False
    while not is_opened:
        filename = input('Filename? ')
        try:
            infile = open(filename)
            is_opened = True
        except FileNotFoundError:
            print('Invalid file name')
            is_opened = False
    return infile.readlines(), filename
    
    
def load_file(filename, lines_loaded):
    """Print summary of lines loaded"""
    print('=-'*30)
    print('Loaded {} ok.'.format(filename))
    print('{} lines in file.'.format(len(lines_loaded)))
    print('=-'*30)
    print()
    
    
def line_ready_to_process(lines_loaded):
    """Get a list of lines
       Ask how many lines would be processed
       retrun lines_process_list which is ready to be processes
    """
    quantity_lines_process = -1
    while quantity_lines_process <= 0 or quantity_lines_process > len(lines_loaded):
        print('{} lines in file'.format(len(lines_loaded)))
        quantity_lines_process = int(input('Process first n lines, n=? '))
        if quantity_lines_process <= 0 or quantity_lines_process > len(lines_loaded):
            print('Invalid n.')
        print()
    lines_ready_process_list = []
    for i in range(0, quantity_lines_process):
        lines_ready_process_list.append(lines_loaded[i])
    return lines_ready_process_list


def exceeded_day_num(summary_tuple_list):
    """Take a list of tuples
       print how many days out of limit
    """
    days = 0
    for item in summary_tuple_list:
        if item[2] is not None and item[2] > LIMIT_VALUE:
            days += 1
    print(EXCCEDED_DAY_INFORMATION.format(days, len(summary_tuple_list)))
    print()
    
#---------------------------------------------------------------------------    
def summarise_daily(lines):
    """Take a list of lines
       Return a list of tuples that containing date, max, average
    """
    summary_tuple_list = []
    for line in lines:
        line = line.strip().split(',')
        date_time = line[0]
        data = line[1:]
        iso_date = date(int(date_time[0:4]), int(date_time[5:7]),
        int(date_time[8:10]))
        current_max = daily_max_function(data)
        data_average = daily_average_function(data)
        summary_tuple_list.append((iso_date, current_max, data_average))
    return summary_tuple_list
    
    
def daily_max_function(data):
    """Return the maximum in data"""
    data_list = []
    for num in data:
        num_float = float(num)
        if num_float >= 0:
            data_list.append(num_float)
    if len(data_list) > 0:
        current_max = max(data_list)
    else:
        current_max = None
    return current_max
        
        
def daily_average_function(data):
    """Return the average in data"""
    if len(data) > 0:
        data_total = 0
        i = 0
        for num in data:
            if float(num) > 0:
                data_total += float(num)
                i += 1
        if i == 0:
            data_average = None
        else:
            data_average = data_total / i
    else:
        data_average = None
    return data_average
    
    
#----------------------------------------------------------------------    

def display_maximum_graph(summary_tuple_list):
    """Take a list of tuples and print the maximum graph of them"""
    infinite = float('-inf')
    for item in summary_tuple_list:
        if item[1] is not None and item[1] > infinite:
            infinite = item[1]
    for (iso_date, daily_max, daily_average) in summary_tuple_list:
        daily_average = daily_average
        if daily_max is not None:
            graph = '=' * int(daily_max / infinite * 40)
            template = '{} {:6.2f} {}'
            print(template.format(iso_date, daily_max, graph))
        else:
            print(iso_date)
    

def display_average_graph(summary_tuple_list):
    """Take a list of tuples and print the maximum graph of them"""
    infinite = float('-inf')
    for item in summary_tuple_list:
        if item[2] is not None and item[2] > infinite:
            infinite = item[2]
    for (iso_date, daily_max, daily_average) in summary_tuple_list:
        daily_max = daily_max
        if daily_average is not None:
            graph = '=' * int(daily_average / infinite * 40)
            template = '{} {:6.2f} {}'
            print(template.format(iso_date, daily_average, graph))
        else:
            print(iso_date)

    
main()








"""A program to show data from students course information   
   Total functions: 10
   Jimmy
   22/12/2018
"""


#===========================================================================
#Core functions:

def main():
    """Main function of the program"""
    records = records_from_file()
    command = None
    while command != 'q':
        command, command_type, parameter = command_process(records)
        if command_type == 'list' and parameter == 'courses':
            print_courses(records)
        elif command_type == 'list' and parameter == 'students':
            print_students(records)
        elif command_type == 'list' and parameter == 'rolls':
            print_course_rolls(records)
        elif command_type == 'clashes' and parameter in all_courses(records):
            print_clashes(records, parameter)
    print('Adios Changxing')
    

def command_process(records):
    """Sub-function of the main function
       Process command
       return a parameter in string type
    """
    command = input('Command? (q to quit): ')
    command_type = command.split()[0]
    parameter = ''.join(command.split()[1:])
    if command_type not in ['list', 'clashes'] and command_type != 'q':
        print('Command invalid!')
    elif command_type in ['list']:
        if parameter not in ['courses', 'students', 'rolls']:
            print('Unknown list parameter.')
    elif command_type in ['clashes']:
        if parameter not in all_courses(records):
            print('Invalid course code!')
    return command, command_type, parameter


    
#===========================================================================
#Print functions:

def print_courses(records):
    """Take a dictionary that maps course codes to course names
       Print courses information
    """
    print('All courses:')
    courses_dict = all_courses(records)
    for course_code in courses_dict:
        print('  {}: {}'.format(course_code, courses_dict[course_code]))
    print()
    
    
def print_students(records):
    """Take a dictionary that maps student numbers (as ints) to student name tuples
       Print students information
    """
    print('All students:')
    students_dict = all_students(records)
    for student_number in students_dict:
        given_name = students_dict[student_number][0]
        family_name = students_dict[student_number][1].upper()
        print('  {}: {} {}'.format(student_number, given_name, family_name))
    print()


def print_course_rolls(records):
    """Take a dictionary that mapping course codes to sets of student numbers
       Print the course_rolls information
    """ 
    print('Course rolls:')
    course_rolls_dict = course_rolls(records)
    for course_code in course_rolls_dict:
        print(course_code)
        student_info_list = list(course_rolls_dict[course_code])
        student_info_list.sort()
        for student_number, given_name, family_name in student_info_list:
            print('  {}: {} {}'.format(student_number, given_name, family_name.upper()))
        print()
    

def print_clashes(records, course_code):
    """Take the course code 
       check the students who take this course and other course at the same time
       Print the clashes information
    """
    print('Clashes with {}:'.format(course_code))
    course_rolls_dict = course_rolls(records)
    other_courses_dict = course_rolls(records)
    other_courses_dict.pop(course_code)
    for another_course in other_courses_dict:
        print('In {} and {}'.format(course_code, another_course))
        intersection = other_courses_dict[another_course] & course_rolls_dict[course_code]
        if intersection == set():
            print('  Nobody.\n')
        else:
            intersection_list = list(intersection)
            for student_number, given_name, family_name in sorted(intersection_list):
                print('  {}: {} {}'.format(student_number, given_name, family_name.upper()))
            print()
    
#============================================================================
#Main function to process file:

def records_from_file():
    """Take a file and process it
       return a list of tuples
    """
    records = []
    filename = input('Filename? ')
    lines = open(filename).read().splitlines()[1:]
    for line in lines:
        course_code, course_name, student_number, given_name, family_name = line.split(',')
        course_tuple = (course_code, course_name)
        student_tuple = (int(student_number), given_name, family_name)
        records.append((course_tuple, student_tuple))
    return records
    
    
#============================================================================ 
#Sub-functions to process file:

def all_courses(records):
    """Takes a list of tuples 
       returns a dictionary that maps course codes to course names.
    """
    courses_dict = {}
    for tuples in sorted(records):
        course_code = tuples[0][0]
        course_name = tuples[0][1]
        courses_dict[course_code] = course_name
    return courses_dict
        
    
def all_students(records):
    """Takes a list of tuples
       return a dictionary that maps student numbers (as ints) to student name tuples
    """
    students_dict = {}
    students_info = []
    for tuples in records:
        student_number = tuples[1][0]
        given_name = tuples[1][1]
        family_name = tuples[1][2]
        students_info.append((student_number, given_name, family_name))
        students_info.sort()
    for student_number, given_name, family_name in students_info:
        students_dict[student_number] = (given_name, family_name)
    return students_dict


def course_rolls(records):
    """Takes a list of records (as generated by records_from_file)
       returns a dictionary mapping course codes to sets of student numbers and names
    """
    course_rolls_dict = {}
    for course, student in sorted(records):
        course_code = course[0]
        student_number = student[0]
        given_name = student[1]
        family_name = student[2]
        if course_code in course_rolls_dict:
            course_rolls_dict[course_code].add((student_number, given_name, family_name))
        elif course_code not in course_rolls_dict:
            course_rolls_dict[course_code] = {(student_number, given_name, family_name)}
    return course_rolls_dict


#=========================================================================    
main()






class Car:
    """A class of car"""
    def __init__(self, model, year, speed=0):
        """initializer to the Car class"""
        self.model = model
        self.year = year
        self.speed = speed
    
    
    def accelerate(self):
        """Increase speed"""
        self.speed += 5
        
        
    def brake(self):
        """Decrease the speed"""
        self.speed = max(0, self.speed - 5)
        
        
    def honk_horn(self):
        """Beep"""
        print("{} goes 'beep beep'".format(self.model))
        
    
    def __str__(self):
        """Print the information of the car"""
        return "{} ({}), moving at {} km/h.".format(self.model, self.year, self.speed)
    
    
    
    
    
    
    
    
    """File for creating Person objects"""
    
    class Person:
        """Defines a Person class, suitable for use in a hospital context.
        Data attributes: name of type str
                         age of type int
                         weight (kg) of type float
                         height (metres) of type float
        Methods: bmi()
        """
    
        def __init__(self, name, age, weight, height):
            """Creates a new Person object with the specified name, age, weight
               and height"""
            self.name = name
            self.age = age
            self.weight = weight
            self.height = height
    
    
        def bmi(self):
            """Returns the body mass index of the person"""
            return self.weight / (self.height * self.height)
            
            
        def status(self):
            """Return the status of somebody"""
            if self.bmi() < 18.5:
                return 'Underweight'
            elif 18.5 <= self.bmi() < 25:
                return 'Normal'
            elif 25 <= self.bmi() < 30:
                return 'Overweight'
            elif self.bmi() >= 30:
                return 'Obese'
                
        def __str__(self):
            """This is the method inside print function"""
            return "{} ({}) has a bmi of {:.2f}. Their status is {}.".format(self.name,
            self.age, self.bmi(), self.status())
            
                
    def read_people(csv_filename):
        """Read a file and process it"""
        a_list = []
        lines = open(csv_filename).read().splitlines()
        for line in lines:
            line = line.split(',')
            name = line[0]
            age = int(line[1])
            weight = float(line[2])
            height = float(line[3])
            a_list.append(Person(name, age, weight, height))
        return a_list
    
    
    
    
    
    
"""Jimmy     27/12/2018"""
from tkinter import *

def double():
    """Say hello to somebody"""
    global hello_label, number_entry
    double_label['text'] = 2 * int(float(number_entry.get()))

def main():
    """main function"""
    global double_label, number_entry
    window = Tk()
    number_entry = Entry(window)
    number_entry.grid(row=0, column=0)
    double_button = Button(window, text='Double it!', command=double)
    double_button.grid(row=1, column=0)
    double_label = Label(window)
    double_label.grid(row=2, column=0)    
    
    window.mainloop()
main()





"""Jimmy     27/12/2018"""
from tkinter import *

def say_hello():
    """Say hello to somebody"""
    global hello_label, name_entry
    hello_label['text'] = 'Hi ' + name_entry.get()

def main():
    """main function"""
    global hello_label, name_entry
    window = Tk()
    prompt_label = Label(window, text='Enter a name below')
    prompt_label.grid(row=0, column=0)
    name_entry = Entry(window)
    name_entry.grid(row=1, column=0)
    hello_button = Button(window, text='Say hello', command=say_hello)
    hello_button.grid(row=2, column=0)
    hello_label = Label(window)
    hello_label.grid(row=3, column=0)    
    window.mainloop()
main()





from tkinter import *
from tkinter.ttk import *


def change(count):
    """Change the count of number"""
    global value, value_label
    value += count
    value_label['text'] = str(value)
def main():
    """Set up the GUI and run it"""

    global value, value_label
    window = Tk()
    value = 0
    value_label = Label(window, text=str(value))
    value_label.grid(row=0, column=0, columnspan=4)
    subtract_five_button = Button(window, text="-5", command=lambda x=-5: change(x))
    subtract_five_button.grid(row=1, column=0)
    subtract_one_button = Button(window, text="-1",  command=lambda x=-1: change(x))
    subtract_one_button.grid(row=1, column=1)
    add_one_button = Button(window, text="+1",  command=lambda x=1: change(x))
    add_one_button.grid(row=1, column=2)
    add_five_button = Button(window, text="+5",  command=lambda x=5: change(x))
    add_five_button.grid(row=1, column=3)
    window.mainloop()

main()













"""A programm including a label and two buttons"""
from tkinter import *
from tkinter.ttk import *


def plus_function():
    """A function to add one"""
    global current_count, label
    current_count += 1
    label['text'] = str(current_count)
    
def subtract_function():
    """Afunction to subtract"""
    global current_count
    current_count -= 1
    label['text'] = str(current_count)

def main():
    """main function"""
    global current_count, label
    current_count = 0    
    
    window = Tk()
    label = Label(window, text=str(current_count))
    label.grid(row=0, column=0)
    plus_button = Button(window, text='+1', command=plus_function)
    plus_button.grid(row=1, column=0)
    subtract_button = Button(window, text='-1', command=subtract_function)
    subtract_button.grid(row=1, column=1)
    window.mainloop()
    
main()









from tkinter import *
from tkinter.ttk import *

def hello_label():
    """Change the label text to hello"""
    message_label['text'] = 'Kia ora!'
    
def adios_label():
    """Change the label text to adios"""
    message_label['text'] = 'noho ora mai'

def main():
    """Construct the GUI and run it"""

    global message_label
    window = Tk()
    message_label = Label(window, text="Click a button!")
    message_label.grid(row=0, column=0)
    hello_button = Button(window, text='Say hello', command=hello_label)
    hello_button.grid(row=1, column=0)
    adios_button = Button(window, text='Say goodbye', command=adios_label)
    adios_button.grid(row=1, column=1)
    window.mainloop()

main()








from tkinter import *
from tkinter.ttk import *

TEMPLATE = "Name: {0}\nHeight: {1:.2f} m\nHorns: {2}"

class Blork(object):
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns   
class BlorkGui(object):
    """Defines the Blork Interface"""
    
    def __init__(self, window, blorks):
        """Setup the label and button on given window"""
        self.blorks = blorks
        self.combobox = Combobox(window, values=list(blorks.keys()))
        self.combobox.grid(row=0, column=0)
        self.button = Button(window, text='View details', 
                             command=lambda x=self:view_details(x))
        self.button.grid(row=0,column=1)
        self.label = Label(window, text="Press 'View details'")
        self.label.grid(row=1, column=0)
        
def view_details(self):
    """View details from database"""
    name = self.combobox.get()
    height = self.blorks[name].height
    if self.blorks[name].has_horns:
        horns = 'Yes'
    else:
        horns = 'No'
    self.label['text'] = TEMPLATE.format(name, height, horns)
        

def main():
    """Set up the GUI and run it."""    
    blorks = {"Jeff": Blork("Jeff", 1.6),
              "Lily": Blork("Lily", 1.111111),
              "Jack": Blork("Jack", 1.89),
              "Chewblorka": Blork("Chewblorka", 3.14, True),
              "Blorkstien": Blork("Blorkstien", 0.856, True)}
    window = Tk()
    blork_gui = BlorkGui(window, blorks)
    window.mainloop()

main()



class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
        
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
        

def dividBy2(decNumber):
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
        
    a_string = ''
    while not remstack.isEmpty():
        a_string += str(remstack.pop())
     
    return a_string


decNumber = 233
print(dividBy2(decNumber))






"""A program to send email         Jimmy              23/1/2019

   Support server: outlook, gmail, qq-email
   
   Note: Some email account can't login in because of security issue.
         If the system gives you a prompt that the server is refusing.
         You need to go to setting and change some security options. 
"""
from tkinter import *
from tkinter.ttk import *
from smtplib import SMTP
from email.mime.text import MIMEText
import smtplib
from time import asctime


#=================================================================================
#Please add some accounts or receivers to the dictionaries below if you need to

global ACCOUNT_DICT, RECEIVER_DICT
ACCOUNT_DICT = {"Jimmy's gmail": 'jimmy75792@gmail.com', 
                "Jimmy's outlook": 'cgo54@uclive.ac.nz'}

RECEIVER_DICT = { "Jimmy's qq email": '737648711@qq.com',
                  "Jimmy's gmail": 'jimmy75792@gmail.com',
                 "Jimmy's outlook": 'cgo54@uclive.ac.nz', 
                  'Paul Mckeown': 'paul.mckeown@canterbury.ac.nz',
                  'Lotte': '360621695@qq.com'}



#==================================================================================

class EmailGui:
    """To send email quicklier"""
    global ACCOUNT_DICT, RECEIVER_DICT
    def __init__(self, window):
        """Initializer"""
        #Labels:
        self.prompt_label = Label(window, text='Welcome to use swift email system!')
        self.prompt_label.grid(row=0, column=0, columnspan=3)      
        
        self.account_label = Label(window, text='Account: ')
        self.account_label.grid(row=1, column=0)        
        
        self.password_label = Label(window, text='Password: ')
        self.password_label.grid(row=2, column=0)        
        
        self.address_label = Label(window, text='To: ')
        self.address_label.grid(row=4, column=0, sticky=E)
        
        self.subject_label = Label(window, text='Subject: ')
        self.subject_label.grid(row=5, column=0, sticky=E)
        
        self.content_label = Label(window, text='Content: ')
        self.content_label.grid(row=6, column=0)
        
        #Buttons:
        self.account_enter = Button(window, text='Enable', command=self.connection)
        self.account_enter.grid(row=3, column=1, columnspan=3, sticky=(E, W))
           
        self.content_submit = Button(window, text='Send', command=self.send)
        self.content_submit.grid(row=8, column=2)
        
        #Combobox:
        self.account_combo = Combobox(window, values=list(ACCOUNT_DICT.keys()))
        self.account_combo.grid(row=1, column=1, sticky=(E, W), columnspan=2)
        
        self.address_combo = Combobox(window, values=list(RECEIVER_DICT.keys()))
        self.address_combo.grid(row=4, column=1, sticky=(E, W))
        
        #Entry:

        self.password_entry = Entry(window, show='*')
        self.password_entry.grid(row=2, column=1, sticky=(E, W), columnspan=2)
                
        self.subject_entry = Entry(window)
        self.subject_entry.grid(row=5, column=1, sticky=(E, W))
        self.subject_entry.insert('1', '')
        
        #Text:
        self.content = Text(window, width=50, height=25)
        self.content.grid(row=7, column=1)
        #self.content.insert('1.0', 'Dear ' + '\n' * 10)
        #self.content.insert('10.0', 'Thank you\nJimmy')
        

    def connection(self):
        """A connection to email server"""
        if self.account_combo.get() == '' or self.password_entry.get() == '':
            self.prompt_label['text'] = 'Incorrect account information' 
            
        else:
            try:
                self.account = ACCOUNT_DICT[self.account_combo.get()]
            except KeyError:
                self.account = self.account_combo.get()
            try:
                host = self.account.split('@')[1] 
            except IndexError:
                self.prompt_label['text'] = 'Invilid address'
            else:
                if host[-5:-3] in ['ac']:
                    host = 'office365.com'
                password = self.password_entry.get()            
                time = asctime().split()[3]
                self.server = SMTP('smtp.' + host, 587)
                self.server.ehlo()
                self.server.starttls()
                self.server.ehlo()
                try:
                    self.server.login(self.account, password, initial_response_ok=True)
                except smtplib.SMTPAuthenticationError:
                    self.prompt_label['text'] = 'Invalid password    ' + '  Time: ' + time
                except smtplib.SMTPServerDisconnected:
                    self.prompt_label['text'] = 'Email server is refusing connection    ' + '  Time: ' + time                
                except:
                    self.prompt_label['text'] = 'Disconnected    ' + '  Time: ' + time
                else:
                    self.prompt_label['text'] = self.account +'       Connected    ' + 'Time: ' + time
        
        
    def send(self):
        """Send message"""
        time = asctime().split()[3]
        try:
            address = RECEIVER_DICT[self.address_combo.get()]
        except KeyError:
            address = self.address_combo.get()  
        try:
            mail = MIMEText(self.content.get(0.0, 10.0))
            mail['Subject'] = self.subject_entry.get()
            print(mail.as_string())
            self.server.sendmail(self.account, address, mail.as_string())
        except:
            self.prompt_label['text'] = 'Fail to send     ' + 'Time: ' + time
        else:
            print(self.content.get(0.0, 25.0))
            self.prompt_label['text'] = 'Send to:  ' + address + '    Successfullly    ' + 'Time: ' + time

#================================================================================

def main():
    """Core function"""
    window = Tk()
    main_object = EmailGui(window)
    window.mainloop()
    
main()





class Fraction(object):
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numberator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError
            
    def __add__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        return Fraction(numerator1 + numerator2, self.denominator * other.denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __repr__(self):
        return 'Fraction({}, {})'.format(self.numerator, self.denominator)    
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)     

    
class ReducedFraction(Fraction):
    """A subclass of Fraction"""
    def __init__(self, numerator, denominator=1):
        Fraction.__init__(self, numerator, denominator)
        self.__reduce__()

    def __reduce__(self):
        gcd = findgcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
        
    def __mul__(self, other):
        unreduced_fraction = Fraction.__mul__(self, other)
        return ReducedFraction(unreduced_fraction.numerator, unreduced_fraction.denominator)
        
        
    def __add__(self, other):
        unreduced_fraction = Fraction.__add__(self, other)
        return ReducedFraction(unreduced_fraction.numerator, unreduced_fraction.denominator)
    

    def __repr__(self):
        return 'ReducedFraction({}, {})'.format(self.numerator, self.denominator)
        
        
def findgcd(x, y):
    '''Returns the Greatest Common Divisor of x and y. Assumes x and y are positive integers.'''
    smaller = min(x, y)
    for i in range(int(smaller), 1, -1):
        if x % i == 0 and y % i == 0:
            return i
    return 1    


class MixedNumber(ReducedFraction, Fraction):
    def __init__(self, whole_part, fraction_part):
        self.whole_part = whole_part
        ReducedFraction.__init__(self, fraction_part.numerator, fraction_part.denominator)
        
    def __add__(self, other):
        reduced_fraction = ReducedFraction.__add__(self, other)
        plus = 0
        if reduced_fraction.numerator >= reduced_fraction.denominator:
            while reduced_fraction.numerator >= reduced_fraction.denominator:
                reduced_fraction.numerator -= reduced_fraction.denominator
                plus += 1
        return MixedNumber(self.whole_part + other.whole_part + plus, reduced_fraction)
        
    def __repr__(self):
        return 'MixedNumber({}, ReducedFraction({}, {}))'.format(self.whole_part, self.numerator, self.denominator)
        
    def __str__(self):
        return '{} and {}/{}'.format(self.whole_part, self.numerator, self.denominator)
    
    
    
x = MixedNumber(3, Fraction(1, 3))
y = MixedNumber(-1, Fraction(2, 5))
z = x + y
print(z)
print(repr(z))




import string
from abstract_data_type import Stack
import doctest

def infixToPostfix(infixexpr):
    """>>> infixexpr1 = 'A + ( ( B + C ) * ( D + E ) )'
       >>> print(infixToPostfix(infixexpr1))
       ABC+DE+*+
       >>> infixexpr1 = '( A + B ) * ( C + D ) * ( E + F )'
       >>> print(infixToPostfix(infixexpr1))
       AB+CD+*EF+*
    """

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    load_Stack = Stack()
    result = []
    tokenlist = infixexpr.split()
    for token in tokenlist:
        if token.isupper():      #Letter
            result.append(token)
        elif token == '(':
            load_Stack.push(token)
        elif token == ')':
            topToken = load_Stack.pop()
            while topToken != '(':
                result.append(topToken)
                topToken = load_Stack.pop()
        else:      #Operator
            while not load_Stack.isEmpty() and prec[load_Stack.peek()] >= prec[token]:
                result.append(load_Stack.pop())
            load_Stack.push(token)
            
    while not load_Stack.isEmpty():
        result.append(load_Stack.pop())
    return ''.join(result) 


print()
    

    

            
def infix_to_postfix(infix_expr):
    """Convert infix to postfix
       >>> infix_expr = 'A + ( ( B + C ) * ( D + E ) )'
       >>> print(infix_to_postfix(infix_expr))
       ABC+DE+*+
       >>> infix_expr = '( A + B ) * ( C + D ) * ( E + F )'
       >>> print(infix_to_postfix(infix_expr))
       AB+CD+*EF+*
    """
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    result = []
    operator_stack = Stack()
    operator_stack.push('(')
    for token in infix_expr.split() + [')']:
        if token.isupper():
            result.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token in prec:
            if prec[token] > prec[operator_stack.peek()]:
                operator_stack.push(token)
            elif prec[token] == prec[operator_stack.peek()]:
                result.append(token)
            elif prec[token] < prec[operator_stack.peek()]:
                result.append(operator_stack.pop())
        elif token == ')':
            operator = operator_stack.pop()
            while operator != '(':
                result.append(operator)
                operator = operator_stack.pop()
    
    return ''.join(result)
            
            
    
    
    
       
def postfix_evaluation(postfix_expr):
    """Evaluate the the postfix expression, the number must be single digit"""
    token_list = postfix_expr.split()
    load_stack = Stack()
    for token in token_list:
        if token.isdigit():
            load_stack.push(int(token))
        elif token in '+-*/':
            operand2 = load_stack.pop()
            operand1 = load_stack.pop()
            calculation = infix_evaluation(token, operand1, operand2)
            load_stack.push(calculation)
            
    return load_stack.pop()
            

def infix_evaluation(operator, operand1, operand2):
    """Evaluate the the infix expression, the number must be single digit"""
    if operator == '+':
        return operand1 + operand1
    if operator == '-':
        return operand1 - operand1
    if operator == '*':
        return operand1 * operand1
    if operator == '/':
        return operand1 / operand1    

print(doctest.testmod())


def BMi():
    bmi_history = {}
    stop = False
    while not stop:
        name = input('Your name: ')
        weight = float(input('What is your weight?  (kg) '))
        height = float(input('What is your height?  (cm) '))
        body_mass_index = weight / (height/100)**2
        print('Your body mass index is:')
        print('{:.2f}'.format(body_mass_index))
        print()
        if body_mass_index < 18.5:
            print('You are too skiny')
        elif 18.5 <= body_mass_index <= 23:
            print('Good!')
        else:
            print('You are too heavy!')
        bmi_history[name] = body_mass_index
    return bmi_history
print(BMi())