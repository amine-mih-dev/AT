from models import db
from extensions import *

from flask_restful import fields,Resource, marshal_with,Api

         
db.init_app(app)

with app.app_context():
    db.create_all()
    pass
   

@app.route('/')
def hello():
    return "Dia"
if __name__ == "__main__":
        app.run(debug=True)
