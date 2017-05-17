# bd-assignment updated code
p=input('Enter your first name : ')
q=input('Enter your last name : ')
r=input('Enter the month you were born (1-12)? : ')
s=input('Enter the date you were born (1-31)? : ')
t=input('How old will you be this year? : ')
yob=2017-(int(t))
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
u=months[(int(r))-1]
days=['st','nd','rd','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','th','st','nd','rd','th','th','th','th','th','th','th','st']
v=days[(int(s))-1]

import datetime
w=datetime.date(int(yob),int(d),int(c))
#print('you were born on',h.strftime('%a'))
print('Your names are' ,p, ' ' ,q, 'born on' ,s+r, ' ' ,u, ' ' ,yob, 'the day of the week was a' ,h.strftime('%a'))
