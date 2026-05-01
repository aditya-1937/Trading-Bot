import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from app.config import API_KEY, API_SECRET, BASE_URL
from app.logger import logger


class BinanceClient:

    def _sign(self, params: dict):
        query_string = urlencode(params)
        signature = hmac.new(
            API_SECRET.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": API_KEY
        }

        response = requests.post(BASE_URL + endpoint, headers=headers, params=params)
        data = response.json()

        logger.info(f"Request: {params}")
        logger.info(f"Response: {data}")

        if response.status_code != 200:
            raise Exception(data)

        return data
