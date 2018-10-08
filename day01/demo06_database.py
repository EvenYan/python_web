from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    passwd = db.Column(db.String(50))


if __name__ == "__main__":
    # 清除数据库中所有数据(第一次)
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 添加一条数据
    # 创建对象
    user1 = User(name="Tom", passwd="123455")
    # session记录对象任务
    db.session.add(user1)
    # 提交任务到数据库中
    db.session.commit()

    # 添加多条数据
    user2 = User(name="Alice", passwd="123456")
    user3 = User(name="Tim", passwd="123456")
    db.session.add_all([user2, user3])
    db.session.commit()

    # 查询单条数据
    name1 = User.query.get(2).name
    print(name1)

    passwd = User.query.first().passwd
    print(passwd)

    user1 = User.query.filter_by(name="Tom", id=1).first()
    print(user1)

    user2 = db.session.query(User).first()
    print(user2)

    # 查询多条数据
    users1 = User.query.all()
    users2 = db.session.query(User).all()
    query = User.query.filter_by(name="Alice")
    users3 = User.query.filter_by(name="Tom", id=1).all()
    print(users1)
    print(users2)
    print(query)
    print(users3)

    # 高级查询
    from sqlalchemy import or_, and_, not_
    from sqlalchemy import func
    users4 = User.query.filter(or_(User.name == 'Tom', User.passwd.startswith('123'))).all()
    users5 = User.query.offset(1).limit(2).all()
    users6 = User.query.order_by(User.id.desc()).all()
    users7 = db.session.query(User.passwd).group_by(User.passwd).all()
    users8 = db.session.query(User.passwd, func.count(User.passwd)).group_by(User.passwd).all()
    print("advance")
    print(users4)
    print(users5)
    print(users6)
    print(users7)
    print(users8)

    # 更新
    user = User.query.get(2)
    user.name = "Even"
    db.session.add(user)
    db.session.commit()
    User.query.filter_by(name="Even").update({'name': 'EvenYan', 'passwd': 'Even'})
    db.session.commit()

    # 删除操作
    user = User.query.get(2)
    db.session.delete(user)
    db.session.commit()






