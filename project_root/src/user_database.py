class UserDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, user_data):
        if user_id in self.users:
            raise ValueError("Usuário já existe.")
        self.users[user_id] = user_data
        return self.users[user_id]

    def read_user(self, user_id):
        return self.users.get(user_id, None)

    def update_user(self, user_id, new_data):
        if user_id not in self.users:
            raise ValueError("Usuário não existe.")
        self.users[user_id].update(new_data)
        return self.users[user_id]

    def delete_user(self, user_id):
        if user_id not in self.users:
            raise ValueError("Usuário não existe.")
        del self.users[user_id]
        return True
