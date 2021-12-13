#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# TFang, 2021-Dec-11, added code to work with modules and completed todos for Assignment 09
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """Function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None

        """
        cdId, title, artist = CDInfo # unpack variables from 1st argument
        try: # function to process IO.ScreenIO.get_CD_info from user and create new CD object
            cdId = int(cdId)
        except ValueError: # exception trap
            print('ID must be a number!')
        raise Exception('ID must be a number!')
        row = DC.CD(cdId, title, artist) # create CD object
        table.append(row) # add CD object to 2nd argument, table

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """Selects a CD object out of table that has the ID cd_idx.

        Args:
            table (list): Inventory list of CD objects
            cd_idx (int): ID of CD object to return
        Raises:
            Exception: If ID is not in list
        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        try: # function for user to select CD before sub menu loop begins
            cd_idx = int(cd_idx)
        except TypeError: # exception trap
            print('CD / Album index was not a number. Returning to menu.')
        except ValueError: # exception trap
            print('CD / Album index was not an accepted number. Returning to menu.')
        for row in table:
            if row.cd_id == cd_idx:
                return row
        else:
            raise Exception('CD / Album index was not found. Returning to menu.')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """Adds a Track object with attributes in track_info to CD.

        Args:
            track_info (tuple): Tuple containing track info (position, title, Length)
            cd (DC.CD): cd object the track gets added to
        Raises:
            Exception: Raised in case position is not an integer
        Returns:
            None: DESCRIPTION

        """
        tkPosition, tkTitle, tkLength = track_info # unpack variables from 1st argument
        try: # function to process IO.ScreenIO.get_track_info from user and create new track object
            tkPosition = int(tkPosition)
        except ValueError: # exception trap
            print('ID must be a number!')
        except:
            raise Exception('ID must be a number!')
        track = DC.Track(tkPosition, tkTitle, tkLength) # create track object
        cd.add_track(track) # add track object to 2nd arugment, CD object