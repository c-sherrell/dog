import requests
import io
from flask import Flask

app = Flask(__name__)


@app.route('/get/dog/image')
def get_img():
    """
    This function takes no arguments and returns a random image of a dog as a BytesIO object.
    :return: BytesIO
    """
    img_api_url = "https://dog.ceo/api/breeds/image/random"
    img_api_response = requests.get(img_api_url)
    img_url = img_api_response.json()['message']
    img_data = io.BytesIO(requests.get(img_url).content)
    return img_data


@app.route('/get/dog/fact')
def get_fact():
    """
    This function takes no arguments and returns a string containing a random dog fact.
    :return: string
    """
    fact_api_url = "http://dog-api.kinduff.com/api/facts"
    fact_response = requests.get(fact_api_url)
    fact_txt = fact_response.json()['facts'][0]
    return fact_txt


if __name__ == '__main__':
    app.run()
