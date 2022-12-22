"""General utilities used throughout the react sub-package"""

# Third-Party
from urllib.parse import urlparse

# This Project
from slobypy.react._react_types import UriType
from slobypy.errors.react_errors import URIError


def uri_checker(uri: UriType) -> str | bool:
    """
     ### Arguments
    - url: The url of the component

    ### Returns
    url: if the uri is valid
    error: if the uri is not valid
    """

    slobypy_result = urlparse(uri)

    if slobypy_result.path and slobypy_result.scheme is not True:
        return uri

    raise URIError("Not valid uri")
