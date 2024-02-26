import requests
from PIL import Image
import io


print("Endpoint Hit:  http://127.0.0.1:5000/get/dog/image")
img_route = 'http://127.0.0.1:5000/get/dog/image'
img_content = requests.get(img_route).content
img_content = io.BytesIO(img_content)
img = Image.open(img_content)
img.show()

print("Endpoint Hit:  http://127.0.0.1:5000/get/dog/fact")
fact_route = 'http://127.0.0.1:5000/get/dog/fact'
fact = requests.get(fact_route).content
fact = fact.decode('utf-8')
print(fact)
