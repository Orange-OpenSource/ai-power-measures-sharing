#################################
# AI Power Measure Sharing      #
# Creative Commons 4.0          #
# Orange/INNOV/DATA-AI          #
#################################
#!/usr/bin/python

from config.config import Config
from config.const import Const

LITERAL_TYPES_SET = set([ t.__name__ for t in [ str, int, float, bool, type(None) ] ])
DICT_OR_NULL_TYPES_SET = set([ dict.__name__, type(None).__name__ ])
NULL_TYPE_SET = set([ type(None).__name__ ])

class AmbiguousColumnException(Exception):

    def __init__(self, column:str) -> None:
        super().__init__('Ambiguous column '+column)

class InconsistentListException(Exception):

    def __init__(self, column:str) -> None:
        super().__init__('Inconsistent list value of column '+column)

class ObjectFlattener(object):

    separator:str = None

    def __init__(self, separator:str=Config.DEFAULT_COLUMN_FLATTENING_SEPARATOR) -> None:
        self.separator = separator

    def _flatten_node(self, n:dict, k:str, f:dict, prefix:str=''):
        if isinstance(n[k], dict):
            children_keys = n[k].keys()
            for c_k in children_keys:
                self._flatten_node(n=n[k], k=c_k, f=f, prefix=prefix+k+self.separator)
        elif isinstance(n[k], list):
            # check elements' type homogeneity
            if len(n[k]) == 0:
                return
            types_set = set([ type(elt).__name__ for elt in n[k] ])
            # possible lists are lists of dict or lists of literals
            if types_set.issubset(LITERAL_TYPES_SET) or types_set == NULL_TYPE_SET:
                # the list contains only literals or null values
                for i in range(len(n[k])):
                    f[prefix+k+str(i)] = n[k][i]
            elif types_set.issubset(DICT_OR_NULL_TYPES_SET):
                # the list contains only objects or None and calls for the presence of '$$key' in keys of non-null items
                presence = list(set([ Const.OBJECT_KEY_LABEL in list(elt.keys()) for elt in n[k] if elt is not None ]))
                if presence != [ True ]:
                    raise InconsistentListException(column=prefix+k)
                for o in n[k]:
                    if o is None:
                        continue
                    o_key = o[Const.OBJECT_KEY_LABEL]
                    del o[Const.OBJECT_KEY_LABEL] # it is necessary to remove the key once to avoid infinite loop
                    children_keys = o.keys()
                    for c_k in children_keys:
                        self._flatten_node(n=o, k=c_k, f=f, prefix=prefix+k+self.separator+o_key+self.separator)
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
