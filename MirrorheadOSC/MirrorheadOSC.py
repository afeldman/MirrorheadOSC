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

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset2")
    msg = msg.build()
    client.send(msg)
   
    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset3")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset4")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_preset5")
    msg = msg.build()
    client.send(msg)

    time.sleep(1)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_media4")
    msg = msg.build()
    client.send(msg)
