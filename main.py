import base64
import datetime

import mongoengine
import pymongo

from nosql.contact import Contact
from nosql.title import State, Title
from nosql.vehicle import Vehicle, Manufacture, Model

conn_str = "mongodb://spowell:n2329w@localhost:27017"
cl = pymongo.MongoClient(conn_str)
db = cl['vehicle_db']

contact = Contact(first_name='scot', last_name='powell')
contact.insert_one(db)
buyer = contact.find_one(db, {'first_name':'SCOT', 'last_name' : 'POWELL'})




with open("images/c10.JPG", "rb") as imageFile:
    c10_bytes = base64.b64encode(imageFile.read())

with open("images/title.JPG", "rb") as imageFile:
    title_bytes = base64.b64encode(imageFile.read())

title = Title(title_number='19600705023', state=State.TX, odometer=79, image=title_bytes)

v = Vehicle(stock_number=1,
            vin='97507329',
            manufacture=Manufacture.CHEVROLET,
            model=Model.CORVETTE,
            year=1969,
            purchase_date=datetime.datetime(year=2021, month=6, day=27),
            purchase_price=8250,
            title=title,
            image=c10_bytes
            )
v.insert_one(db)
#
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
#
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print(db.list_collection_names())

# print(cl.list_database_names())

# client = mongoengine.connect(db='admin',alias='default', username='spowell', password='n2329w', host='localhost', port=27017)
#
#
# # mongoengine.register_connection(alias='default', name='vehicles', host='localhost',username='spowell',password='n2329w',db='vehicle_db')
# #
# #
# v = Vehicle()
# v.stock_number = 2
# v.year = '1969'
# v.vin = '97507329'
# v.manufacture = 'CHEVROLET'
# v.model = 'CORVETTE'
# v.purchase_date = datetime.date(2021,6,27)
# v.purchase_price = 8250
#
# v.save()


# class Vehicle(mongoengine.Document):
#     stock_number = mongoengine.IntField(required=False, null=False)
#     vin = mongoengine.StringField(required=True, null=False)
#     manufacture = mongoengine.StringField(required=True, null=False)
#     model = mongoengine.StringField(required=True, null=False)
#     year = mongoengine.IntField(required=True, null=False)
#     purchase_date = mongoengine.DateField(required=True, null=False)
#     purchase_price = mongoengine.DecimalField(required=True, null=False)
#     sale_date = mongoengine.DateField(required=False, null=True)
#     sale_price = mongoengine.StringField(required=False, null=True)
