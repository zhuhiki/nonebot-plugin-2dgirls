
import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import  MessageSegment
#路径和请求头调成自己的就行了
path = r'C:\Users\ASUS\Desktop\bot_test\robmaster\src\plugins\animate_girl'+'\\'
command=on_command('来点美少女')
@command.handle()
async def send():
    flag=True
    url='https://www.dmoe.cc/random.php'
    headers={
        'useragent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
    }
    response=requests.get(url=url,headers=headers)
    if response.status_code == 200:
        # 将响应内容保存为图片文件
        with open(path+'random_image.jpg', 'wb') as f:
            f.write(response.content)
        await command.send(message='正在为你寻找美少女')
    else:
        await command.send(message='api寄了没找到捏')
        flag=False
    if flag is True:
        image_path =r'C:\Users\ASUS\Desktop\bot_test\robmaster\src\plugins\animate_girl\random_image.jpg'
        with open(image_path, 'rb') as f:
            image_data = f.read()

    await command.send(MessageSegment.image(file=image_data))

    await command.finish()


