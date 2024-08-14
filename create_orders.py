# Левицкая Кристина 20-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def create_orders():
   current_order_body = data.order_body.copy()
   current_order_body ["firstName"] = "Ван"
   track = sender_stand_request.post_orders(current_order_body)c
   return str(track.json()["track"])

def positive_assert():
    track = create_orders()
    current_params = data.params_get.copy()
    current_params["t"] = track
    response = sender_stand_request.get_orders(current_params)
    assert response.status_code == 200
    print(response.status_code)
    print(current_params)

def test_order():
    positive_assert()

