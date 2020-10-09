import sys
from collections import namedtuple
from keyword import iskeyword


def create_unmutable(name: str, fields: str) -> None:
    """Creates an unmutable C like structure given the name of the 
    structure and it's fields. The fields are a string separated by
    a blank space, one word is one field on the structure.

    Arguments:
        name {str} -- [The name of the structure]
        fields {str} -- [A string containing the fields of the structure]

    Returns:
        None -- [Adds the new structure to the global variables of the workspace]
    """
    frame = sys._getframe(1)
    frame.f_globals[name] = namedtuple(name, fields)


def validateMutable(name: str, fields: list) -> None:
    """Raise error if the name of the struct or the fields are incorrect

    Arguments:
        name {str} -- [the name of the struct]
        fields {str} -- [the fields of the struct]

    Returns:
        None -- [description]
    """
    if not fields:
        raise ValueError('Mutable structures need at least one field')
    struct_variable_names = list(name) + fields
    for field_name in struct_variable_names:
        if iskeyword(field_name):
            raise ValueError(
                f'Name of struct and field names cannot be a keyword: {field_name}')
        if field_name[0].isdigit():
            raise ValueError(
                f'Name of struct or field names cannot start with a number {field_name}')
    seen_names = set()
    for field_name in fields:
        if field_name.startswith('_'):
            raise ValueError(
                f'Mutable field names cannot start with an underscore: {field_name}')
        if field_name in seen_names:
            raise ValueError(
                f'Duplicate field names in the struct {field_name}')
        seen_names.add(field_name)


def createStructClass(className: str, classAttr: str) -> str:
    """Creates a multiple line string which text is a new class
    declaration

    Arguments:
        className {str} -- [The name of the new class on the string]
        classAttr {str} -- [A string containing the names of properties on the class, must be
                            separated with a blank space between each propertie name]

    Returns:
        str -- [The class string which will be executed]
    """
    attributes = classAttr.split(" ")
    validateMutable(className, attributes)
    # Defining some raw process text to put on the class
    raw_init_body = map(lambda x: f'self.{x}={x}', attributes)
    raw_self_attributes = map(lambda x: f'self.{x}', attributes)
    raw_repr_text = map(lambda x: str(x)+'={}', attributes)
    raw_eqn_method = map(lambda x: f'self.{x}==other.{x}', attributes)
    # Making the class methods arguments and body
    initArguments = ', '.join(attributes)
    initBody = '; '.join(raw_init_body)
    eqnBody = ' and '.join(raw_eqn_method)
    repr_attr_body = ', '.join(raw_repr_text)
    repr_format_params = ','.join(raw_self_attributes)
    # The class string
    classStr = f"""
class {className}(object):
    def __init__(self,{initArguments}):
        {initBody}
    def __eq__(self,other):
        return isinstance(other, self.__class__) and {eqnBody}
    def __ne__(self,other):
        return not self == other
    def __repr__(self):
        return '{className}({repr_attr_body})'.format({repr_format_params})
    """
    return classStr


def create_mutable(name: str, fields: str) -> None:
    """Creates a new mutable C like structures, containing aliasing and
    changing of the values.

    Arguments:
        name {str} -- [The name of the mutable structure to create]
        fields {str} -- [The fields of the mutable structure, separated by a blank space]

    Returns:
        None -- [Adds the structure to the global variables]
    """
    class_definition = createStructClass(name, fields)
    exec(class_definition)
    frame = sys._getframe(1)
    frame.f_globals[name] = locals()[name]


# API for the course ...
crear = create_unmutable
mutable = create_mutable
