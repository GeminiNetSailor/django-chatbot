def get_bot(message):
    if is_command(message) is False:
        return None

    # remove command slash
    message = message[1:]

    command = message
    parameter = None
    if "=" in message:
        command = message.split("=")[0]
        parameter = message.split("=")[1]

    bot = get_bot_type(command)
    if parameter:
        bot.read_parameter(parameter)

    return bot


def get_bot_type(command):
    if command == 'stock':
        from .bots import StockBot
        return StockBot()
    else:
        return None


def is_command(message):
    first_character = message[0]
    if first_character != '/':
        return False
    return True
