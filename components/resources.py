from flask_restful import Resource, marshal_with
from models import *
from extensions import db
from .src.fields import *
from .src.args import *

class ClientResource(Resource):
    @marshal_with(client_fields)
    def get(self):
        client = Client.query.all()
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
                    setattr(client, arg, args[arg])
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
                    setattr(promotion, arg, args[arg])
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

class ConventionResource(Resource):

    @marshal_with(convention_fields)
    def get(self):
        convention = Convention.query.all()
        return convention
    
    @marshal_with(convention_fields)
    def post(self):
        args = post_convention_args.parse_args()
        convention = Convention.query.filter_by(idcv=args['idcv']).first()
        if convention:
            response = {'message': 'Convention already exists!'}
        else:
            new_convention = Convention(**args)
            db.session.add(new_convention)
            db.session.commit()
            response = {'message': 'Convention created!'}
        return response
    
    @marshal_with(convention_fields)
    def put(self):
        args = put_convention_args.parse_args()
        convention = Convention.query.filter_by(idcv=args['idcv']).first()
        if convention:
            for arg in args:
                if arg:
                    setattr(convention, arg, args[arg])
                db.session.commit()
            response = {'message': 'Convention updated!'}
        else:
            response = {'message': 'Convention does not exist!'}
        return response
    
    @marshal_with(convention_fields)
    def delete(self):
        args = put_convention_args.parse_args()
        convention = Convention.query.filter_by(idcv=args['idcv']).first()
        if convention:
            db.session.delete(convention)
            db.session.commit()
            response = {'message': 'Convention deleted!'}
        else:
            response = {'message': 'Convention does not exist!'}
        return response

class LineResource(Resource):
    @marshal_with(line_fields)
    def get(self):
        line = Line.query.all()
        return line
    
    @marshal_with(line_fields)
    def post(self):
        args = post_line_args.parse_args()
        line = Line.query.filter_by(idl=args['idl']).first()
        if line:
            response = {'message': 'Line already exists!'}
        else:
            new_line = Line(**args)
            db.session.add(new_line)
            db.session.commit()
            response = {'message': 'Line created!'}
        return response
    
    @marshal_with(line_fields)
    def put(self):
        args = put_line_args.parse_args()
        line = Line.query.filter_by(idl=args['idl']).first()
        if line:
            for arg in args:
                if arg:
                    setattr(line, arg, args[arg])
                db.session.commit()
            response = {'message': 'Line updated!'}
        else:
            response = {'message': 'Line does not exist!'}
        return response
    
    @marshal_with(line_fields)
    def delete(self):
        args = put_line_args.parse_args()
        line = Line.query.filter_by(idl=args['idl']).first()
        if line:
            db.session.delete(line)
            db.session.commit()
            response = {'message': 'Line deleted!'}
        else:
            response = {'message': 'Line does not exist!'}
        return response

class HistoryResource(Resource):
    @marshal_with(history_fields)
    def get(self):
        history = History.query.all()
        return history
    
    @marshal_with(history_fields)
    def post(self):
        args = post_history_args.parse_args()
        history = History.query.filter_by(id=args['id']).first()
        if history:
            response = {'message': 'History already exists!'}
        else:
            new_history = History(**args)
            db.session.add(new_history)
            db.session.commit()
            response = {'message': 'History created!'}
        return response

    @marshal_with(history_fields)
    def put(self):
        args = put_history_args.parse_args()
        history = History.query.filter_by(id=args['id']).first()
        if history:
            for arg in args:
                if arg:
                    setattr(history, arg, args[arg])
                db.session.commit()
            response = {'message': 'History updated!'}
        else:
            response = {'message': 'History does not exist!'}
        return response
    
    @marshal_with(history_fields)
    def delete(self):
        args = put_history_args.parse_args()
        history = History.query.filter_by(id=args['id']).first()
        if history:
            db.session.delete(history)
            db.session.commit()
            response = {'message': 'History deleted!'}
        else:
            response = {'message': 'History does not exist!'}
        return response

class TransformResource(Resource):
    @marshal_with(transform_fields)
    def get(self):
        transform = Transform.query.all()
        return transform
    
    @marshal_with(transform_fields)
    def post(self):
        args = post_transform_args.parse_args()
        transform = Transform.query.filter_by(idt=args['idt']).first()
        if transform:
            response = {'message': 'Transform already exists!'}
        else:
            new_transform = Transform(**args)
            db.session.add(new_transform)
            db.session.commit()
            response = {'message': 'Transform created!'}
        return response
    
    @marshal_with(transform_fields)
    def put(self):
        args = put_transform_args.parse_args()
        transform = Transform.query.filter_by(idt=args['idt']).first()
        if transform:
            for arg in args:
                if arg:
                    setattr(transform, arg, args[arg])
                db.session.commit()
            response = {'message': 'Transform updated!'}
        else:
            response = {'message': 'Transform does not exist!'}
        return response
    
    @marshal_with(transform_fields)
    def delete(self):
        args = put_transform_args.parse_args()
        transform = Transform.query.filter_by(idt=args['idt']).first()
        if transform:
            db.session.delete(transform)
            db.session.commit()
            response = {'message': 'Transform deleted!'}
        else:
            response = {'message': 'Transform does not exist!'}
        return response

class CessionResource(Resource):
    @marshal_with(cession_fields)
    def get(self):
        cession = Cession.query.all()
        return cession
    
    @marshal_with(cession_fields)
    def post(self):
        args = post_cession_args.parse_args()
        cession = Cession.query.filter_by(idcs=args['idcs']).first()
        if cession:
            response = {'message': 'Cession already exists!'}
        else:
            new_cession = Cession(**args)
            db.session.add(new_cession)
            db.session.commit()
            response = {'message': 'Cession created!'}
        return response
    
    @marshal_with(cession_fields)
    def put(self):
        args = put_cession_args.parse_args()
        cession = Cession.query.filter_by(idcs=args['idcs']).first()
        if cession:
            for arg in args:
                if arg:
                    setattr(cession, arg, args[arg])
                db.session.commit()
            response = {'message': 'Cession updated!'}
        else:
            response = {'message': 'Cession does not exist!'}
        return response

    @marshal_with(cession_fields)
    def delete(self):
        args = put_cession_args.parse_args()
        cession = Cession.query.filter_by(idcs=args['idcs']).first()
        if cession:
            db.session.delete(cession)
            db.session.commit()
            response = {'message': 'Cession deleted!'}
        else:
            response = {'message': 'Cession does not exist!'}
        return response





