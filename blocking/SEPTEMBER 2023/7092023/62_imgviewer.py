import PySimpleGUI as sg 
import os.path 

# First the window layout in 2 columns 

file_list_column = [ 
    [ 
        sg.Text("Image Folder"), 
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"), 
        sg.FolderBrowse(), 
    ], 
    [
        sg.Listbox( 
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

#for now will only show the name of the file that was chosen 
image_viewer_column = [ 
    [sg.Text("Choose an image from list on left: ")], 
    [sg.Text(size=(40, 1), key="-TOUT-")], 
    [sg.Image(key="-IMAGE")], 
]

# Full layout 
layout = [ 
    [
        sg.Column(file_list_column), 
        sg.VSeperator(), 
        sg.Column(image_viewer_column), 
    ]
]

window = sg.Window("Image Viewer", layout)

while True: 
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break 

    if event == "-FOLDER-": 
        folder = values["-FOLDER"]
        try: 
            file_list = os.listdir(folder)
        except: 
            file_list = []

        fnames = [ 
            f 
            for f in file_list 
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))
        ]
        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-": 
        try: 
            filename = os.path.join (
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)

            try: 
                window["-IMAGE-"].update(filename=filename)
            except Exception as e: 
                print(f"Error updating image: {e}")
        except Exception as e: 
                print(f"Error loading selected file: {e}")

window.close()