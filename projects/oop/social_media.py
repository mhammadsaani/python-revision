class User:
    user_credentials = {}
    user_posts = {}
    def __init__(self, username, password):
        if username not in User.user_credentials:
            self.username = username
            self.password = password
            User.user_credentials[self.username] = self.password
        print(User.user_credentials)
    
    def login(self, username, password):
        temp = User.user_credentials.get(username)
        if temp == password:
            print("login successfully")
        else:
            print('username or password is wrong')
    
    def post(self, post):
        pass
            

hammad = User("hammad", 1234)
hammad.login("hammad", 321)