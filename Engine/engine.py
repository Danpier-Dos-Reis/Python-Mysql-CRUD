from DAL import dal

def initialize():
    dal.create_table()

def create_item(nombre, fecha, linkurl, nulos):
    dal.insert_item(nombre, fecha, linkurl, nulos)

def read_items():
    return dal.get_items()

def read_item(item_id):
    return dal.get_item_by_id(item_id)

def update_item(item_id, nombre, fecha, linkurl, nulos):
    dal.update_item(item_id, nombre, fecha, linkurl, nulos)

def delete_item(item_id):
    dal.delete_item(item_id)