class CustomDict(dict):
    def get(self, key):
        return super().get(key, 0)


new_dict = CustomDict()
new_dict['f'] = 'first'
new_dict['s'] = 'second'

print(new_dict.get('f'))
print(new_dict.get('s'))
print(new_dict.get('t'))