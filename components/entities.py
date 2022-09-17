from extensions import db
from flask_restful import Resource, marshal_with
from models import History, Line, Convention, Promotion, Client

from .src.args import put_history_entity_args, put_promotion_args, post_promotion_args, \
    put_client_args, post_client_args
from .src.fields import history_entity_fields, promotion_fields, client_fields


class EntityResource(Resource):
    @marshal_with(history_entity_fields)
    def get(self, id):
        # extract the fields from the database by history id
        query = db.session.query(History.id, History.date, Promotion.namepr,
                                 Promotion.typepr, Convention.namecv, Line.numberl,
                                 Line.street, Line.serv). \
            filter(History.id == id). \
            join(Promotion, History.idp == Promotion.idp). \
            join(Convention, History.idcv == Convention.idcv). \
            join(Line, History.idl == Line.idl)

        return query.all()

    @marshal_with(history_entity_fields)
    def put(self, id):
        # update the values of database tables by history id
        # im sure this is a bad practice and theres better ways to do this
        args = put_history_entity_args.parse_args()
        history_query = db.session.query(History).filter(History.id == id).first()
        if args['date']:
            history_query.date = args['date']
            db.session.commit()
        if args['namepr']:
            promotion_query = db.session.query(Promotion).filter(Promotion.idp == history_query.idp).first()
            promotion_query.namepr = args['namepr']
            db.session.commit()
        if args['typepr']:
            promotion_query = db.session.query(Promotion).filter(Promotion.idp == history_query.idp).first()
            promotion_query.typepr = args.typepr
            db.session.commit()
        if args['namecv']:
            convention_query = db.session.query(Convention).filter(Convention.idcv == history_query.idcv).first()
            convention_query.namecv = args.namecv
            db.session.commit()
        if args['numberl']:
            line_query = db.session.query(Line).filter(Line.idl == history_query.idl).first()
            line_query.numberl = args.numberl
            db.session.commit()
        if args['street']:
            line_query = db.session.query(Line).filter(Line.idl == history_query.idl).first()
            line_query.street = args.street
            db.session.commit()
        if args['serv']:
            line_query = db.session.query(Line).filter(Line.idl == history_query.idl).first()
            line_query.serv = args.serv
            db.session.commit()


class PromotionResource(Resource):
    @marshal_with(promotion_fields)
    def get(self):
        promotion = Promotion.query.all()
        return promotion

    @marshal_with(promotion_fields)
    def post(self):
        args = post_promotion_args.parse_args()
        promotion = Promotion.query.filter_by(idp=args['idp']).first()
        if promotion:
            response = {'message': 'Promotion already exists!'}
        else:
            new_promotion = Promotion(**args)
            db.session.add(new_promotion)
            db.session.commit()
            response = {'message': 'Promotion created!'}
        return response

    @marshal_with(promotion_fields)
    def put(self):
        args = put_promotion_args.parse_args()
        promotion = Promotion.query.filter_by(idp=args['idp']).first()
        if promotion:
            for arg in args:
                if arg:
                    promotion.arg = args[arg]
                db.session.commit()
            response = {'message': 'Promotion updated!'}
        else:
            response = {'message': 'Promotion does not exist!'}
        return response

    @marshal_with(promotion_fields)
    def delete(self):
        args = put_promotion_args.parse_args()
        promotion = Promotion.query.filter_by(idp=args['idp']).first()
        if promotion:
            db.session.delete(promotion)
            db.session.commit()
            response = {'message': 'Promotion deleted!'}
        else:
            response = {'message': 'Promotion does not exist!'}
        return response


class ClientResource(Resource):
    @marshal_with(client_fields)
    def get(self):
        args = put_client_args.parse_args()
        client = Client.query.filter_by(idc=args['idc']).all()
        return client

    @marshal_with(client_fields)
    def post(self):
        print("post")
        args = post_client_args.parse_args()
        print(args)
        client = Client.query.filter_by(idc=args['idc']).first()
        if client:
            print("client exist")
            response = {'message': 'Client already exists!'}
        else:
            new_client = Client(**args)
            db.session.add(new_client)
            db.session.commit()
            print("client added")
            response = {'message': 'Client created!'}
        return response

    @marshal_with(client_fields)
    def put(self):
        args = put_client_args.parse_args()
        client = Client.query.filter_by(idc=args['idc']).first()
        if client:
            for arg in args:
                if arg:
                    client.arg = args[arg]
                db.session.commit()
            response = {'message': 'Client updated!'}
        else:
            response = {'message': 'Client does not exist!'}
        return response

    @marshal_with(client_fields)
    def delete(self):
        args = put_client_args.parse_args()
        client = Client.query.filter_by(idc=args['idc']).first()
        if client:
            db.session.delete(client)
            db.session.commit()
            response = {'message': 'Client deleted!'}
        else:
            response = {'message': 'Client does not exist!'}
        return response
