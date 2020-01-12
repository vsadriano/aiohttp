from aiohttp import web
from app.server import Server

def main():
    Server().run()

if __name__ == "__main__":
    main()
