people = {
    'Alice':{'phone':'2341','addr':'foo drive 23'},
    'Beth':{'phone':'9102','addr':'street 8899'},
    'Ceil':{'phone':'8239','addr':'hello wqwqw94398'}
         }
labels = {'phone':'phone number','addr':'address'}
name = input('Name:')
request = input('Phone number (p) or adress (a)?')
if request == 'p':key ='phone'
if request == 'a':key = 'addr'
if name in people:
    print("%s's %s is %s."%(name,labels[key],people[name][key]))
else:
    person = people.get(name, {})
    result = person.get('key', 'not available')
    print("%s's %s is %s"% (name,request,result))

