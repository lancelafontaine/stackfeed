from . import parsing
import argparse
import pytest

def test_parser_defaults():
    parse_obj = parsing.Parser()
    assert(parse_obj.question_type_default == 'noanswers')
    assert(parse_obj.seconds_default == 120)
    assert(type(parse_obj.parser) is argparse.ArgumentParser)
    assert(parse_obj.args == None)

def test_parser_args_defaults():
    parse_obj = parsing.Parser()
    parse_obj.parse_arguments()
    print(parse_obj.args)
    assert(parse_obj.args.question_type == 'noanswers')
    assert(parse_obj.args.seconds == 120)

def test_valid_question_types():
    parse_obj = parsing.Parser()
    parse_obj.args = parse_obj.parser.parse_args()
    parse_obj.args.seconds = 120

    parse_obj.args.question_type = 'noanswers'
    try:
        parse_obj.validate_arguments()
    except ValueError as e:
        pytest.fail(str(e))


    parse_obj.args.question_type = 'unanswered'
    try:
        parse_obj.validate_arguments()
    except ValueError as e:
        pytest.fail(str(e))

    parse_obj.args.question_type = 'all'
    try:
        parse_obj.validate_arguments()
    except ValueError as e:
        pytest.fail(str(e))

def test_invalid_question_types():
    parse_obj = parsing.Parser()
    parse_obj.args = parse_obj.parser.parse_args()
    parse_obj.args.seconds = 120

    parse_obj.args.question_type = 'klkjflkjfkkk'
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.question_type = 123
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.question_type = None
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.question_type = True
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.question_type = {}
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.question_type = []
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

def test_valid_seconds():
    parse_obj = parsing.Parser()
    parse_obj.args = parse_obj.parser.parse_args()
    parse_obj.args.question_type = 'noanswers'

    parse_obj.args.seconds = 120

    try:
        parse_obj.validate_arguments()
    except ValueError as e:
        pytest.fail(str(e))

    parse_obj.args.seconds = 999999999999999999
    try:
        parse_obj.validate_arguments()
    except ValueError as e:
        pytest.fail(str(e))

def test_invalid_seconds():
    parse_obj = parsing.Parser()
    parse_obj.args = parse_obj.parser.parse_args()
    parse_obj.args.question_type = 'noanswers'

    parse_obj.args.seconds = 1
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.seconds = 0
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.seconds = 'Test'
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.seconds = None
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.seconds = True
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

    parse_obj.args.seconds = {}
    with pytest.raises(ValueError) as e:
        parse_obj.validate_arguments()

