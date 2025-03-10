import json
from collections import defaultdict, Counter, ChainMap


def load_setting(env):
    with open(f'{env}.json') as file:
        settings = json.load(file)
    return settings


def load_profiles(*profiles):
    common_settings = load_setting('common')
    config = []
    for profile in profiles:
        config.append(load_setting(profile))
    config.append(common_settings)
    return ChainMap(config)



def recursive_chain(d1, d2):
    chain = ChainMap(d1, d2)
    for k,v in chain.items():
        if isinstance(v, dict) and k in d2:
            chain[k] = recursive_chain(d1[k], d2[k])
    return  chain





common_settings = load_setting('common')
dev_settings = load_setting('dev')

print("common", common_settings)
print("dev",dev_settings)



dev_profile = recursive_chain(dev_settings, common_settings)

print("dev profile", dev_profile['database'])







