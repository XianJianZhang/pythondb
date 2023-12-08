class InMemoryDB:
    def __init__(self):
        self.storage = {}
        self.temp = {}
        self.inprogress = False

    def get(self, key):
        if (key in self.storage):
            return self.storage[key]
        else:
            return None
        
    def put(self, key, val):
        if (self.inprogress):
            self.temp[key] = val
        else: 
            print("Transaction is not started! Put request failed!")

    def begin_transaction(self):
        self.inprogress = True

    def commit(self):
        if (self.inprogress):
            for key, value in self.temp.items():
                self.storage[key] = value
            self.inprogress = False
        else:
            print("No ongoing transactions to commit!")

    def rollback(self):
        if (self.inprogress):
           self.temp = {}
        else:
            print("No ongoing transactions! Nothing to rollback!")

db = InMemoryDB()
print(db.get("A"))
db.put("A", 5)
db.begin_transaction()
db.put("A", 5)
print(db.get("A"))
db.put("A", 6)
db.commit()
print(db.get("A"))
db.commit()
db.rollback()
print(db.get("B"))
db.begin_transaction()
db.put("B", 10)
db.rollback()
print(db.get("B"))