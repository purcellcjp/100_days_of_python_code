class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # not necessary to populate with value to initialize
        self.following = 0
        
        
    def follow(self, user):
        user.followers +=1
        self.following +=1
        

user_1 = User('001', 'Jack Smith')
# user_1.id = '001'
# user_1.username = 'George'
user_2 = User('002','Jack Ryan')


# print(user_1.id, user_1.username, user_1.followers, sep='|')

user_1.follow(user_2)

print('-'*20)
print(user_1.username, user_1.followers, user_1.following, sep='|')
print(user_2.username, user_2.followers, user_2.following, sep='|')
print('-'*20)
