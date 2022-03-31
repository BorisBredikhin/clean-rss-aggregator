import configparser
import uvicorn

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")

    uvicorn.run('main:app', reload=True, port=int(config['server']['PORT']))
