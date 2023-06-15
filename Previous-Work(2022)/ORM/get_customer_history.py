import csv

from sqlalchemy.orm import create_session
import delphi

def run():
    session = create_session(bind = delphi.Engine)

    query = session.query(delphi.Customer, delphi.Order, delphi.OrderItem, delphi.Item, delphi.OrderItemCustomization, delphi.Customization) \
                   .join(delphi.Order, delphi.Customer.customer_id == delphi.Order.customer_id) \
                   .join(delphi.OrderItem, delphi.Order.order_id == delphi.OrderItem.order_id) \
                   .join(delphi.Item, delphi.OrderItem.item_id == delphi.Item.item_id) \
                   .outerjoin(delphi.OrderItemCustomization, (delphi.OrderItem.item_id == delphi.OrderItemCustomization.item_id) & (delphi.OrderItem.order_id == delphi.OrderItemCustomization.order_id)) \
                   .outerjoin(delphi.Customization, delphi.OrderItemCustomization.customization_id == delphi.Customization.customization_id)

    columns = ['customer_id', 'opt_in', 'birthday', 'gender', 'order_id', 'weather', 'order_timestamp', 'item_id', \
               'item_name', 'item_description', 'item_image', 'price', 'taste_profile', 'item_type', 'customization_id', 'customization']
    rows = []

    for customer, order, orderitem, item, orderitemcustomization, customization in query:
        rows.append([customer.customer_id, customer.opt_in, customer.birthday, customer.gender, \
                     order.order_id, order.weather, order.order_timestamp, \
                     item.item_id, item.item_name, item.item_description, item.item_image, item.price, item.taste_profile, item.item_type, \
                     customization.customization_id if customization else None, customization.customization if customization else None])

    with open('CSVs/customer_orders.csv', 'w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(columns)
        csvwriter.writerows(rows)

if __name__ == '__main__':
    run()
