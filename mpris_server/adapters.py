from typing import List, NamedTuple, Optional, Tuple
from abc import ABC
from enum import Enum

from .base import URI, MIME_TYPES, PlayState, DEFAULT_RATE, TimeInMicroseconds, \
  VolumeAsDecimal, RateAsDecimal, Metadata, DbusObj, PlaylistEntry, PlaylistValidity, DEFAULT_PLAYLIST_COUNT, \
  DEFAULT_ORDERINGS

from .events import EventAdapter


class Artist(NamedTuple):
  name: str = "Default Artist"


class Album(NamedTuple):
  name: str = "Default Album"
  artists: Tuple[Artist] = tuple()
  art_url: str = None


class Track(NamedTuple):
  track_id: DbusObj = '/default/1'
  name: str = "Default Track"
  track_no: int = None
  length: TimeInMicroseconds = 0
  uri: str = None
  artists: Tuple[Artist] = tuple()
  album: Optional[Album] = None
  art_url: str = None
  disc_no: int = None
  type: Optional[Enum] = None


class RootAdapter(ABC):
  def get_uri_schemes(self) -> List[str]:
    return URI

  def get_mime_types(self) -> List[str]:
    return MIME_TYPES

  def set_raise(self, val: bool):
    pass

  def quit(self):
    pass

  def get_fullscreen(self) -> bool:
    return False

  def set_fullscreen(self, val: bool):
    pass

  def get_desktop_entry(self) -> str:
    return ''


class PlayerAdapter(ABC):
  def metadata(self) -> Metadata:
    """
    Implement this function to supply your own MPRIS Metadata.

    If this function is implemented, metadata won't be built from get_current_track().

    See: https://www.freedesktop.org/wiki/Specifications/mpris-spec/metadata/
    :return:
    """
    pass

  def get_current_track(self) -> Track:
    """
    This function is an artifact of forking the base MPRIS library to a generic interface.
    The base library expected Track-like objects to build metadata.

    If metadata() is implemented, this function won't be used to build MPRIS metadata.
    :return:
    """
    pass

  def get_current_position(self) -> TimeInMicroseconds:
    pass

  def next(self):
    pass

  def previous(self):
    pass

  def pause(self):
    pass

  def resume(self):
    pass

  def stop(self):
    pass

  def play(self):
    pass

  def get_playstate(self) -> PlayState:
    pass

  def seek(self, time: TimeInMicroseconds):
    pass

  def open_uri(self, uri: str):
    pass

  def is_repeating(self) -> bool:
    pass

  def is_playlist(self) -> bool:
    pass

  def set_repeating(self, val: bool):
    pass

  def set_loop_status(self, val: str):
    pass

  def get_rate(self) -> RateAsDecimal:
    return DEFAULT_RATE

  def set_rate(self, val: RateAsDecimal):
    pass

  def get_shuffle(self) -> bool:
    pass

  def set_shuffle(self, val: bool):
    pass

  def get_art_url(self, track: int) -> str:
    pass

  def get_volume(self) -> VolumeAsDecimal:
    pass

  def set_volume(self, val: VolumeAsDecimal):
    pass

  def is_mute(self) -> bool:
    pass

  def set_mute(self, val: bool):
    pass

  def can_go_next(self) -> bool:
    pass

  def can_go_previous(self) -> bool:
    pass

  def can_play(self) -> bool:
    pass

  def can_pause(self) -> bool:
    pass

  def can_seek(self) -> bool:
    pass

  def can_control(self) -> bool:
    pass

  def get_stream_title(self) -> str:
    pass

  def get_previous_track(self) -> Track:
    pass

  def get_next_track(self) -> Track:
    pass


class PlaylistAdapter(ABC):
  def activate_playlist(self, id: DbusObj):
    pass

  def get_playlists(self, index: int, max_count: int, order: str, reverse: bool) -> List[PlaylistEntry]:
    pass

  def get_playlist_count(self) -> int:
    return DEFAULT_PLAYLIST_COUNT

  def get_orderings(self) -> List[str]:
    return DEFAULT_ORDERINGS

  def get_active_playlist(self) -> Tuple[PlaylistValidity, PlaylistEntry]:
    pass


class TrackListAdapter(ABC):
  def get_tracks_metadata(self, track_ids: List[DbusObj]) -> Metadata:
    pass

  def add_track(self, uri: str, after_track: DbusObj, set_as_current: bool):
    pass

  def remove_track(self, track_id: DbusObj):
    pass

  def go_to(self, track_id: DbusObj):
    pass

  def get_tracks(self) -> List[DbusObj]:
    pass

  def can_edit_track(self) -> bool:
    pass


class MprisAdapter(RootAdapter, PlayerAdapter, PlaylistAdapter, TrackListAdapter):
  """
  MRPRIS interface for your application.

  The MPRIS implementation is supplied with information
  returned from this adapter.
  """

  def __init__(self, name: str = 'MprisAdapter'):
    self.name = name
