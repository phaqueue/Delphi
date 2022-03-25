from sqlalchemy.orm import create_session
import delphi

if __name__ == '__main__':
    session = create_session(bind = delphi.Engine)
    
    # for row in session.query(delphi.Order).where(delphi.Order.customer_id == 5):
    #     print(row)

    # for row in session.query(delphi.NutritionFacts):
    #     print(row)

    # for row in session.query(delphi.Item).where(delphi.Item.item_name == 'Cheeseburger'):
    #     print(row)
