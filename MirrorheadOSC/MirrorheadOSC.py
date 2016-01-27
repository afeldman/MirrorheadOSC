#!/usr/bin/env python3

## @package MirrorheadOSC
# 
#Mirrorhead Projectors uses a mirror to projekt the content onto the wall.
#Therfore a OpenSound Controll interface can e used. This python module 
#gives a controll to the mirrorhead projector such that the prensentation set can changed and modifyed
#over ethernet with UDP.
#
#To use this module use python 3.x.x and the pythonosc module in version 1.5
#
#@version 0.1.1
#@copyright Anton Feldmann Daimler AG 2016
##

## @license MIT
#
#  Copyright (c) 2016 anton.feldmann@daimler.com
#
# Hiermit wird unentgeltlich, jeder Person, die eine Kopie der Software
# und der zugehörigen Dokumentationen (die "Software") erhält, die
# Erlaubnis erteilt, uneingeschränkt zu benutzen, inklusive und ohne
# Ausnahme, dem Recht, sie zu verwenden, kopieren, ändern, fusionieren,
# verlegen, verbreiten, unter-lizenzieren und/oder zu verkaufen, und 
# Personen, die diese Software erhalten, diese Rechte zu geben, unter
# den folgenden Bedingungen:
#
# Der obige Urheberrechtsvermerk und dieser Erlaubnisvermerk sind in 
# alle Kopien oder Teilkopien der Software beizulegen.
#
# DIE SOFTWARE WIRD OHNE JEDE AUSDRÜCKLICHE ODER IMPLIZIERTE GARANTIE 
# BEREITGESTELLT, EINSCHLIESSLICH DER GARANTIE ZUR BENUTZUNG FÜR DEN
# VORGESEHENEN ODER EINEM BESTIMMTEN ZWECK SOWIE JEGLICHER 
# RECHTSVERLETZUNG, JEDOCH NICHT DARAUF BESCHRÄNKT. IN KEINEM FALL SIND
# DIE AUTOREN ODER COPYRIGHTINHABER FÜR JEGLICHEN SCHADEN ODER SONSTIGE
# ANSPRUCH HAFTBAR ZU MACHEN, OB INFOLGE DER ERFÜLLUNG VON EINEM 
# VERTRAG, EINEM DELIKT ODER ANDERS IM ZUSAMMENHANG MIT DER BENUTZUNG
# ODER SONSTIGE VERWENDUNG DER SOFTWARE ENTSTANDEN.
#
##

# import module
import time

# try to import the pythonosc module. if the module is not in the PYHTONPATH please reinstall the software
try:
    import logging
    import pythonosc as posc
except ImportError:
    logging.error("can not find pythonosc")
    logging.error("you need pythonosc version 1.5")

class mirrorhead():

    ## The constructor.
    #
    # the presentation can have different laver. The default layer is 1. The layer can be changed using 
    #
    # mirrorhead.layer = <number of layer
    #
    # the 
    #
    # @param ip the ip is set in the mirrorhead projector. The default adress is "192.168.0.20"
    # @param the port canbe shanded on the mirrorhead projector controller. The standard port is 7475
    #
    def __init__(self, ip="192.168.0.200", port=7475): 
        self.ip = ip
        self.port = port 
        self.layer = 1

        ##
        # connect the mirrorhead projector server
        ##
        try:
            self.client = posc.udp_client.UDPClient(ip, port)
        except Exception:
            logging.error(Exception.with_traceback)
            logging.error("Cannot start server")

    ##
    #toggel fullscreenmode  
    #
    def fullscreen(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_fullscreen").build()
        self.client.send(msg)
        time.sleep(sleeptime)
   
    ##
    #restart project
    #
    def restart(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_restart").build()
        self.client.send(msg)
        time.sleep(sleeptime)
   
    ##
    # Set Playback Play
    #
    def timelinestart(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_play").build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # Set playback stop
    #
    def timelinestop(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_stop").build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # set playback to pause
    #
    def timelinepause(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_timeline_pause").build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # select playlistitem
    #
    def playlist(self, item=1, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(item < 1), "under the last item"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_%s" % str(item)).build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # selsct next playlist item
    #
    def playlistnext(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_next").build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # selsct next playlist item
    #
    def playlistprevious(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_playlist_previous").build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # Load Presets $Y on layer $X
    #
    def item(self, preset=1, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(preset < 1), "befor the last preset. try one"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset%s" % (str(self.layer),str(preset))).build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # select next preset on on layer $X
    #
    def nextitem(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset_next" % str(self.layer)).build()
        self.client.send(msg)
        time.sleep(sleeptime)
       

    ##
    # select previous preset on on layer $X
    #
    def previousitem(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_preset_previous" % str(self.layer)).build()
        self.client.send(msg)
        time.sleep(sleeptime)

    ##
    # load media y on layer x
    #
    def media(self, media=1, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_media%s" % (str(self.layer),str(media)) ).build()
        self.client.send(msg)
        time.sleep(sleeptime)
      
    ##
    # select map m on layer y
    #
    def map(self, map=1, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_map%s" % (str(self.layer),str(map)) ).build()
        self.client.send(msg)
        time.sleep(sleeptime)   
     
    ##
    # select all maps on layer y
    #
    def mapall(self, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_map_all" % str(self.layer) ).build()
        self.client.send(msg)
        time.sleep(sleeptime)  
      
    ##
    # Same as /mdc_layer$X_map$M + sleep 1 sec + /mdc_layer$X_media$Y
    #
    def map(self, map=1, media=1, sleeptime=1):
        assert(sleeptime < 0), "less then zero seconds"
        assert(self.layer < 1), "smaller then the first layer"
        msg = posc.osc_message_builder.OscMessageBuilder(address = "/mdc_layer%s_mm_$s_%s" % (str(self.layer),str(map),str(media) ) ).build()
        self.client.send(msg)
        time.sleep(sleeptime)
