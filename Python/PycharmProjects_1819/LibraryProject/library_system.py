"""The classes to implement the Library Collection system.

Author: Brianna Guest
Class: CSI-260-01
Assignment: Library Project
Due Date: 2/27/2019 11:59 PM

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
import pickle
import abc


class LibraryItem(abc.ABC):
    """Base class for all items stored in a library catalog.

    Provides a simple LibraryItem with only a few attributes.
    """

    def __init__(self, name, isbn, tag_list=[]):
        """Initialize a LibraryItem.

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        """
        self.name = name
        self.isbn = isbn
        self.type = 'Generic'  # This is the type of item being stored
        self.tag_list = tag_list

    @abc.abstractmethod
    def match(self, filter_text):
        """Return whether the item is a match for the filter_text.

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match
        or partial match.

        match needs to be redefined for any subclasses. Please see the
        note/notebook case study from Chapter 2 as an example of how match
        is designed to work.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            True if filter_text.lower in self.tag_list else False

    @abc.abstractmethod
    def __str__(self):
        """Return a well formatted string representation of the item.

        All instance variables are included.
        """
        return f'{self.name} {self.isbn} {self.type}'

    def to_short_string(self):
        """Return a short string representation of the item.

        String contains only the name of the item and the type of the item
        """
        return f'{self.name} - {self.isbn}'


class BookRecord(LibraryItem):
    """Provides a Book Record for a Library Item."""

    def __init__(self, name, isbn, genre, author, tag_list=[]):
        """Initialize a Book Record.

        :param name: (string) Name of book
        :param isbn: (string) ISBN number for the book
        :param genre: (string) Genre of the book
        :param author: (string) The author of the book
        """
        super().__init__(name, isbn)
        self.genre = genre
        self.author = author
        self.type = 'Book'
        self.tag_list = tag_list

    def match(self, filter_text):
        """Return whether the item is a match for the filter_text.

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match
        or partial match.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() in self.author.lower() or \
            filter_text.lower() == self.isbn.lower or \
            filter_text.lower() in self.genre.lower() or \
            filter_text.lower() in self.type.lower() or \
            True if filter_text.lower in self.tag_list else False

    def __str__(self):
        """Return a well formatted string representation of the book.

        All instance variables are included.
        """
        return \
            f'{super().__str__()} \nAuthor: {self.author} ' \
            f'\nGenre: {self.genre} \nCategory Tags: ' \
            f'\n{self.tag_list}'


class MusicAlbumRecord(LibraryItem):
    """Provides a eBook Record for a Library Item."""

    def __init__(self, name, isbn, genre, artist, label, tag_list=[]):
        """Initialize an eBook Record.

        :param name: (string) Name of eBook
        :param isbn: (string) ISBN number for the eBook
        :param genre: (string) Genre of the eBook
        :param artist: (string) The artist of the music album
        :param label: (string) The record label of the music album
        """
        super().__init__(name, isbn)
        self.genre = genre
        self.artist = artist
        self.label = label
        self.type = 'Music Album'
        self.tag_list = tag_list

    def match(self, filter_text):
        """Return whether the item is a match for the filter_text.

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match
        or partial match.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() in self.artist.lower() or \
            filter_text.lower() in self.label.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in self.genre.lower() or \
            filter_text.lower() in self.type.lower() or \
            True if filter_text.lower in self.tag_list else False

    def __str__(self):
        """Return a well formatted string representation of the eBook.

        All instance variables are included.
        """
        return \
            f'{super().__str__()} \nArtist: {self.artist} ' \
            f'\nRecord Label: {self.label} \nGenre: {self.genre} ' \
            f'\nCategory Tags: \n{self.tag_list}'


class DVDRecord(LibraryItem):
    """Provides a DVD Record for a Library Item."""

    def __init__(self, name, isbn, genre, company, tag_list=[]):
        """Initialize a DVD Record.

        :param name: (string) Name of DVD
        :param genre: (string) Genre of the DVD
        :param company: (string) The distributing company of the DVD
        """
        super().__init__(name, isbn)
        self.genre = genre
        self.company = company
        self.type = 'DVD'
        self.tag_list = tag_list

    def match(self, filter_text):
        """Return whether the item is a match for the filter_text.

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match
        or partial match.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in self.company.lower() or \
            filter_text.lower() in self.genre.lower() or \
            filter_text.lower() in self.type.lower() or \
            True if filter_text.lower in self.tag_list else False

    def __str__(self):
        """Return a well formatted string representation of the DVD.

        All instance variables are included.
        """
        return \
            f'{super().__str__()} \nDistributor: {self.company} ' \
            f'\nGenre: {self.genre} \nCategory Tags: ' \
            f'\n{self.tag_list}'


class Catalog:
    """Provides a 'private' list for holding a collection of LibraryItems."""

    def __init__(self, name):
        """Initialize the name of catalog and the empty 'private' list.

        :param name: the name of the 'private' list
        """
        self.name = name
        self._collection = []

    def add_list(self, collection):
        """Give the ability to add a list of LibraryItems."""
        for item in collection:
            self._collection.append(item)

    def remove_list(self, item):
        """Give the ability to remove a list of LibraryItems."""
        try:
            self._collection.remove(item)
        except IndexError as e:
            print("The item does not exist")
            print(e)

    def search(self, filter_text):
        """Give the ability to search for items.

        Including the ability to filter the search by the type of item.
        """
        return [search for search in
                self._collection if search.match(filter_text)]

    def save_catalog(self, collection):
        """Save the [_catalog] list to a pickle file.

        :param collection: The collection that is being saved
        """
        pickle.dump(collection, open("save_file.p", "wb"))

    def load_catalog(self):
        """Load the [_catalog} list to the system."""
        try:
            self._collection = pickle.load(open("save_file.p", 'rb'))
        except FileNotFoundError:
            self._collection = []


class CategoryTag:
    """Provides a 'private' list for holding category tags."""

    _category_tags = []

    def __init__(self, name):
        """Initialize a Category Tag.

        :param name: Name of Category Tag
        """
        self.name = name
        CategoryTag._category_tags.append(self.name)

    def __str__(self):
        """Return a well formatted string representation of a category tag."""
        return f'{self.name}'

    @classmethod
    def all_category_tags(cls):
        """Return a string representation of all category tags."""
        print("All Category Tags:")
        for tag in cls._category_tags:
            print(f' - {tag}')
