# based on works of tux (linux mascot) folks (https://github.com/ryleu/tux-on-place)
# humanova 2022

import matplotlib.pyplot as plt
import math
from htmlmin import minify



ui_scale = 8
base_href = "https://new.reddit.com/r/place/"
map_focus_zoom = 20

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))

def minify_html(input_file, output_file):
    with open(input_file, 'r') as f:
        html_content = f.read()

    minified_content = minify(html_content, remove_empty_space=True, remove_comments=True, reduce_empty_attributes=True, remove_all_empty_space=True, remove_optional_attribute_quotes=True, )

    with open(output_file, 'w') as f:
        f.write(minified_content)

def generate_static_webpage(image_path: str, output_filename:str, top_left:tuple):
    (shift_x, shift_y) = top_left
    
    image = plt.imread(image_path)
    
    rows = ""
    colors = []
    height = len(image)
    width = len(image[0])
    color_has_alpha_channel = len(image[0][0])>3
    for row in range(height):
        rows += f"<div>"
        for column in range(width):
            # get pixel channels
            color = list(map(lambda x:clamp(0, math.floor(x*255), 255), image[row][column]))

            item = next(filter(lambda c: c==color, colors), None)

            if item is None:
                colors.append(color)
                index = len(colors)-1
            else:
                index = colors.index(item)
            
            style = []

            # hile tile style
            if color_has_alpha_channel:
                ALPHA = color[-1]
                if ALPHA == 0:
                    style.append( "pointer-events: none")

            style = f"style='{';'.join(style)}'" if len(style)>0 else ""

            # add link for square
            rows += f"<c{index} p='{column}-{row}'></c{index}>\n"

        rows += "</div>"


    website_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <base target="_blank" href="{base_href}" />
        <style>
            * {{
                top: 0;
                left: 0;
                padding: 0;
                margin: 0;
                width: {ui_scale}px;
                height: {ui_scale}px;
            }}
            #content >div {{
                display:flex;
                width: {ui_scale * width}px;
            }}
            #content >div >* {{
                cursor: pointer;
                display: inline-block;
                box-sizing: border-box;
            }}
            #content >div >*:hover {{
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

            {"".join(map(lambda e: f"#content>div>c{str(e[0])} {{ background-color: rgba({','.join(map(lambda n:str(n), e[1]))}); }}", enumerate(colors)))}
        </style>
    
        <script>
            let pos;
            function documentReady() {{
                pos = document.getElementById("pos");

                for(const row of document.getElementById("content").children){{
                        for(const box of row.children){{
                            box
                                .addEventListener("mouseover", (event)=>{{
                                    const element = event.target;
                                    const [x,y] = element.getAttribute("p").split('-').map(n=> parseInt(n));

                                    pos.innerText = "[" + (x + { top_left[0] }) + ", " + (y + {top_left[1]}) + "]";
                                    pos.style.left = x * {ui_scale} + 16 + "px";
                                    pos.style.top = y * {ui_scale} - 6 + "px";
                                }});

                            box
                                .addEventListener("click", (event)=>{{
                                    const element = event.target;
                                    const [x,y] = element.getAttribute("p").split('-').map(n=> parseInt(n));

                                    const cx = x + {shift_x},
                                        cy = y + {shift_y};
                                    window.open(`?cx=${{cx}}&cy=${{cy}}&px={map_focus_zoom}`, "_blank");
                                }});
                        }}
                    }}
            }}

            // Use the DOMContentLoaded event to call the function after the document is ready
            document.addEventListener("DOMContentLoaded", function() {{ documentReady(); }});
            
        </script>
    </head>
    <body>
        <div id="pos" class="info">[?,?]</div> 
        <div id="content">
            {rows}
        </div>
        </body>
    </html>
    """
    
    fileLocation = f"../{output_filename}"
    with open(fileLocation, "w") as file:
        file.write(website_template)

    minify_html(fileLocation, f"{fileLocation.replace('.html', '')}_min.html")


if __name__ == '__main__':
    generate_static_webpage(image_path="../img/bayrak2023_2.png",
                            output_filename="index_new.html",
                            top_left=(-368, 290))

    #generate_static_webpage(image_path="../img/elraenn_bayrak.png",
    #           output_filename="elraenn_bayrak.html",
    #            top_left=(299,343))

    #generate_static_webpage(image_path="../img/shovel.png",
    #            output_filename="shovel.html",
    #            top_left=(317,1902))


    #generate_static_webpage(image_path="../img/ramizdayi.png",
    #    output_filename="ramizdayi.html",
    #    top_left=(881, 1745))

    #generate_static_webpage(image_path="../img/turkish_flag3_with_text.png",
    #                        output_filename="index.html",
    #                        top_left=(299,343))

    #generate_static_webpage(image_path="../img/turkish_flag3_with_text.png",
    #                    output_filename="bayrak2.html",
    #                    top_left=(299,343))

    #generate_static_webpage(image_path="../img/chad.png",
    #                    output_filename="zade.html",
    #                    top_left=(480,414))

    #generate_static_webpage(image_path="../img/2balkan4u.png",
    #        output_filename="2b4u.html",
    #        top_left=(1900,1583))

    #generate_static_webpage(image_path="../img/kgbtr.png",
    #                output_filename="kgbtr.html",
    #                top_left=(736,1440))
    
    #generate_static_webpage(image_path="../img/kgbtr2.png",
    #            output_filename="kgbtr2.html",
    #            top_left=(1072, 120))

    #generate_static_webpage(image_path="../img/maoy.png",
    #        output_filename="maoy.html",
    #        top_left=(1219,60))

    #generate_static_webpage(image_path="../img/turkey-and-ataturk.png",
    #                        output_filename="index.html",
    #                        top_left=(299,318))
