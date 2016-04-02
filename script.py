import pyejdb

db = pyejdb.EJDB("city", pyejdb.DEFAULT_OPEN_MODE)


db.save("people", {"name":"Jan", "lastname": "Kowalski"})
db.save("people", {"name":"Michał", "lastname": "Nowak"})
db.save("people", {"name":"Paweł", "lastname": "Koń"})
db.save("people", {"name":"Piotrek", "lastname": "Tusk"})
