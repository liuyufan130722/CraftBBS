from database import user, verification_code
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

# with requests.post("http://127.0.0.1:5665/register", json={
#     "username": "PYmili",
#     "password": "123",
#     "email": "2097632843@qq.com",
#     "code": "fEHWyGfO",
#     "avatar_url": "https://profile-avatar.csdnimg.cn/414f7b0a2036498bab4e37580fca6377_qq_53280175.jpg"
#     }) as post:
#     print(post.json())

# with verification_code.VerificationCodeDataBase() as vcd:
#     print(vcd.create_data(
#         "mc2005wj@163.com",
#         "PYmili",
#         "huifhaioe"
#     ))
    # print(vcd.delete_by_username("PYmili"))

# with requests.post("http://127.0.0.1:5665/send_code", json={
#     "email": "2097632843@qq.com",
#     "username": "PYmili"
# }) as post:
#     if post.status_code == 200:
#         print(post.json())
#     else:
#         print(post.text)