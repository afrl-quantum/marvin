# vim: et:sw=2:ts=2:nowrap
# -*- coding: utf-8 -*-

class NotATimingBoard(Exception):
  """
  This exception is raised when the requested board address does not appear to actually
  be a timing board.
  """
  pass
