from flask_restful import Resource, marshal_with
from models import *
from extensions import db
from .src.fields import *
from .src.args import *


class EntityResource(Resource):
    entity_fields = {  
    'id',
    'date',
    'promotion_namepr',
    'promotion_typepr',
    'convention_namecv',
    'line_numberl',
    'line_street',
    'line_serv',
    'cession_idcs',
}
    @marshal_with(history_entity_fields)
    def get(self, id):
    # extract the fields from the database by history id
        query = db.session.query(History.id, History.date, Promotion.namepr, 
                             Promotion.typepr, Convention.namecv, Line.numberl,
                             Line.street, Line.serv, Cession.idcs, History.idtr).\
                                filter(History.id == id).\
                                    join(Promotion , History.idp == Promotion.idp).\
                                        join(Convention, History.idcv == Convention.idcv).\
                                            join(Line, History.idl == Line.idl).\
                                                join(Cession, History.idcs == Cession.idcs)
                                                
        return query.all()
        
        
