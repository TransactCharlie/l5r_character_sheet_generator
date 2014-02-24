import StringIO
from PIL import Image, ImageDraw
from flask import send_file
from config import FONT, USE_TALLYS

__author__ = 'Charlie'

def generate_tally_mask(tallys):
    """returns an image with tally marks
    @type tallys:int
    @rtype: Image"""

    strikes = tallys / 5
    verticals = tallys - strikes
    width = 4 + verticals * 4

    tally_mask = Image.new(mode = "L", size = (width, 10), color = "White")
    draw = ImageDraw.Draw(tally_mask)
    draw.colour = "black"

    for t in range(0, verticals):
        draw.line([(2 + ( t * 4 ) ,0),( 2 + ( t * 4 ), 10)], fill = "black")

    for s in range(0, strikes):
        st = s + 1
        draw.line([((st * 16) , 0),((st * 16 - 16) , 10)], fill = "black")

    del draw
    return tally_mask



def generate_skill_mask(skill, use_tallys = USE_TALLYS,  font = FONT, width = 150, height = 18,):
    """Returns an image for a skill...
    @rtype: Images"""

    text_mask = Image.new(mode="L", size = (width, height), color ="white")
    draw = ImageDraw.Draw(text_mask)

    draw.line([(0,height-1),(width-40,height-1)], width = 2, fill = "black")
    draw.line([(width-30, height - 1), (width,height-1)], width = 2, fill = "black")
    draw.text((0,0), skill.Skill, font = font, fill="black")

    del draw
    text_mask.paste(generate_tally_mask(skill.Rank), (120,4))
    return text_mask



def generate_skills_mask(skills, width = 150, height = 400):
    """returns a skills mask
    @rType: Image"""
    skills_mask = Image.new(mode = "L", size = (width, height), color = "white")

    for i, skill in enumerate(sorted(skills, key = lambda k: k.Skill)):
        skills_mask.paste(generate_skill_mask(skill), (0, (i + 1) *20))

    return skills_mask



def serve_pil_image(pil_img):
    """converts a pil Image into a fake file IO stream of image/png
    @type pil_img: Image
    , @rtype: File"""
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')