import argparse

class Parser:
    def __init__(self):
        self.question_type_default = 'noanswers'
        self.seconds_default = 120
        program_description = 'A Python command-line tool for listing StackOverflow questions in real-time based on tags.'
        self.parser = argparse.ArgumentParser(description=program_description)

        self.args = None

    def parse_question_type(self):
        question_type_help = 'Specifies the type of question to output. Possible values are \'noanswers\', \'unanswered\' \
                or \'all\'. Default is {}. Visit https://api.stackexchange.com/docs for more information.'.format(self.question_type_default)
        self.parser.add_argument('-q', '--question_type', default='noanswers', help=question_type_help)

    def parse_seconds(self):
        seconds_help= 'Specifies output frequency in seconds. Minimum and default value is {} in order to prevent \
                rate-limiting and respect StackExchange\'s service.'.format(self.seconds_default)
        self.parser.add_argument('-s', '--seconds', type=int, default=120, help=seconds_help)

    def validate_arguments(self):
        a = self.args
        if type(a.question_type) is not str or \
            (a.question_type != 'noanswers' and \
            a.question_type != 'unanswered' and \
            a.question_type != 'all'):
            raise ValueError("QUESTION_TYPE argument is invalid. See --help for more information")

        if type(a.seconds) is not int or a.seconds < self.seconds_default:
            raise ValueError("SECONDS argument is invalid. See --help for more information")

    def parse_arguments(self):
        self.parse_question_type()
        self.parse_seconds()

        self.args = self.parser.parse_args()
        self.validate_arguments()

        return self.args

