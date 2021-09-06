import base64
import datetime
import io

import pymongo
from PIL import Image
import matplotlib.pyplot as plt

from nosql.contact import Contact
from nosql.title import State, Title
from nosql.vehicle import Vehicle, Manufacture, Model

conn_str = "mongodb://spowell:n2329w@localhost:27017"
cl = pymongo.MongoClient(conn_str)
db = cl['vehicle_db']

contact = Contact(first_name='scot', last_name='powell')
contact.insert_one(db)
seller = contact.find_one(db, {'first_name': 'SCOT', 'last_name': 'POWELL'})

# im = Image.open('images/c10.JPG')
# im.show()

with open("images/c10.JPG", "rb") as imageFile:
    c10_bytes = base64.b64encode(imageFile.read())

with open("images/title.JPG", "rb") as imageFile:
    title_bytes = base64.b64encode(imageFile.read())

atitle = Title(title_number='19600705023', state=State.TX, odometer=79, title_image=title_bytes)

img = Image.open('images/c10.JPG')
imgByteArr = io.BytesIO()
img.save(imgByteArr, 'JPEG')
imgByteArr = imgByteArr.getvalue()

v = Vehicle(stock_number=1,
            vin='97507329',
            manufacture=Manufacture.CHEVROLET,
            model=Model.CORVETTE,
            year=1969,
            purchase_date=datetime.datetime(year=2021, month=6, day=27),
            purchase_price=8250,
            title=atitle,
            seller=seller['_id'],
            vehicle_image=imgByteArr
            )
v.insert_one(db)

# pil_img = Image.open(io.BytesIO(v.vehicle['vehicle_image']))
# plt.imshow(pil_img)
# plt.show()
