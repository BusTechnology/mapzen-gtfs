""" Test Feed Info"""
import unittest
import collections
import entities

class TestFeedInfo(unittest.TestCase):
  """Test Feed Info."""
  expect = collections.OrderedDict({
    'feed_publisher_url': 'http://google.com',
    'feed_publisher_name': 'Demo Transit Authority',
    'feed_id': 'DTA',
  })

  def test_name(self):
    feed_info = entities.FeedInfo(**self.expect)
    assert feed_info.name() == self.expect['feed_publisher_name']

  def test_id(self):
    feed_info = entities.FeedInfo(**self.expect)
    assert feed_info.id() == self.expect['feed_id']