from app import make_app 

if __name__ == '__main__':
    app = make_app()
    server = app.server
    app.run_server(debug=True)