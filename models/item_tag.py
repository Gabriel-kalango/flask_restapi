from db import db
class ItemTagsModel(db.Model):
    __tablename__="item_tags"
    id=db.Column(db.Integer,primary_key=True)
    items_id=db.Column(db.Integer, db.ForeignKey("items.id"),nullable=False)
    tags_id=db.Column(db.Integer,db.ForeignKey("tags.id"),nullable=False)