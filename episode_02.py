#episode-02 (Finding the leader)
import re
def check_vowels(name):
    v = re.compile('[aeiouAEIOU]')
    return len(v.findall(name))  #returns the length of the list which contains the elements that are common in the strings VOWELS and NAME


# Said that the name contains atleast one consecutive double character. so it is sufficient to look for the first occurence of a consecutive double character
def check_consecutive_double_letter(name):      
    return bool(re.search(r'((\w)\2)', 'narendra'))


    

# To find the leader
def find_leader(name, eyes, hair, glasses):

    check_list  = ""    #Checklist to mark 
    if eyes == 'green':
        check_list += 't'

        if hair == 'red':
            if check_consecutive_double_letter(name) is True:
                check_list += 't'

            else :
                return 'False'
        if glasses == 'yes':
            if check_vowels(name) == 2:
                check_list += 't'
            else:
                return 'False'

        elif check_vowels(name) == 3: 
            check_list +='t'

        else :
            return 'False'
    else:
        return 'False'
   
    if check_list.find('f') == -1:
        return 'True'
    else:
        return 'False'




#Test Bench
persons = int(input ("no.of persons:"))
names = []*persons
eyecolor = []*persons
haircolor = []*persons
spectacles = []*persons    #Type either 'yes' or 'no'
print("*******************CAUTION: Please type lower case characters***********************")
for i in range(persons):
    print(i)
    names.append(input("Enter name:"))
    eyecolor.append(input("Enter the color of eyes:"))
    haircolor.append(input("Enter the color of hair:"))
    spectacles.append(input("If he/she has glasses:(Type 'yes' or'no' withour any quotes)" ))



set_of_persons = list(zip(names, eyecolor, haircolor, spectacles))

var = 'False'
for i in range (len(set_of_persons)):

    temp = set_of_persons[i]
    if find_leader(temp[0], temp[1], temp[2], temp[3]) == 'True':
        print("The leader is " + temp[0])
        var = 'True'
        break

if var == 'False':
    print("No leader found")

