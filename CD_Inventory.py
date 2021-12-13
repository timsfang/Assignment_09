#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# TFang, 2021-Dec-11, added code to work with modules and completed todos for Assignment 09
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l': # load CD inventory from file
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            print() # extra line for layout
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a': # add CD/album object
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd': # display CD inventory
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c': # choose CD/album object
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Please select the CD / Album index: ').strip()
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        while True: # sub menu loop for tracks in CD object
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            # sub menu choices for handling tracks
            if strChoice == 'a': # add track to CD object
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                print('Track added.')
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'd': # display track objects
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'r': # remove track object from CD object
                IO.ScreenIO.show_tracks(cd)
                track_idx = input('Please select the track index: ').strip()
                cd.rmv_track(track_idx) # delete track object from list in CD object
                print('Track removed.')
                IO.ScreenIO.show_tracks(cd)
            elif strChoice == 'x': # exit sub menu
                break
            else:
                print('General Error')
    elif strChoice == 's': # save CD inventory to file
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')