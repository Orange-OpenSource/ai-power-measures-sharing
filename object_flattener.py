#################################
# CO2 Reporting                 #
# (c) 2023 Orange/INNOV/DATA-AI #
#################################
#!/usr/bin/python

class AmbiguousColumnException(Exception):

    def __init__(self, column:str) -> None:
        super().__init__('Ambiguous column '+column)

class ObjectFlattener(object):

    separator:str = None

    def __init__(self, separator:str='.') -> None:
        self.separator = separator

    def _flatten_node(self, n:dict, k:str, f:dict, prefix:str=''):
        if isinstance(n[k], dict):
            children_keys = n[k].keys()
            for c_k in children_keys:
                self._flatten_node(n=n[k], k=c_k, f=f, prefix=prefix+k+self.separator)
        else:
            flat_key = prefix+k
            if flat_key in list(f.keys()):
                raise AmbiguousColumnException(column=flat_key)
            f[prefix+k] = n[k]

    def flatten(self, o:dict) -> dict:
        if o is None or o == {}:
            return o
        
        # output object
        f = {}

        keys = o.keys()
        for k in keys:
            self._flatten_node(o, k, f)

        return f



if __name__ == '__main__':
    of = ObjectFlattener(separator='_')

    print('Test OK')
    print(str(of.flatten({
        'prop': 'value',
        'figure': 1,
        'empty': {},
        'nested': {
            'sub': 5,
            'renested': {
                'grandson': 'Hello World!',
                'null': None
            }
        }
    })))

    print('Test KO')
    print(str(of.flatten({
        'prop': 'value',
        'figure': 1,
        'empty': {},
        'nested': {
            'sub': 5,
            'renested': {
                'grandson': 'Hello World!',
                'null': None
            }
        },
        'nested_renested_grandson': 'ambiguous'
    })))
