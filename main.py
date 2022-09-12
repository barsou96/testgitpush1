import pymongo


client = pymongo.MongoClient("mongodb+srv://<raahil_123>:<NarMay>@cluster1.n4ulbe7.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d1 = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db2 = client['mongotest1']
coll = db2['test']
coll.insert_one(d1 )