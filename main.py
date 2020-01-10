from aiohttp import web
from application.server import Server

def main():
    Server().run()

if __name__ == "__main__":
    main()
