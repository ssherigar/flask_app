Flask Web Application

Task:
Create a web service which combines two existing web services.

Docker Commands:

docker build -t flask-app .

docker run -p 5000:5000 flask-app

Container is now running and port 5000 is mapped.

You can visit http://127.0.0.1:5000/ and see the Flask application 
running.

Test

pytest test_webservice.py
