"""The user interface of the Library Collection System.

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
from library_system \
    import BookRecord, MusicAlbumRecord, DVDRecord, \
    Catalog, CategoryTag
import sys
import csv

# main menu of user interface
menu = "\nLibrary Catalog Menu\n" \
       "1. Search catalog" \
       "\n2. Print the entire catalog" \
       "\n3. Add item to catalog" \
       "\n4. Remove item from catalog" \
       "\n5. Print all Category Tags" \
       "\n6. Open Catalog from file" \
       "\n7. Save Catalog to file" \
       "\n8. Export to .csv file" \
       "\n9. Exit System" \
       "\n"

# menu of Add item option
add_menu = "\nType of Library Items\n" \
           "1. Book" \
           "\n2. Music Album" \
           "\n3. DVD" \
           "\n"


def main():
    """User Interface of the Library Collection system.

    Provides the user interface and initialization of the Catalog Class,
    thus the catalog itself.
    """
    name = input("Enter the name of the Catalog: ")
    catalog = Catalog(name)
    while True:
        print(menu)
        user_input = input("Choose an option: ")

        if user_input == '1':
            filter_text = input("Search for: ")
            catalog.search(filter_text)

        elif user_input == '2':
            try:
                for item in catalog._collection:
                    print(f'{item}\n')
            except TypeError:
                print(catalog._collection)

        elif user_input == '3':
            collection = []

            print(add_menu)
            user_input = input("Choose an option: ")

            if user_input == '1':
                tag_list = []
                name = input("Enter Name: ")
                isbn = int(input("Enter ISBN Number: "))
                genre = input("Enter Genre: ")
                author = input("Enter Author: ")
                while True:
                    user_input = input("Optionally - "
                                       "Enter Category Tags"
                                       "(Press Enter when finish): ")
                    if user_input != '':
                        tag_list.append(CategoryTag(user_input).__str__())
                    else:
                        break

                # fix from previous submission (forgot to implement)
                collection.\
                    append(BookRecord(
                        name, isbn, genre, author,
                        tag_list).__str__())
                catalog.add_list(collection)
            elif user_input == '2':
                tag_list = []
                name = input("Enter Name: ")
                isbn = int(input("Enter ISBN Number: "))
                genre = input("Enter Genre: ")
                artist = input("Enter Artist: ")
                label = input("Enter the Record Label of the Music Album: ")
                while True:
                    user_input = input("Optionally - "
                                       "Enter Category Tags"
                                       "(Press Enter when finish): ")
                    if user_input != '':
                        tag_list.append(CategoryTag(user_input).__str__())
                    else:
                        break

                # fix from previous submission (forgot to implement)
                collection.append(MusicAlbumRecord(
                        name, isbn, genre, artist, label,
                        tag_list=tag_list).__str__())
                catalog.add_list(collection)
            elif user_input == '3':
                tag_list = []
                name = input("Enter Name: ")
                isbn = int(input("Enter ISBN Number: "))
                company = input("Enter Company: ")
                genre = input("Enter Genre: ")
                while True:
                    user_input = input("Optionally - "
                                       "Enter Category Tags"
                                       "(Press Enter when finish): ")
                    if user_input != '':
                        tag_list.append(CategoryTag(user_input).__str__())
                    else:
                        break

                # fix from previous submission (forgot to implement)
                collection.\
                    append(DVDRecord(name, isbn, company, genre,
                                     tag_list).__str__())
                catalog.add_list(collection)

        elif user_input == '4':
            remove_list = []
            while True:
                user_input = \
                    input("Enter the items to remove(Press Enter when done): ")
                if user_input != '':
                    remove_list.append(user_input)
                else:
                    break
            for item in remove_list:
                catalog.remove_list(item)

        elif user_input == '5':
            print(CategoryTag.all_category_tags())

        elif user_input == '6':
            catalog.load_catalog()

        elif user_input == '7':
            catalog.save_catalog(catalog)

        elif user_input == '8':
            with open('database.csv', 'a') as write_file:
                writer = csv.writer(write_file)
                writer.writerow(catalog._collection)
                print("Export Complete")
        # I wasn't able to get the import function to work so I decided not to include it

        elif user_input == '9':
            sys.exit()


if __name__ == "__main__":
    main()
