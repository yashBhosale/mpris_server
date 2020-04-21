"""Implementation of org.mpris.MediaPlayer2 interface.

https://specifications.freedesktop.org/mpris-spec/2.2/Media_Player.html
"""


import logging

from .interface import Interface
from .base import INTERFACE as _INTERFACE, MIME_TYPES, NAME

logger = logging.getLogger(__name__)


class Root(Interface):
    """
    <node>
      <interface name="org.mpris.MediaPlayer2">
        <method name="Raise"/>
        <method name="Quit"/>
        <property name="CanQuit" type="b" access="read"/>
        <property name="CanRaise" type="b" access="read"/>
        <property name="Fullscreen" type="b" access="readwrite"/>
        <property name="CanSetFullscreen" type="b" access="read"/>
        <property name="HasTrackList" type="b" access="read"/>
        <property name="Identity" type="s" access="read"/>
        <property name="DesktopEntry" type="s" access="read"/>
        <property name="SupportedUriSchemes" type="as" access="read"/>
        <property name="SupportedMimeTypes" type="as" access="read"/>
      </interface>
    </node>
    """

    INTERFACE = _INTERFACE
    Identity = NAME

    CanSetFullscreen = False
    CanRaise = False
    HasTrackList = False
    CanQuit = False

    def Raise(self):
        logger.debug("%s.Raise called", self.INTERFACE)
        pass

    def Quit(self):
        logger.debug("%s.Quit called", self.INTERFACE)
        pass

    @property
    def Fullscreen(self):
        self.log_trace("Getting %s.Fullscreen", self.INTERFACE)
        return False

    @Fullscreen.setter
    def Fullscreen(self, value):
        logger.debug("Setting %s.Fullscreen to %s", self.INTERFACE, value)
        pass

    @property
    def DesktopEntry(self):
        self.log_trace("Getting %s.DesktopEntry", self.INTERFACE)
        return ""

    @property
    def SupportedUriSchemes(self):
        self.log_trace("Getting %s.SupportedUriSchemes", self.INTERFACE)
        return self.adapter.get_uri_schemes()

    @property
    def SupportedMimeTypes(self):
        self.log_trace("Getting %s.SupportedMimeTypes", self.INTERFACE)
        return self.adapter.get_mime_types()