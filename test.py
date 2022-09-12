import pymongo

client = pymongo.MongoClient("mongodb+srv://rony1:mongodb@cluster0.gqsxyzs.mongodb.net/?retryWrites=true&w=majority")



d = {
    "name" : "sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )