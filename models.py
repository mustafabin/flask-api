from peewee import *

db = PostgresqlDatabase('car_people', user='postgres',
                        password='123', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    age = IntegerField()
    
class Car(BaseModel):
    model = CharField()
    miles = IntegerField()
    year = DateField()
    ownerid = CharField()
