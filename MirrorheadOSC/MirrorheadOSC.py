#!/usr/bin/env python3

## @package MirrorheadOSC
#  Documentation for this module.
#
#  More details.

import time
import logging

try:
    import pythonosc as posc
except ImportError:
    logging.error("can not find pythonosc")
    logging.error("you need pythonosc version 1.5")

class Mirrorhead():

    def __init__(self, ip="192.168.0.200", port=7475): 
        self.ip = ip
        self.port = port 
        self.layer = 1
        try:
            self.client = posc.udp_client.UDPClient(ip, port)
        except Exception:
            logging.error(Exception.with_traceback)
            logging.error("Cannot start server")

#
#toggel fullscreenmode  
#
    def fullscreen(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_fullscreen").build()
        self.client.send(msg)
        time.sleep(sleeptime)
   
    """
    restart project
    """
    def restart(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_restart").build()
        client.send(msg)
        time.sleep(sleeptime)
   
    ##
    # Set Playback Play
    #
    def timelinestart(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_play").build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # Set playback stop
    #
    def timelinestop(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_stop").build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # set playback to pause
    #
    def timelinepause(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_pause").build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # select playlistitem
    #
    def playlist(self, item=1, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_%s" % str(item)).build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # selsct next playlist item
    #
    def playlistnext(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_next").build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # selsct next playlist item
    #
    def playlistprevious(self, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_previous").build()
        client.send(msg)
        time.sleep(sleeptime)

     ##
     # Load Presets $Y on layer $X
     #
     def item(self, preset=1, sleeptime=1):
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset%s" % (str(self.layer),str(preset))).build()
        client.send(msg)
        time.sleep(sleeptime)

    ##
    # select next preset on on layer $X
    #
    def nextitem(self, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset_next" % str(self.layer)).build()
       client.send(msg)
       time.sleep(sleeptime)
       

    ##
    # select previous preset on on layer $X
    #
    def previousitem(self, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset_previous" % str(self.layer)).build()
       client.send(msg)
       time.sleep(sleeptime)

    ##
    # load media y on layer x
    #
    def media(self, media=1, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_media%s" % (str(self.layer),str(media)) ).build()
       client.send(msg)
       time.sleep(sleeptime)
      
    ##
    # select map m on layer y
    #
    def map(self, map=1, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_map%s" % (str(self.layer),str(map)) ).build()
       client.send(msg)
       time.sleep(sleeptime)   
     
    ##
    # select all maps on layer y
    #
    def mapall(self, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_map_all" % str(self.layer) ).build()
       client.send(msg)
       time.sleep(sleeptime)  
      
    ##
    # Same as /mdc_layer$X_map$M + sleep 1 sec + /mdc_layer$X_media$Y
    #
    def map(self, map=1, media=1, sleeptime=1):
       msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_mm_$s_%s" % (str(self.layer),str(map),str(media) ) ).build()
       client.send(msg)
       time.sleep(sleeptime)  
       

    
