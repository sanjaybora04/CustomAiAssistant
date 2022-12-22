from datetime import datetime

def reply():
    weekdays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    months = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    now = datetime.now()
    return ("Time is "+str(now.hour)+" "+str(now.minute)+" "+("PM" if now.hour>12 else "AM")+ " and today is "+weekdays[now.weekday()]+" "+str(now.day)+" "+months[now.month]+" "+str(now.year))

print(reply())