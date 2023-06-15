from sqlalchemy.orm import create_session
import delphi

if __name__ == '__main__':
    session = create_session(bind = delphi.Engine)
    
    # print('Order')
    # for row in session.query(delphi.Order).where(delphi.Order.customer_id == 5):
    #     print(row)

    # print('\nNutritionFacts')
    # for row in session.query(delphi.NutritionFacts):
    #     print(row)

    # print('\nItem')
    # for row in session.query(delphi.Item).where(delphi.Item.item_name == 'Cheeseburger'):
    #     print(row)

    print('Item')
    for row in session.query(delphi.Item):
        print(row.get_item_name())
