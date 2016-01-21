import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
    ip = "192.168.0.200"
    port = 7475

    try:
        client = udp_client.UDPClient(ip, port)
    except:
        print("cannot open client")

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset1")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset19")
    msg = msg.build()
    client.send(msg)
   
    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset13")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset14")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset15")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset16")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset17")
    msg = msg.build()
    client.send(msg)

    time.sleep(10)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset18")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset20")
    msg = msg.build()
    client.send(msg)