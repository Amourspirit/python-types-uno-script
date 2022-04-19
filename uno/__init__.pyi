from typing import Any, Iterator, Tuple

def getComponentContext() -> Any:
    """Returns the UNO component context used to initialize the Python runtime."""
def getCurrentContext() -> Any:
    """Returns the current context.

    See http://udk.openoffice.org/common/man/concept/uno_contexts.html#current_context
    for an explanation on the current context concept.
    """
def setCurrentContext(newContext: Any) -> None:
    """Sets newContext as new UNO context.

    The newContext must implement the XCurrentContext interface. The
    implementation should handle the desired properties and delegate
    unknown properties to the old context. Ensure that the old one
    is reset when you leave your stack, see
    http://udk.openoffice.org/common/man/concept/uno_contexts.html#current_context
    """
def getConstantByName(constant: str) -> Any:
    """Looks up the value of an IDL constant by giving its explicit name."""
def getTypeByName(typeName: str) -> Any:
    """Returns a `uno.Type` instance of the type given by typeName.

    If the type does not exist, a `com.sun.star.uno.RuntimeException` is raised.
    """
def createUnoStruct(typeName: str, *args: any, **kwargs: any) -> Any:
    """Creates a UNO struct or exception given by typeName.

    Can be called with:

    1) No additional argument.
       In this case, you get a default constructed UNO structure.
       (e.g. `createUnoStruct("com.sun.star.uno.Exception")`)
    2) Exactly one additional argument that is an instance of typeName.
       In this case, a copy constructed instance of typeName is returned
       (e.g. `createUnoStruct("com.sun.star.uno.Exception" , e)`)
    3) As many additional arguments as the number of elements within typeName
       (e.g. `createUnoStruct("com.sun.star.uno.Exception", "foo error" , self)`).
    4) Keyword arguments to give values for each element of the struct by name.
    5) A mix of 3) and 4), such that each struct element is given a value exactly once,
       either by a positional argument or by a keyword argument.

    The additional and/or keyword arguments must match the type of each struct element,
    otherwise an exception is thrown.
    """
def getClass(typeName: str) -> Any:
    """Returns the class of a concrete UNO exception, struct, or interface."""

def isInterface(obj: object) -> bool:
    """Returns True, when obj is a class of a UNO interface."""

def generateUuid() -> ByteSequence:
    """Returns a 16 byte sequence containing a newly generated uuid or guid.

    For more information, see rtl/uuid.h.
    """
def systemPathToFileUrl(systemPath: str) -> str:
    """Returns a file URL for the given system path."""

def fileUrlToSystemPath(url: str) -> str:
    """Returns a system path.

    This path is determined by the system that the Python interpreter is running on.
    """
def absolutize(path:str, relativeUrl: str) -> str:
    """Returns an absolute file url from the given urls."""

class Enum:
    """Represents a UNO enum.

    Use an instance of this class to explicitly pass an enum to UNO.

    :param typeName: The name of the enum as a string.
    :param value: The actual value of this enum as a string.
    """
    def __init__(self, typeName: str, value: str) -> None: ...
    def __repr__(self) -> None: ...
    def __eq__(self, that: object) -> bool: ...
    def __ne__(self,other: object) -> bool: ...
    @property
    def tyepName(self) -> str: ...
    @property
    def value(self) -> Any: ...


class Type:
    """Represents a UNO type.

    Use an instance of this class to explicitly pass a type to UNO.

    :param typeName: Name of the UNO type
    :param typeClass: Python Enum of TypeClass, see com/sun/star/uno/TypeClass.idl
    
    See Also:
        https://api.libreoffice.org/docs/idl/ref/TypeClass_8idl_source.html
    """
    def __init__(self, typeName: str, typeClass: str) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, that: object) -> bool: ...
    def __ne__(self,other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def typeName(self) -> str: ...
    @property
    def typeClass(self) -> str: ...


class Bool(object):
    """Represents a UNO boolean.

    Use an instance of this class to explicitly pass a boolean to UNO.

    Note: This class is deprecated. Use Python's True and False directly instead.
    """
    def __new__(cls, value: Any) -> bool:...


class Char:
    """Represents a UNO char.

    Use an instance of this class to explicitly pass a char to UNO.

    For Python 3, this class only works with unicode (str) objects. Creating
    a Char instance with a bytes object or comparing a Char instance
    to a bytes object will raise an AssertionError.

    :param value: A Unicode string with length 1
    """
    def __init__(self, value: str) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, that: object) -> bool: ...
    def __ne__(self,other: object) -> bool: ...


class ByteSequence:
    """Represents a UNO ByteSequence value.

    Use an instance of this class to explicitly pass a byte sequence to UNO.

    :param value: A string or bytesequence
    """
    def __init__(self, value: bytes | ByteSequence) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, that: object) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    def __iter__(self) -> Iterator[int]: ...
    def __add__(self, b: bytes | ByteSequence) -> ByteSequence: ...
    @property
    def value(self) -> bytes: ...

class Any:
    """Represents a UNO Any value.

    Use only in connection with uno.invoke() to pass an explicit typed Any.
    """
    def __init__(self, type, value: str | Type) -> None: ...
    @property
    def value(self) -> Any: ...

def invoke(object, methodname: str, argTuple: Tuple[Any, ...]):
    """Use this function to pass exactly typed Anys to the callee (using uno.Any)."""
