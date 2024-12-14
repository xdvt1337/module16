from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {username} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {username} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users.pop(user_id)
    return f"User with {user_id} was deleted!"