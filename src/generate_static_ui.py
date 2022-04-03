# based on works of tux (linux mascot) folks (https://github.com/ryleu/tux-on-place)
# humanova 2022

import matplotlib.pyplot as plt

ui_scale = 8

def generate_static_webpage(image_path: str, output_filename:str, top_left:tuple):
    generated = ""
    p = plt.imread(image_path)
    for row in range(len(p)):
        generated += f"<div class='row' style='top: {row * ui_scale}px;'>"
        for square in range(len(p[row])):
            color = f"rgba({p[row][square][0]*255},{p[row][square][1]*255},{p[row][square][2]*255},{p[row][square][3]})"
            hide_transparent_tile_css = "pointer-events: none" if p[row][square][3] == 0 else ""
            generated += f"<a style='background-color: {color};left: {square * ui_scale}px; {hide_transparent_tile_css}' class='square' href='https://new.reddit.com/r/place/?cx={top_left[0] + square}&cy={top_left[1] + row}&px=20' onMouseOver='onTileHovered({square}, {row })'></a>\n"
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
        z-index: 1;
        border: solid 1px black;
        outline: solid 1px white;
    }}
    .info{{
        color: black;
        position: absolute;
        background-color: white;
        font-family: monospace;
        z-index: 2;
        border-radius: 8px;
        height: 20px;
        font-size: 16px;
        width: 100px;
        pointer-events: none;
        text-align: center;
        border: solid 1px black;
        outline: solid 1px white;
    }}
    </style>
    
    <script>
        function onTileHovered(x, y) {{
        const pos = document.getElementById("pos");
        pos.innerText = "[" + (x + { top_left[0] }) + ", " + (y + {top_left[1]}) + "]";
        pos.style.left = x * {ui_scale} + 16 + "px";
        pos.style.top = y * {ui_scale} - 6 + "px";
      }}
    </script>

    <body>
    <div id="pos" class="info">[999,999]</div> 
    {generated}
    </body>
    </html>
    """
    
    with open(f"../{output_filename}", "w") as file:
        file.write(website_template)


if __name__ == '__main__':
    generate_static_webpage(image_path="../img/topright_ataturk2.png",
                            output_filename="ataturk.html",
                            top_left=(1000, 0))

    generate_static_webpage(image_path="../img/ramizdayi.png",
        output_filename="ramizdayi.html",
        top_left=(881, 1745))

    #generate_static_webpage(image_path="../img/turkish_flag3_with_text.png",
    #                        output_filename="index.html",
    #                        top_left=(299,343))

    #generate_static_webpage(image_path="../img/turkish_flag3_with_text.png",
    #                    output_filename="bayrak2.html",
    #                    top_left=(299,343))

    #generate_static_webpage(image_path="../img/chad.png",
    #                    output_filename="zade.html",
    #                    top_left=(480,414))

    generate_static_webpage(image_path="../img/2balkan4u.png",
            output_filename="2b4u.html",
            top_left=(1900,1583))

    generate_static_webpage(image_path="../img/kgbtr.png",
                    output_filename="kgbtr.html",
                    top_left=(736,1440))
    
    #generate_static_webpage(image_path="../img/kgbtr2.png",
    #            output_filename="kgbtr2.html",
    #            top_left=(1072, 120))

    generate_static_webpage(image_path="../img/maoy.png",
            output_filename="maoy.html",
            top_left=(1219,60))

    #generate_static_webpage(image_path="../img/turkey-and-ataturk.png",
    #                        output_filename="index.html",
    #                        top_left=(299,318))
