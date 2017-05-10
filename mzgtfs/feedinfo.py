"""GTFS Feed Info entity."""
import entity
import geom
import util
import validation

class FeedInfo(entity.Entity):
    """GTFS Feed Info entity."""
    ENTITY_TYPE = 'o'
    KEY = 'feed_publisher_name'
    REQUIRED = [
        'feed_publisher_name',
        'feed_publisher_url',
        'feed_lang'
    ]
    OPTIONAL = [
        'feed_start_date',
        'feed_end_date',
        'feed_version',
        #an OpenTripPlanner construct, not part of the GTFS spec
        'feed_id'
    ]
    def name(self):
        return self.get('feed_publisher_name')

    def id(self):
        return self.get('feed_id')

    ##### Validation #####

    def validate(self, validator=None):
        validator = super(FeedInfo, self).validate(validator)
        # Required
        with validator(self):
            assert self.get('feed_publisher_name'), \
                "Required: feed_publisher_name"

        with validator(self):
            assert self.get('feed_publisher_url'), "Required: feed_publisher_url"
            assert validation.valid_url(self.get('feed_publisher_url')), \
                "Invalid agency_url"

        with validator(self):
            assert validation.valid_language(self.get('feed_lang')), \
            "Invalid language"

        with validator(self):
            if self.get('feed_start_date'):
                assert validation.valid_language(self.get('feed_start_date')), \
                "Invalid start date"

        with validator(self):
            if self.get('feed_end_date'):
                assert validation.valid_language(self.get('feed_end_date')), \
                "Invalid end date"
