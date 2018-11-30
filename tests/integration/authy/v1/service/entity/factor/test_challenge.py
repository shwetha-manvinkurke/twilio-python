# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ChallengeTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities(identity="identity") \
                                .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .challenges.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Factors/YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Challenges',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "pending",
                "responded_reason": "none",
                "details": "Hi! Mr. John Doe, would you like to sign up?",
                "hidden_details": "Hidden details about the sign up",
                "type": "sms",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges.create()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities(identity="identity") \
                                .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .challenges(sid="sid").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Factors/YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Challenges/sid',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges(sid="sid").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities(identity="identity") \
                                .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .challenges(sid="sid").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Factors/YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Challenges/sid',
        ))

    def test_fetch_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "pending",
                "responded_reason": "none",
                "details": "details",
                "hidden_details": "hidden_details",
                "type": "sms",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges(sid="sid").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_latest_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "pending",
                "responded_reason": "none",
                "details": "details",
                "hidden_details": "hidden_details",
                "type": "sms",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges(sid="sid").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .entities(identity="identity") \
                                .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .challenges(sid="sid").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://authy.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities/identity/Factors/YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Challenges/sid',
        ))

    def test_verify_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "approved",
                "responded_reason": "none",
                "details": "Hi! Mr. John Doe, would you like to sign up?",
                "hidden_details": "Hidden details about the sign up",
                "type": "sms",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges(sid="sid").update()

        self.assertIsNotNone(actual)

    def test_verify_latest_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "entity_sid": "YEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "identity": "ff483d1ff591898a9942916050d2ca3f",
                "factor_sid": "YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "date_responded": "2015-07-30T20:00:00Z",
                "expiration_date": "2015-07-30T20:00:00Z",
                "status": "approved",
                "responded_reason": "none",
                "details": "Hi! Mr. John Doe, would you like to sign up?",
                "hidden_details": "Hidden details about the sign up",
                "type": "sms",
                "url": "https://authy.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities/ff483d1ff591898a9942916050d2ca3f/Factors/YFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Challenges/YCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.authy.v1.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .entities(identity="identity") \
                                     .factors(sid="YFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .challenges(sid="sid").update()

        self.assertIsNotNone(actual)
