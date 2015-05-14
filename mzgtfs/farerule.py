"""GTFS Fare Rule."""
import datetime

import entity
import geom
import util
import widetime
import validation

class FareRule(entity.Entity):
  KEY = 'fare_id'
  REQUIRED = [
    'fare_id'
  ]
  OPTIONAL = [
    'route_id',
    'origin_id',
    'destination_id',
    'contains_id'
  ]
  
  def validate(self, validator=None):
    validator = super(FareRule, self).validate(validator)
    # Required
    with validator(self):
      assert self.get('fare_id'), "Required: fare_id"
    return validator
    
  def validate_feed(self, validator=None):
    validator = super(FareRule, self).validate_feed(validator)
    with validator(self):
      if self.get('route_id'):
        assert self._feed.route(self.get('route_id'))
    with validator(self):
      if self.get('origin_id'):
        pass
    with validator(self):
      if self.get('destination_id'):
        pass
    with validator(self):
      if self.get('contains_id'):
        pass
    return validator