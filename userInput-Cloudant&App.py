from cloudant.client import Cloudant
from cloudant.result import Result

# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-2g0897b2w64ufus4y2goqiiqy5vsu4alw9gjffnfd9pj", "24293d308931fd40b27340bb195374f3",
                  url="https://apikey-v2-2g0897b2w64ufus4y2goqiiqy5vsu4alw9gjffnfd9pj:24293d308931fd40b27340bb195374f3@68da9970-a9f0-4f54-bf81-ca6367522e95-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()
database_name = "user_input" #Cloudant db name which is udes to store the user input from MIT App using Nodered

my_database = client.create_database(database_name)
result_collection = Result(my_database.all_docs, include_docs=True)
# Iterate over the result collection
result_collection = list(result_collection)
result = result_collection[0]
print("The user input received is: ")
print(result['doc']['userInput'])



