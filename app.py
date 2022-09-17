from extensions import *
from components.resources import ConventionResource
from components.resources import LineResource
from components.resources import TransformResource
from components.resources import CessionResource
from components.resources import HistoryResource
from components.entities import ClientResource
from components.entities import PromotionResource
from components.entities import EntityResource

db.init_app(app)

with app.app_context():
    # db.create_all()
    pass


@app.route('/')
def hello():
    return "Dia"


api.add_resource(ConventionResource, '/convention')
api.add_resource(LineResource, '/line')
api.add_resource(TransformResource, '/transform')
api.add_resource(CessionResource, '/cession')
api.add_resource(HistoryResource, '/history')
api.add_resource(ClientResource, '/client')
api.add_resource(PromotionResource, '/promotion')
api.add_resource(EntityResource, '/entity/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
