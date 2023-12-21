import os
import subprocess

# Path to the root folder and virtual environment
base_path = 'C:\\path\\to\\facefusion' # Modify with FaceFusion's installation path
venv_activate = os.path.join(base_path, 'venv\\Scripts\\activate')

# Activate the virtual environment
subprocess.run(f'"{venv_activate}" & cd /d "{base_path}"', shell=True)

# Folder path (works with folders created in the same path as FaceFusion)
source_path = os.path.join(base_path, 'FOLDER NAME')
target_path = os.path.join(base_path, 'FOLDER NAME')
output_path = os.path.join(base_path, 'FOLDER NAME')

# List of files in the 'source' folder
source_files = [f for f in os.listdir(source_path) if f.endswith((".png", ".jpg", ".jpeg"))]

# List of files in the 'target' folder
target_files = [f for f in os.listdir(target_path) if f.endswith((".png", ".jpg", ".jpeg"))]

# Check if there are files in both 'source' and 'target'
if source_files and target_files:
    # Get the first file from 'source'
    source_file = source_files[0]

    # Generate and execute a command line for each file in 'target'
    for target_file in target_files:
        command_line = f'python run.py -s "{os.path.join(source_path, source_file)}" -t "{os.path.join(target_path, target_file)}" -o "{output_path}" --headless --frame-processor face_swapper face_enhancer --face-enhancer-model gfpgan_1.4'
        subprocess.run(command_line, shell=True, check=True)
else:
    print("There are not enough files in the 'source' or 'target' folders.")
	
