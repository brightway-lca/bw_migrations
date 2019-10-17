from bw_migrations.strategies import modify_object, migrate_data


def test_modify_object():
    given = {"a": 5, "b": "foo"}
    dct = {"b": "zany", "c": "wild"}
    expected = {"a": 5, "b": "zany", "c": "wild"}
    assert modify_object(given, dct) == expected
    assert given == expected


def test_modify_object_with_disaggregation():
    given = {"a": 5, "b": "foo", "amount": 11}
    dct = {"b": "zany", "c": "wild", "__disaggregation__": 5}
    expected = {"a": 5, "b": "zany", "c": "wild", "amount": 55}
    assert modify_object(given, dct) == expected
    assert given == expected


def test_modify_object_with_multiplier():
    given = {"a": 5, "b": "foo", "amount": 11}
    dct = {"b": "zany", "c": "wild", "__multiplier__": 5}
    expected = {"a": 5, "b": "zany", "c": "wild", "amount": 55}
    assert modify_object(given, dct) == expected
    assert given == expected


def test_modify_object_with_both():
    given = {"a": 5, "b": "foo", "amount": 11}
    dct = {"b": "zany", "c": "wild", "__multiplier__": 5, "__disaggregation__": 0.1}
    expected = {"a": 5, "b": "zany", "c": "wild", "amount": 5.5}
    assert modify_object(given, dct) == expected
    assert given == expected


def test_migrate_data():
    migration = {
        'fields': ['a', 'b'],
        'data': [(
            ('green', 'brown'),
            {
                'a': 'blue',
                'another': 'value'
            }
        )]
    }
    given = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "green", "b": "brown"}]
    expected = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "blue", "b": "brown", "another": "value"}]
    assert list(migrate_data(given, migration)) == expected


def test_migrate_data_disaggregation():
    migration = {
        'fields': ['a', 'b'],
        'data': [(
            ('green', 'brown'),
            [{
                'a': 'blue',
                'another': 'value',
                '__multiplier__': 0.5,
                '__disaggregation__': 0.3,
            }, {
                'a': 'red',
                '__disaggregation__': 0.7,
            }]
        )]
    }
    given = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "green", "b": "brown", "amount": 10}]
    expected = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "blue", "b": "brown", "another": "value", "amount": 1.5}, {"a": "red", "b": "brown", "amount": 7}]
    assert list(migrate_data(given, migration)) == expected


def test_migrate_data_multiplier():
    migration = {
        'fields': ['a', 'b'],
        'data': [(
            ('green', 'brown'),
            {
                'a': 'blue',
                'another': 'value',
                '__multiplier__': 0.5
            }
        )]
    }
    given = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "green", "b": "brown", "amount": 4}]
    expected = [{"a": 5, "b": "foo"}, {"a": "green", "b": "foo"}, {"a": "blue", "b": "brown", "another": "value", "amount": 2}]
    assert list(migrate_data(given, migration)) == expected
