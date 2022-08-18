from app import make_app 

app = make_app()
server = make_app().server

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
