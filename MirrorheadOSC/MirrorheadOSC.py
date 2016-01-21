"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
    ip = "192.168.0.200"
    port = 7475

    client = udp_client.UDPClient(ip, port)

    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_presert1")
    msg = msg.build()
    client.send(msg)
   
    time.sleep(5)

#    msg = osc_message_builder.OscMessageBuilder(address = "/mdc_layer1_presert2")
#    msg = msg.build()
#    client.send(msg)
