Hi I'm ProximaLXXVI,
thank you for downloading the MultiFaceFuser.

Some info before using this service:
Currently there is no UI, if you would like to work on it or give me some feedbacks or 
suggestion in order to simplify the usage I would really appreciate it

##########################################################################################################################################

You will install 2 different files that you will need to modify but first you need to follow a few steps:

Locate the path where you installed FaceFusion and create 3 different folders (E.g. Source, Target & Output)
The "Source" folder will be used for the Source Images (the faces you want to be swapped onto the Target Images)
The "Target" folder will be used for the Target Images (the images where the face will be swapped)
The "Output" folder will contain all the finished results after running the .bat

The first file you will install is face_swapper.py
Move the python script to your FaceFusion folder
Open with any editor the .py file, change the FaceFusion folder path (base_path variable) 
and the "FOLDER NAME" of the 3 different folders you created previously.

The second file you will install is MultiFaceFuser.bat
Before using the .bat and start the swapping you will need to modify it.
Open with any editor the .bat file and change the Path to the FaceFusion folder

##########################################################################################################################################

Once you finished these steps you are ready to face-swap. Add images in the "source" & "target" folder you created previously and start the .bat file. You will find the result in the output Folder