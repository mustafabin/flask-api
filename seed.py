from models import *
import datetime
db.drop_tables([Person,Car])
db.create_tables([Person,Car])


Person(name='Mustafa', age=18).save()
Person(name='Ben', age=24).save()
Car(model='rav4', year= datetime.date(2010, 6, 5),miles=10000, ownerid="1").save()
Car(model='rav4 but black', year= datetime.date(2010, 6, 5),miles=10001, ownerid="1").save()
Car(model='rav4 but red', year= datetime.date(2010, 6, 5),miles=10002, ownerid="1").save()
Car(model='hotwheels', miles=200000, year= datetime.date(2040, 11,11), ownerid="2").save()