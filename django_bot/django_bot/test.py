from django.test import TestCase

from . import get_bot


class BotTextProcessTestCase(TestCase):

    def test_non_bot_message(self):
        message = 'Non format with / message'
        bot = get_bot(message)
        self.assertIsNone(bot)

    def test_bot_message_format(self):
        message = '/stock'
        bot = get_bot(message)
        self.assertTrue(bot)


class StockBotTestCase(TestCase):

    def test_bot_invalid_symbol_response(self):
        symbol = "NOT_SYMBOL"
        message = '/stock=' + symbol
        bot = get_bot(message)
        response = bot.get_response()
        self.assertEqual(response, "Sorry I didn't find any value for " + symbol)

    def test_bot_success_symbol_response(self):
        symbol = "AAPL.US"
        message = '/stock=' + symbol
        response = get_bot(message).get_response()
        self.assertTrue(symbol + " quote is" in response)
