from extensions import db


# 1-CLIENT
class Client(db.Model):
    _tablename_ = 'client'
    idc = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    prename = db.Column(db.String(255))
    birthday = db.Column(db.DateTime)
    idcard = db.Column(db.String(255))
    releasecrd = db.Column(db.DateTime)
    Phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    line_c = db.relationship('Line', backref=db.backref('client', lazy='select'))
    ces1 = db.relationship('Cession', backref=db.backref('client', lazy='select'))
    hisr = db.relationship('History', backref=db.backref('client', lazy='select'))


# 2-PROMOTION
class Promotion(db.Model):
    _tablename_ = 'promotion'
    idp = db.Column(db.Integer, primary_key=True)
    namepr = db.Column(db.String(255))
    typepr = db.Column(db.String(255))
    mountpr = db.Column(db.String(255))
    hisr = db.relationship('History', backref=db.backref('promotion', lazy='select'))


# 3-convention
class Convention(db.Model):
    _tablename_ = 'convention'
    idcv = db.Column(db.Integer, primary_key=True)
    namecv = db.Column(db.String(255))
    remise = db.Column(db.Integer)
    hisr = db.relationship('History', backref=db.backref('convention', lazy='select'))


# 4-Line
class Line(db.Model):
    _tablename_ = 'line'
    idl = db.Column(db.Integer, primary_key=True)
    numberl = db.Column(db.String(255))
    street = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    idc = db.Column(db.Integer, db.ForeignKey('client.idc'))
    serv = db.Column(db.Integer)
    rtrans = db.relationship('Transform', backref=db.backref('line', lazy='select'))
    rcession = db.relationship('Cession', backref=db.backref('line', lazy='select'))
    hisr = db.relationship('History', backref=db.backref('line', lazy='select'))


# History
class History(db.Model):
    _tablename_ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    idc = db.Column(db.Integer, db.ForeignKey('client.idc'))
    idl = db.Column(db.Integer, db.ForeignKey('line.idl'))
    date = db.Column(db.DateTime)
    idp = db.Column(db.Integer, db.ForeignKey('promotion.idp'))
    idcv = db.Column(db.Integer, db.ForeignKey('convention.idcv'))
    idtr = db.Column(db.Integer, db.ForeignKey('transform.idt'))
    idcs = db.Column(db.Integer, db.ForeignKey('cession.idcs'))
    # Transform


class Transform(db.Model):
    _tablename_ = 'transform'
    idt = db.Column(db.Integer, primary_key=True)
    street1 = db.Column(db.String(255))
    street2 = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    idl = db.Column(db.Integer, db.ForeignKey('line.idl'))
    hisr = db.relationship('History', backref=db.backref('transform', lazy='select'))
    # Cession


class Cession(db.Model):
    _tablename_ = 'cession'
    idcs = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    idl = db.Column(db.Integer, db.ForeignKey('line.idl'))
    ces = db.Column(db.Integer, db.ForeignKey('client.idc'))
    hisr = db.relationship('History', backref=db.backref('cession', lazy='select'))
