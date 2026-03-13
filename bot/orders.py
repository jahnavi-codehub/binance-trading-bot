import logging

def market_order(client, symbol, side, quantity):

    order = client.create_order({
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity
    })

    logging.info(f"Market Order: {order}")

    return order


def limit_order(client, symbol, side, quantity, price):

    order = client.create_order({
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "timeInForce": "GTC"
    })

    logging.info(f"Limit Order: {order}")

    return order
