# What is Map_Art

Map_Art is a combination of programs to convert a .png Image into a placeable form for a scarpet app.

# How to use? (recomendet)

1. Download the **.exe** and **.sc** files from the release page
2. Put the **.exe** file with the image you want to convert into a map_art into the same folder
3. Rename the image to **_Map_Art.png_**
   - This is **_very important_**, if you dont rename the image corectly it doesnt work! 
4. Execute the **.exe**-file
5. Wait until the magic is finished
   - First a cmd window will open and count up. Until it reached 100% it will close automatically and the magic is finished
6. Now you should have a new folder named **_map_art_placement.data_**
7. Put the **_map_art_placement.data_**-folder and the **_map_art_placement.sc_**-file into your worlds **script**-folder
   - The scripts-folder is located at **\.minecraft\saves\ _your worlds name_\scripts**
8. Start your minecraft world you put the files into the scripts folder
   - Its recomendet to use a super flat world
9. Load the script with the following comand `/script load map_art_placement`
10. Make sure that no importan builds are in the area of -64, 0, -64 to 64, 255, 64
11. To clear the area use `/script in map_art_placement invoke fill_air` 
12. To place the map art use `/script in map_art_placement invoke place_map_art`

# How to use? (.py file)

If you want a bigger map art you need to change the values for **pic_width** and **pic_height** in the .py file. To adjust the placement for the scarpet app you need to change the values after the "<" in the last **c_for** loop. 

At the moment it could happen, that some blocks have a bigger y value than minecraft can handle. So change of the size at your own risk.

# Contact

Discord: rekkep#7705
