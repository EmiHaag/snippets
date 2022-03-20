from datetime import datetime

#returns a boolean value between two date values string type 
#import this snippet in your code, then call this function

#ex:
#params date 1 ex: passedSevenDays("23/10/2022", "12/02/2021") => False

def passedSevenDays(dateA, dateB):
    dateA = datetime.strptime(v, "%d/%m/%Y")
    dateB = datetime.strptime(v, "%d/%m/%Y")
    return dateA < dateB
