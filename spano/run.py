#!/usr/bin/env python

from spano.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)


#def main():
#  from spano.app import create_app
#  app = create_app()
#  app.run(debug=True, port=5000)
#
#main()
