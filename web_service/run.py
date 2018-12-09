# import the app variable that is a member of the app package
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
