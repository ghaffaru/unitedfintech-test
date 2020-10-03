import pymongo
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
# Create the client
client = pymongo.MongoClient(env('DB_HOST', default='localhost'), 27017)

# Connect to our database
db = client['employeedb']