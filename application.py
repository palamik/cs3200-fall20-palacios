from flask import Flask, jsonify

application = Flask('hello')

@application.route('/')
def hello():
    return """
        <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Insert title here</title>
                </head>
                <body>
                    <h1>Hello Jose Annunziato!</h1>
                </body>
            </html>
    """

@application.route('/api/hello/string')
def hello_string():
    return "Hello Miguel Palacios"

@application.route('/api/hello/object')
def hello_object():
    return jsonify({
        "message": "Hello Miguel Palacios"
    })


if __name__ == "__main__":
    application.run()