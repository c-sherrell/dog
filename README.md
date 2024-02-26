# dog
CS 361
Group 26
Microservice Communication Contract
Chris Sherrell - Microservice Author
Jacob Kaiser - Microservice User

NAME
    dog.py

ABOUT
    This microservice can be used to get random images and facts about dogs.
    It uses REST API via Flask for communication.

    It has two functions:
        1. get_img() called with route '/get/dog/image'
            a. This function takes no arguments and returns a random dog image.

        2. get_fact() called with route '/get/dog/fact'
            b. This function takes no arguments and returns a random dog fact.

REQUEST
    To request data, run the microservice on a local server.  In the program requesting the data,
    send a GET request to the appropriate endpoint depending on whether you want to request a
    random dog image or fact.

    Example dog image call (using Python):
        import requests

        img_route = 'http://127.0.0.1:5000/get/dog/image'
        img_response = requests.get(img_route)

    Example dog fact call (using Python):
        import requests

        fact_route = 'http://127.0.0.1:5000/get/dog/fact'
        fact_response = requests.get(fact_route)

RECEIVE
    To receive data, store the response returned by the GET request (shown above) and extract
    the content of the response.

    Example dog image receive
    (using Python to receive the image file and display it using BytesIO and PIL):
        import requests
        import io
        from PIL import Image

        img_route = 'http://127.0.0.1:5000/get/dog/image'
        img_response = requests.get(img_route)
        img_response_content = img_response.content
        img_content = io.BytesIO(img_response_content)
        img = Image.open(img_content)
        img.show()

    Example dog fact receive
    (using Python to receive the fact and display it as a string):
        import requests

        fact_route = 'http://127.0.0.1:5000/get/dog/fact'
        fact_response = requests.get(fact_route)
        fact_response_content = fact_response.content
        fact = fact.decode('utf-8')
        print(fact)
        
UML SEQUENCE DIAGRAM
[CS361 Microservice UML Sequence Diagram.pdf](https://github.com/c-sherrell/dog/files/14399637/CS361.Microservice.UML.Sequence.Diagram.pdf)


