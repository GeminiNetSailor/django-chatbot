from django.contrib.auth import get_user_model
from stock_market import today_price_for
from django_bot.models import Bot

User = get_user_model()


class StockBot:
    parameter = None

    def read_parameter(self, parameter):
        self.parameter = parameter

    def get_response(self):
        if self.parameter is None:
            return 'What Ticker are you looking for?'

        data = today_price_for(self.parameter)
        symbol = data['Symbol']
        value = data['Close']

        if value == 'N/D':
            return "Sorry I didn't find any value for {}".format(symbol)

        return '{0} quote is ${1:0,.2f} per share'.format(symbol, float(value))

    @property
    def user(self):
        bot_name = "stock-bot"
        try:
            bot = Bot.objects.get(name=bot_name)
            user = bot.user
        except Bot.DoesNotExist:
            username = 'stock-bot'
            email = username + '@mail.com'
            password = User.objects.make_random_password()
            user = User.objects.create_user(username, email, password)
            if user:
                Bot.objects.create(name=bot_name, user=user)

        return user
