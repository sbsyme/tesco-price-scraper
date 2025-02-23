from meal_planner_db_interface import insert_item, get_items, select_item_by_id

def create_item(name, price):
    return insert_item(name, price)

def get_all_items():
    return get_items()

def get_item_by_id(item_id):
    return select_item_by_id(item_id)