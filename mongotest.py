import pymongo
client = pymongo.MongoClient("mongodb+srv://iNeuron:mongodb123@cluster0.9pjbtql.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "id": 123456,
    "name": "Mrunal",
    "emailid": "mruanl2210@yahoo.in",
    "surname": "Sawant"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)