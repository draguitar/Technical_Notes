import json
import time
import requests
from PIL import Image
import numpy as np

im = Image.open("baby.jpg").convert('L')


np_array = np.array(im)

print(np_array)
print(np_array.shape)
img = Image.fromarray(np_array, 'L')
img.save('bab.jpg')
img.show()

img_data = np_array.tolist()


params={
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5,
    "tags":img_data
}

url='http://127.0.0.1:8888/sys/sinoma/v1/optimization/predict/fcao'

time1=time.time()
html = requests.post(url, json.dumps(params))
print('post 成功!')
print('回傳 post结果如下：')
print(html.text)

time2=time.time()
print('耗時：' + str(time2 - time1) + 's')