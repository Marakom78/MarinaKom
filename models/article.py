from models.active_record_entity import ActiveRecordEntity
from models.user import User

class Article(ActiveRecordEntity):
  # __tablename__ = 'table1'
  _id = None
  _author_id = None
  _name = None
  _text = None
  _created_at = None

  def get_author_id(self):
    return self._author_id

  def get_name(self):
    return self._name

  def get_text(self):
    return self._text

  def get_created_at(self):
    return self._created_at

  def get_author(self):
    return User.get_by_id(self._author_id)
    
    
  
  def set_author_id(self, author_id):
    self._author_id = author_id

  def set_name(self, name):
    self._name = name

  def set_text(self, text):
    self._text = text
  # def set_created_at(self, created_at):
  #   self._created_at = created_at

  @staticmethod
  def get_table_name():
    return 'articles'