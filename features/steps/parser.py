import os
from python_parser.parser import Parser
from behave import given, when, then


THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))


@given('Some valid json')
def step_impl(context):
    # Look in the right place for the example file
    context.filename = os.path.abspath(os.path.join(THIS_FILE_DIR, '..', '..', 'homer.json'))


@when('I parse the data')
def step_impl(context):
    context.data = Parser().parse_file(context.filename)


@then('the name should be {name}')
def step_impl(context, name):
    assert context.data.name == name


@then('the children should be')
def step_impl(context, name):
    for expected, actual in zip(context.table, context.data.children):
        assert expected['Name'] == actual.name
        assert expected['Age'] == actual.age


@then('the postcode should be {postcode}')
def step_impl(context, postcode):
    assert context.data.address.postcode == postcode


@then('the postal area should be {area}')
def step_impl(context, area):
    assert context.data.address.postal_area == area


@then('the house number should be {house_number}')
def step_impl(context, house_number):
    assert context.data.address.building_name_or_number == house_number


@then('the street should be {street}')
def step_impl(context, street):
    assert context.data.address.street == street


@then('the town should be {town}')
def step_impl(context, town):
    assert context.data.address.city == town


@then('the year of birth should be {year}')
def step_impl(context, year):
    assert context.data.dob.year == year


@then('the friends should be')
def step_impl(context):
    for expected, actual in zip(context.table, context.data.friends):
        assert expected == actual.name


@then('the brand preferences should be')
def step_impl(context):
    for expected, actual in zip(context.table, context.data.brand_preferences):
        assert expected['Name'] == actual.name
        assert expected['Type'] == actual.type


@then('the family should be')
def step_impl(context):
    for expected, actual in zip(context.table, context.data.family):
        assert expected['Name'] == actual.name
        assert expected['Relationship'] == actual.relationship


@then('the average score should be {score}')
def step_impl(context, score):
    assert context.data.performance.average == score
