from flask import Flask, request, Response

app = Flask(__name__)

# @app.route('/sum')
# def calc():
#     number = request.args.get('a')
#     return str(int(number)*5)

filename = "test.txt"


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


@app.route('/red')
def viv():
    return read_file(filename)


def add(shapka, body, filename):
    with open(filename, "a+") as file:
        file.write(f"{shapka}\n{body}\n")


@app.route('/new')
def new():
    zagolovok = request.args.get('z')
    telo = request.args.get('x')
    add(zagolovok, telo, filename)
    return Response()


def delete(filename):
    with open(filename, "w") as file:
        file.write('')


@app.route('/del')
def nayn():
    delete(filename)
    return Response()


if __name__ == '__main__':
    app.run()
