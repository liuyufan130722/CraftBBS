from database import user
import requests

# with user.UserDatabase() as useroper:
#     result = useroper.create_user(
#         "PYmili",
#         "mc2005wj@163.com",
#         True,
#         password="124",
#         key="jfakprfweaf",
#         avatar=b''
#     )
#     print(result)
#     print(useroper.get_user("PYmili"))
#     print(useroper.delete_user("PYmili"))
#     print(useroper.get_user("PYmili"))

with requests.post("http://127.0.0.1:5665/register", json={
    "username": "PYmili",
    "password": "123",
    "email": "mc2005wj@163.com",
    "avatar_url": "https://profile-avatar.csdnimg.cn/414f7b0a2036498bab4e37580fca6377_qq_53280175.jpg"
    }) as post:
    print(post.json())