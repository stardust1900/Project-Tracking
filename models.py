from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()


association_table = db.Table('project_supporter',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    login_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    dept_id = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=True)

class Dept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 商户名称	
    merchant_name = db.Column(db.String(255), nullable=False)
    # 产品	
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    # 产品详情	项目说明
    instruction = db.Column(db.String(1024), nullable=False)
    # 提交日期	
    input_date = db.Column(db.String(10), nullable=False)
    # 上线日期	
    launch_date = db.Column(db.String(10), nullable=True)
    # 归属部门	
    dept_id =  db.Column(db.Integer, db.ForeignKey('dept.id'), nullable=False)
    # 客户经理	
    manager_id =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    # 项目状态 0-初始 1-对接中 2-对接完成待上线 3-已上线 4-本周无进展 5-两周无进展 6-长期无进展 7-终止
    state = db.Column(db.SmallInteger,nullable=False,default=0)
    # 备注
    remark = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=True)
    create_by = db.Column(db.Integer)
    update_by = db.Column(db.Integer)

    product = db.relationship('Product', foreign_keys=[product_id], backref=db.backref('projects', lazy='dynamic'))
    manager = db.relationship('User', foreign_keys=[manager_id], backref=db.backref('managed_projects', lazy='dynamic'))
    dept = db.relationship('Dept', foreign_keys=[dept_id], backref=db.backref('projects', lazy='dynamic'))
    # 技术支持
    supporters = db.relationship('User', secondary=association_table, backref=db.backref('projects', lazy='dynamic'))
    # 项目近期进展	
    logs = db.relationship('Log', back_populates='project')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sort = db.Column(db.Integer)
    level = db.Column(db.Integer,default=0)
    parent_id = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=True)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    content = db.Column(db.String(1024),nullable=False)
    user_id =  db.Column(db.Integer, nullable=False)
    input_date = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=True)
    create_by = db.Column(db.Integer)
    update_by = db.Column(db.Integer)
    project = db.relationship('Project', back_populates='logs')