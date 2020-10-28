from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.insert_one({'name':'bobby', 'age':21})
db.users.insert_one({'name':'kay', 'age':27})
db.users.insert_one({'name':'john', 'age':30})

## MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':21}))

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user)

user = db.users.find_one({'name': 'bobby'})
print(user)

# 그 중 특정 키 값을 빼고 보기
user = db.users.find_one({'name': 'bobby'}, {'_id':False})
print(user)

## 수정하기
db.users.update_one({'name': 'bobby'}, {'$set': {'age':19}})
user = db.users.find_one({'name': 'bobby'})
print(user)

## 삭제하기
db.users.delete_one({'name':'bobby'})
user = db.users.find_one({'name':'bobby'})
print(user)