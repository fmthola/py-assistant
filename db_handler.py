from tinydb import TinyDB, Query
db = TinyDB('db.json')

Server = Query() # type: tinydb.queries.Query

def initialize():
    db.insert({'server': 'pi', 'ip': '192.168.0.78'})
    db.insert({'server': 'dns', 'ip': '192.168.0.250'})
    db.insert({'server': 'develop1', 'ip': '192.168.0.98', 'script': '/home/flamehaze/sync.sh'})
    db.insert({'server': 'develop-main',  'ip': '192.168.0.107', 'script': '/home/flamehaze/script.sh' })

def search_user():
    results = db.search(Server.server == 'develop1') # returns a list
    for res in results:
        print(res) # type: tinydb.database.Document
        # print(res.city) # Not allowed!
        print(res['script'])

def update_server():
    db.update({'ip': '192.168.0.1'}, Server.server == 'dns')
    for item in db:
        print(item)

def delete_user():
    db.remove(Server.server == 'dns')
    # db.purge() # remove all
#initialize()
#insert_user()
#search_user()
#update_user()
#delete_user()

print(db.all())
for item in db:
    print(item)
print(len(db)) # number of items
