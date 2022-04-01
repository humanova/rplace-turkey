# based on works of tux (linux mascot) folks (https://github.com/ryleu/tux-on-place)
# humanova 2022

import matplotlib.pyplot as plt

top_left = (299, 318)
ui_scale = 10

def generate_static_webpage(filename: str):
    generated = ""
    p = plt.imread(filename)
    for row in range(len(p)):
        generated += f"<div class='row' style='top: {row * ui_scale}px;'>"
        for square in range(len(p[row])):
            color = f"rgba({p[row][square][0]*255},{p[row][square][1]*255},{p[row][square][2]*255},{p[row][square][3]})"
            generated += f"<a style='background-color: {color};left: {square * ui_scale}px;' class='square' href='https://new.reddit.com/r/place/?cx={top_left[0] + square}&cy={top_left[1] + row}&px=20'></a>\n"
        generated += "</div>"

    website_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <style>
    * {{
        top: 0;
        left: 0;
        padding: 0;
        margin: 0;
        width: {ui_scale}px;
        height: {ui_scale}px;
    }}
    .row {{
        position: absolute;
        width: {ui_scale * len(p[0])}px;
    }}
    .square {{
        position: absolute;
    }}
    .square:hover {{
        border-style: solid;
        border-radius: 0;
        border-thickness: 2px;
        border-color: gray;
    }}
    </style>
    <body>
    {generated}
    </body>
    </html>
    """
    with open("index.html", "w") as file:
        file.write(website_template)


if __name__ == '__main__':
    generate_static_webpage(filename="turkey-and-ataturk.png")
