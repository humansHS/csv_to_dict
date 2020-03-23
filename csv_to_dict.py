import os
import csv

# Converts strings to the correct data types
# Works for: int, float, first level list, string
# Does not work for: Nested lists, tuples
# Converts | to , and \n to new line
def string_to_calc(string):
    try:
        i = int(string)
    except ValueError:
        try:
            i = float(string)
        except ValueError:
            if string[0] == '[':
                if string[len(string)-1] == ']':
                    string = string[1:len(string)-1]
                else:
                    string = string[1:]
                i = []
                comma = 0
                while comma != -1:
                    comma = string.find(',')
                    if comma != -1:
                        i.append(string_to_calc(string[:comma]))
                        string = string[1+comma:]
                    else:
                        i.append(string_to_calc(string))
            else:
                string = string.replace('|',',')
                string = string.replace('\\n','\n')
                i = string
                #print(i)
    return i

# Reads a csv and stores it into a DICT
def csv_to_dict(inputcsv, *args):
    
    #print(os.path.join("csv_files", inputcsv))
    with open(os.path.join("csv_files", inputcsv)) as csv_input:

        csv_reader = csv.DictReader(csv_input, delimiter=',')
        #line_count = 0
        output_dict = {}

        for row in csv_reader:
            temp_dict = {}
            headers = csv_reader.fieldnames
            for header in headers:
                if header != 'name':
                    temp_dict[header] = string_to_calc(row[header])
            output_dict[row['name']] = temp_dict
  
    return output_dict
