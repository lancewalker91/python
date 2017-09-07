people={'alice':{'phone':'2341','addr':'dajjdaks'},'beth':{'phone':'9102','addr':'qjwqwq'},
    'cecil':{'phone':'3526','addr':'ywquwqu'}}
labels={'phone':'phone number','addr':'address'}
name=raw_input('Name:')
request=raw_input('Phone number (p) or address (a)?')
if request =='p':key ='phone'
if request =='a':key='addr'
if name in people:print "%s's%s is %s."%\
   (name,labels[key],people[name][key])
