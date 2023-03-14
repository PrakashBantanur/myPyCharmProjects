# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = '001'
# user_1.username = 'Pavan'
#
# print(user_1.username)
#
#
# user_2 = User()
# user_2.id = '002'
# user_2.username = 'Navin'
# print(user_2.id)

# Using constructor
class NewUser:

    def __init__(self, username, user_id):
        self.user_id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_3 = NewUser('Pradeep', '004')
user_4 = NewUser('Prakash', '005')

user_3.follow(user_4)

print(user_4.name)
print(user_3.user_id)
print(user_4.followers)


print(user_3.followers)
print(user_3.following)
print(user_4.followers)
print(user_4.following)

