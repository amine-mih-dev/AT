from models import db, Client
from extensions import *

from flask_restful import fields,Resource, marshal_with,Api ,reqparse
   
db.init_app(app)

with app.app_context():
    #db.create_all()
    pass
   
@app.route('/')
def hello():
    return "Dia"



from components.resources import ConventionResource
api.add_resource(ConventionResource, '/convention')

from components.resources import LineResource
api.add_resource(LineResource, '/line')

from components.resources import TransformResource
api.add_resource(TransformResource, '/transform')

from components.resources import CessionResource
api.add_resource(CessionResource, '/cession')

from components.resources import HistoryResource
api.add_resource(HistoryResource, '/history')



from components.entities import ClientResource
api.add_resource(ClientResource, '/client')

from components.entities import PromotionResource
api.add_resource(PromotionResource, '/promotion')

from components.entities import EntityResource
api.add_resource(EntityResource, '/entity/<int:id>')

if __name__ == "__main__":
        app.run(debug=True)
