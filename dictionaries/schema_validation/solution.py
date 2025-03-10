template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}

# That should return this:
# * `validate(john, template) --> True, ''`
# * `validate(eric, template) --> False, 'mismatched keys: bio.birthplace.city'`
# * `validate(michael, template) --> False, 'bad type: bio.dob.month'`



def validate(data, template, path=''):
    state = True
    error = ''
    for key, _type in template.items():
        if isinstance(_type, dict):
            path += "."+key
            state, error = validate(data[key], template[key], path)
            if not state:
                break
        else:
            if not key in data:
                return False, f"Key mismatch: {path}.{key}"

            if type(data[key]) != _type:
                return False, f"Type mismatch: {path}.{key}"

    return state, error

#print(validate(john, template))

#print(validate(eric, template))

print(validate(michael, template))