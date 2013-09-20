__Author__ = "Charlie"

from flask import Flask, send_file
import StringIO
from PIL import Image, ImageFont, ImageDraw

l5r = Flask(__name__)

@l5r.route("/about")
def about():
    return 'a service to generate character sheets for l5r'

@l5r.route("/raw/v1")
def raw_pdfs():
    return 'pdfs'

# Returns an image containing the tallys    
def generate_tally_mask(tallys):

    strikes = tallys / 5
    verticals = tallys - strikes
    width = 4 + verticals * 4

    tally_mask = Image.new(mode = "L", size = (width, 10), color = "White")
    draw = ImageDraw.Draw(tally_mask)
    draw.colour = "black"

    for t in range(0, verticals):
        draw.line([(2+ ( t*4 ) ,0),( 2 + ( t*4 ),10)], fill = "black")

    for s in range(0, strikes):
        st = s + 1
        draw.line([((st * 16) , 0),((st * 16 - 16) , 10)], fill = "black")

    del draw

    return tally_mask

# returns an image with lines and skill tallys
def generate_skill_mask(skill_name, rank, use_tallys = True, width = 150, height = 18, font_size = 14):
    text_mask = Image.new(mode="L", size = (width, height), color ="white")
    draw = ImageDraw.Draw(text_mask)

    draw.line([(0,height-1),(width-40,height-1)], width = 2, fill = "black")
    draw.line([(width-30, height - 1), (width,height-1)], width = 2, fill = "black")

    text_font = ImageFont.truetype("resources/Present_LT_Black_Condensed.ttf",14)
    draw.text((0,0), skill_name, font = text_font, fill="black")
    del draw
    text_mask.paste(generate_tally_mask(5), (120,4))
    return text_mask


def serve_pil_image(pil_img):
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@l5r.route("/imgtest")
def imgtest():
    return serve_pil_image(generate_skill_mask("Lore: Maho", rank = 5))

if __name__ == '__main__':
    l5r.run(debug=True)