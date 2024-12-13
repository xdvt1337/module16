from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def Get_Main_Page() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def Get_Admin_Page() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def Get_User_Number(user_id: int ) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def Get_User_Info(username: str, age: int) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}