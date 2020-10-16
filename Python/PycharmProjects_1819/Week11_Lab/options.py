"""Class Options for storing and retrieving options for a web server.

Author: Brianna Guest
Class: CSI-260-02
Assignment: Week 8 Lab
Due Date: March 8, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Options(dict):
    """Store and retrieve options for a Web Server."""

    def __init__(self, *args, **kwargs):
        """Initialize the dictionary of Server options."""
        super().__init__(kwargs)
        for arg in args:
            if type(arg) is str:
                self[arg] = True
            else:
                raise TypeError()

    def __getitem__(self, item):
        """Access options with square bracket notation.

        Accessing unspecified options returns the boolean False.
        """
        try:
            return super().__getitem__(item)
        except KeyError:
            return False

    def __setitem__(self, item, value):
        """Set and update options using square bracket notation."""
        super().__setitem__(item, value)

    def __getattr__(self, item):
        """Access options as attributes of the Options class."""
        return self[item]
        # Naomi from the SMART Space helped me understand how to use the method
        # in terms of syntax

    def __setattr__(self, item, value):
        """Set and update options using attribute notation."""
        self[item] = value
        # Naomi from the SMART Space helped me understand how to use the method
        # in terms of syntax

    def __delattr__(self, item):
        """Delete an attribute using square bracket/attribute notation."""
        del self[item]
        # Naomi from the SMART Space helped me understand how to use the method
        # in terms of syntax
