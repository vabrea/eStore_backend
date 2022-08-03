import pymongo
import certifi

con_str = "mongodb+srv://eStoreVG:FullStack27@cluster0.ihvtj.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Jerseys")