import requests
import configuration
import data

def post_orders(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body,
                         headers=data.header_content)

def get_orders(parameters):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS,
                        params=parameters)
