#!/usr/bin/env python

from app import app, db

db.create_all()
#app.run(host='0.0.0.0', port=8000)
if __name__ == '__main__':
  app.run(debug=True)
