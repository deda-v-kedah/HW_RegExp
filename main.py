from pprint import pprint
import re
import csv


def dict_join(dict_1, dict_2):
    result_dict = {}
    iteration_list = ['lastname','firstname','surname','organization','position','phone','email']

    for key in iteration_list:
        if dict_1[key] != '':
            result_dict[key] = dict_1[key]
        else:
            result_dict[key] = dict_2[key]

    return result_dict

def read_file():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def fix_text( text ):
    result_list = []
    return_list = []
    pattern = re.compile(r'^(\w*)[ ,]*(\w*)[ ,]*(\w*)[ ,]')
    phone_pattern = re.compile(r'(8|\+7)\s?\(?(\d{3})\)?[ -]?(\d{3})[ -]?(\d{2})[ -]?(\d{2})(\s?\(?(доб.)\s(\d+)\)?)?')

    for line in text:
        
        new_phone =  phone_pattern.sub(r'+7(\2)\3-\4-\5 \7\8', line[5])

        join_line = ','.join(line)
        result = pattern.search(join_line)

        mydict = {'lastname': result.group(1),'firstname': result.group(2), 'surname': result.group(3), 'organization': line[3],'position': line[4], 'phone': new_phone.rstrip(), 'email': line[6]}

        for old_line in result_list:
            if old_line['lastname'] == mydict['lastname'] and old_line['firstname'] == mydict['firstname']:
                result_list.remove(old_line)
                result_list.append(dict_join(old_line, mydict))
                break
        else:
            result_list.append(mydict)


    for line in result_list:
        return_list.append(list(line.values()))
 
    
    return return_list

def write_file(write_text):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(write_text)



    

if __name__ == '__main__':
    text = read_file()
    write_text = fix_text(text)
    write_file(write_text)





