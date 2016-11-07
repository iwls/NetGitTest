
#This Functions transforms a year between a minimum year and a maximum year/ age to an age
#years that are too long ago or to recent to fit within a given age range have as output 0

#lijst = [2000 , 1916, 2002, 20030]
def year_to_age(year, min_age, max_age):
    age=[]
    for element in year:
        if element >= (2016 - max_age) and element <= (2016 - min_age) :
            age.append(2016 - element)
        elif element <= max_age and element >= min_age:
            age.append(element)
        else:
            age.append(0)
    return age

#print( year_to_age(lijst , 10, 100))


##this function is similar to year_to_age function with the extra that you can choose the basis year to which you want the age.
def year_to_age_at_year(year, min_age, max_age, basisyear):
    age=[]
    for element in year:
        if element >= (basisyear - max_age) and element <= (basisyear - min_age) :
            age.append(basisyear - element)
        elif element <= max_age and element >= min_age:
            age.append(element)
        else:
            age.append(0)
    return age
