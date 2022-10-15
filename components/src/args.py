from flask_restful import reqparse
from datetime import datetime

get_client_args = reqparse.RequestParser()
get_client_args.add_argument('idc', type=int, help='Client id')

post_client_args = reqparse.RequestParser()
post_client_args.add_argument("idc", type=int, help="idc is required", required=True)
post_client_args.add_argument("name", type=str, help="name is required", required=True)
post_client_args.add_argument("prename", type=str, help="prename is required", required=True)
post_client_args.add_argument("birthday",type=lambda x: datetime.strptime(x, '%Y-%m-%d'), help="birthday is required", required=True)
post_client_args.add_argument("idcard", type=str, help="idcard is required", required=True)
post_client_args.add_argument("releasecrd", type=lambda x: datetime.strptime(x, '%Y-%m-%d'), help="releasecrd is required", required=True)
post_client_args.add_argument("Phone", type=str, help="Phone is required", required=True)
post_client_args.add_argument("email", type=str, help="email is required", required=True)

put_client_args = reqparse.RequestParser()
put_client_args.add_argument("idc", type=int, help="idc is required", required=True)
put_client_args.add_argument("name", type=str,  required=False)
put_client_args.add_argument("prename", type=str,  required=False)
put_client_args.add_argument("birthday", type=lambda x: datetime.strptime(x,'%Y-%m-%d'),  required=False)
put_client_args.add_argument("idcard", type=str,  required=False)
put_client_args.add_argument("releasecrd", type=lambda x: datetime.strptime(x,'%Y-%m-%d'),  required=False)
put_client_args.add_argument("Phone", type=str,  required=False)
put_client_args.add_argument("email", type=str,  required=False)


post_line_args = reqparse.RequestParser()
post_line_args.add_argument("idl", type=int, help="idl is required", required=True)
post_line_args.add_argument("numberl", type=str, help="Number of the line is required", required=True)
post_line_args.add_argument("street", type=str, help="Street of the line is required", required=True)
post_line_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="Date of the line is required", required=True)
post_line_args.add_argument("idc", type=int, help="Id of the client is required", required=True)
post_line_args.add_argument("serv", type=int, help="Service of the line is required", required=True)

put_line_args = reqparse.RequestParser()
put_line_args.add_argument("idl", type=int, help="idl is required", required=False)
put_line_args.add_argument("numberl", type=str,  required=False)
put_line_args.add_argument("street", type=str,  required=False)
put_line_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="Date of the line is required", required=False)
put_line_args.add_argument("idc", type=int, required=False)
put_line_args.add_argument("serv", type=int,  required=False)


post_transform_args = reqparse.RequestParser()
post_transform_args.add_argument("idt", type=int, help="idt is required", required=True)
post_transform_args.add_argument("street1", type=str, help="Street1 of the transform is required", required=True)
post_transform_args.add_argument("street2", type=str, help="Street2 of the transform is required", required=True)
post_transform_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="Date of the transform is required", required=True)


put_transform_args = reqparse.RequestParser()
put_transform_args.add_argument("idt", type=int, help="idt is required", required=True)
put_transform_args.add_argument("street1", type=str,  required=False)
put_transform_args.add_argument("street2", type=str,  required=False)
put_transform_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="Date of the transform is required", required=False)


post_history_args = reqparse.RequestParser()
post_history_args.add_argument("id", type=int, help="id is required", required=True)
post_history_args.add_argument("idc", type=int, help="idc is required", required=True)
post_history_args.add_argument("idl", type=int, help="idl is required", required=True)
post_history_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="date is required", required=True)
post_history_args.add_argument("idp", type=int, help="idp is required", required=True)
post_history_args.add_argument("idcv", type=int, help="idcv is required", required=True)
post_history_args.add_argument("idtr", type=int, help="idtr is required", required=True)
post_history_args.add_argument("idcs", type=int, help="idcs is required", required=True)

put_history_args = reqparse.RequestParser()
put_history_args.add_argument("id", type=int, help="id is required", required=True)
put_history_args.add_argument("idc", type=int,  required=False)
put_history_args.add_argument("idl", type=int,  required=False)
put_history_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'),  required=False)
put_history_args.add_argument("idp", type=int,  required=False)
put_history_args.add_argument("idcv", type=int,  required=False)
put_history_args.add_argument("idtr", type=int,  required=False)
put_history_args.add_argument("idcs", type=int,  required=False)

get_history_args = reqparse.RequestParser()
get_history_args.add_argument("id", type=int, help="id is required", required=True)

post_cession_args = reqparse.RequestParser()
post_cession_args.add_argument("idcs", type=int, help="idcs is required", required=True)
post_cession_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="date is required", required=True)
post_cession_args.add_argument("idl", type=int, help="idl is required", required=True)
post_cession_args.add_argument("ces", type=int, help="ces is required", required=True)

put_cession_args = reqparse.RequestParser()
put_cession_args.add_argument("idcs", type=int, help="idcs is required", required=True)
put_cession_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'),  required=False)
put_cession_args.add_argument("idl", type=int,  required=False)
put_cession_args.add_argument("ces", type=int,  required=False)

post_promotion_args = reqparse.RequestParser()
post_promotion_args.add_argument("idp", type=int, help="idp is required", required=True)
post_promotion_args.add_argument("namepr", type=str, help="namepr is required", required=True)
post_promotion_args.add_argument("typepr", type=str, help="typepr is required", required=True)
post_promotion_args.add_argument("mountpr", type=str, help="mountpr is required", required=True)

put_promotion_args = reqparse.RequestParser()
put_promotion_args.add_argument("idp", type=int, help="idp is required", required=True)
put_promotion_args.add_argument("namepr", type=str,  required=False)
put_promotion_args.add_argument("typepr", type=str,  required=False)
put_promotion_args.add_argument("mountpr", type=str,  required=False)

post_convention_args = reqparse.RequestParser()
post_convention_args.add_argument("idcv", type=int, help="idcv is required", required=True)
post_convention_args.add_argument("namecv", type=str, help="namecv is required", required=True)
post_convention_args.add_argument("remise", type=int, help="remise is required", required=True)

put_convention_args = reqparse.RequestParser()
put_convention_args.add_argument("idcv", type=int, help="idcv is required", required=True)
put_convention_args.add_argument("namecv", type=str,  required=False)
put_convention_args.add_argument("remise", type=int,  required=False)



post_history_entity_args = reqparse.RequestParser()
post_history_entity_args.add_argument("id", type=int, help="id is required", required=True)
post_history_entity_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'), help="date is required", required=True)
post_history_entity_args.add_argument("namepr", type=str, help="promotion_namepr is required", required=True)
post_history_entity_args.add_argument("typepr", type=str, help="promotion_typepr is required", required=True)
post_history_entity_args.add_argument("namecv", type=str, help="convention_namecv is required", required=True)
post_history_entity_args.add_argument("numberl", type=str, help="line_numberl is required", required=True)
post_history_entity_args.add_argument("street", type=str, help="line_street is required", required=True)
post_history_entity_args.add_argument("serv", type=int, help="line_serv is required", required=True)

put_history_entity_args = reqparse.RequestParser()
put_history_entity_args.add_argument("id", type=int, help="id is required", required=True)
put_history_entity_args.add_argument("date", type=lambda x: datetime.strptime(x,'%Y-%m-%d'),  required=False)
put_history_entity_args.add_argument("namepr", type=str,  required=False)
put_history_entity_args.add_argument("typepr", type=str,  required=False)
put_history_entity_args.add_argument("namecv", type=str,  required=False)
put_history_entity_args.add_argument("numberl", type=str,  required=False)
put_history_entity_args.add_argument("street", type=str,  required=False)
put_history_entity_args.add_argument("serv", type=int,  required=False)

