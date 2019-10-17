# bw_migrations

Migration data and utilities for Brightway IO and LCA in general

[![Build Status](https://travis-ci.org/brightway-lca/bw_migrations.svg?branch=master)](https://travis-ci.org/brightway-lca/bw_migrations) [![Coverage Status](https://coveralls.io/repos/github/brightway-lca/bw_migrations/badge.svg?branch=master)](https://coveralls.io/github/brightway-lca/bw_migrations?branch=master) [![Build status](https://ci.appveyor.com/api/projects/status/lk0tbo21v2irm48x?svg=true)](https://ci.appveyor.com/project/cmutel/bw-migrations)

Most databases use their own nomenclature for classification systems, units, etc. These systems need to be matched when linking from one database to another. Often, a simple mapping is suitable, and tools like [correspondentia](https://github.com/BONSAMURAIS/correspondentia) are a good fit. However, sometimes one needs more complexity, e.g. change field X to Y, but only if field A has value B. When ecoinvent released version 3, they changed their unit of mesaure for water from kilograms to cubic meters. ``bw_migrations`` provides tools for this more complicated transformations, and is built around the following data format:

    {
        # The fields on which to filter
        'fields': ['name', 'category', 'unit'],
        'data': [
            (
                # First element is input data in the order of `fields` above
                ('Water', 'air', 'kilogram'),
                # Second element is new values to substitute when all fields match
                {
                    'unit': 'cubic meter',
                    '__multiplier__': 0.001
                }
            )
        ]
    }

And is implemented with the following pseudo-code:

    for element in input_data:
        for original, new in migration['data']:
            if all(element[field] == original[field] for field in migration['fields']):
                element.update(dict(zip(migration['fields'], new)))

The actual code is a bit more complex, as `bw_migrations` can also do rescaling of probability distributions and disaggregation migrations (splitting one object into several outputs).
