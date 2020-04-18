import datetime

class Log:
    @staticmethod
    def info(message):
        Log.write_to_log('info', message)

    @staticmethod
    def debug(message):
        Log.write_to_log('debug', message)

    @staticmethod
    def error(message):
        Log.write_to_log('error', message)

    @staticmethod
    def write_to_log(log_type, message):
        if type(message) is list:
            message = "\n".join(str(val) for val in message)

        message = str(message)

        with open("run.log", "a") as log_file:
            log_type = log_type.upper()
            log_file.write("[" + datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S") + "] " + log_type + " - " + message + "\n")