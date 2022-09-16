from flask_restful import fields

# define the fields to be returned in the json response
history_fields = {
    'id': fields.Integer,
    'idc': fields.Integer,
    'idl': fields.Integer,
    'date': fields.DateTime,
    'idp': fields.Integer,
    'idcv': fields.Integer,
    'idtr': fields.Integer,
    'idcs': fields.Integer, 
}

cession_fields = {
    'idcs': fields.Integer,
    'date': fields.DateTime,
    'idl': fields.Integer,
    'ces': fields.Integer,
}

transform_fields = {
    'idt': fields.Integer,
    'street1': fields.String,
    'street2': fields.String,
    'date': fields.DateTime,
    'idl': fields.Integer
}

line_fields = {
    'idl': fields.Integer,
    'numberl': fields.String,
    'street': fields.String,
    'date': fields.DateTime,
    'idc': fields.Integer,
    'serv': fields.Integer,
}

promotion_fields = {
    'idp': fields.Integer,
    'namepr': fields.String,
    'typepr': fields.String,
    'mountpr': fields.String,
}

convention_fields = {
    'idcv': fields.Integer,
    'namecv': fields.String,
    'remise': fields.Integer,
}

client_fields = {

    'idc': fields.Integer,
    'name': fields.String,
    'prename': fields.String,
    'birthday': fields.DateTime,
    'idcard': fields.String,
    'releasecrd': fields.DateTime,
    'Phone': fields.String,
    'email': fields.String,
}

history_entity_fields = {  
    'id': fields.Integer,
    'date': fields.DateTime,
    'namepr': fields.String,
    'typepr': fields.String,
    'namecv': fields.String,
    'numberl': fields.String,
    'street': fields.String,
    'serv': fields.Integer
}
