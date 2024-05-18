# flake8: noqa
def deep_update(base_dict, update_value):
    """This function update a dictionnary with the appropiate
        update_value even if the dictionnary is multi nested"""

    for key, value in update_value.items():
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            else:
                base_dict[key] = value
        else:
            base_dict[key] = value
    return base_dict
