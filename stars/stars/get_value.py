
def get_val(collection, key, default = None):
    if key in list(collection.keys()):
        return collection[key]
    else:
        return default


