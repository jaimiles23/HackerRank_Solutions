"""Collection of functions related to navigating directories
"""


def get_subdomain_dirname(subdomain: str) -> str:
    """Returns directory name for subdomain.

    Args:
        subdomain (str): Subdomain to get directory name

    Returns:
        str: Subdomain directory name
    """
    return subdomain.strip().lower().replace(' ', '_')