import re
import datetime

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=6)
Previous_Date_Formatted = Previous_Date.strftime ('%d/%m/%y') # format the date to dd/mm/yy
pre_date = str(Previous_Date_Formatted)
print(pre_date)

f = open("WhatsApp Chat with s3 - whatsapp summary bot.txt", "r")

#content = f.read()

for x in f:
    # s = re.search("code", x)
    #print(s)
    # if s != None:
    #     print(s.string)
    if re.search("code",x):
        if re.search("^[0-9]",x):
    	    print(x[20:])

f.close()