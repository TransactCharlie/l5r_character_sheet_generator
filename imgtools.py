import StringIO
from PIL import Image, ImageDraw
from flask import send_file
from config import *
from skills import Skill

__author__ = 'Charlie'

def generate_tally_mask(tallys):
    """returns an image with tally marks
    @type tallys:int
    @rtype: Image"""

    strikes = tallys / 5
    verticals = tallys - strikes
    width = 4 + verticals * 4

    tally_mask = Image.new(mode = "L", size = (width, 10), color = SHEET_BACKGROUND_COLOR)
    draw = ImageDraw.Draw(tally_mask)
    draw.colour = "black"

    for t in range(0, verticals):
        draw.line([(2 + ( t * 4 ) ,0),( 2 + ( t * 4 ), 10)], fill = SHEET_FOREGROUND_COLOR)

    for s in range(0, strikes):
        st = s + 1
        draw.line([((st * 16) , 0),((st * 16 - 16) , 10)], fill = SHEET_FOREGROUND_COLOR)

    del draw
    return tally_mask



def generate_skill_mask(skill, use_tallys = SKILLS_USE_TALLYS,  font = SKILL_FONT, width = SKILLS_CELL_WIDTH, height = SKILLS_CELL_HEIGHT,):
    """Returns an image for a skill...
    @type skill:Skill
    @rtype: Images"""

    text_mask = Image.new(mode="L", size = (width, height), color = SHEET_BACKGROUND_COLOR)
    draw = ImageDraw.Draw(text_mask)

    draw.line([(0,height-SKILL_LINE_THICKNESS),(width-40,height-SKILL_LINE_THICKNESS)], width = SKILL_LINE_THICKNESS, fill = SHEET_FOREGROUND_COLOR)
    draw.line([(width - 30, height - SKILL_LINE_THICKNESS), ( width, height - SKILL_LINE_THICKNESS)], width = SKILL_LINE_THICKNESS, fill = SHEET_FOREGROUND_COLOR)
    draw.text((0,0), skill.skill, font = font, fill = SHEET_FOREGROUND_COLOR)

    if use_tallys:
        text_mask.paste(generate_tally_mask(skill.rank), (SKILLS_CELL_WIDTH - 30,4))
    else:
        draw.text((SKILLS_CELL_WIDTH -30, 0), str(skill.rank), font = font, fill = SHEET_FOREGROUND_COLOR)

    del draw
    return text_mask



def generate_skills_mask(skills, box_size = SKILLS_BOX_SIZE):
    """returns a skills mask
    @type skills: List(Skill)
    @rType: Image"""
    skills_mask = Image.new(mode = "L", size = box_size, color = SHEET_BACKGROUND_COLOR)

    for i, skill in enumerate(skills):
        skills_mask.paste(generate_skill_mask(skill), (0, (i + 1) * SKILL_VERTICAL_SPACING))

    return skills_mask



def serve_pil_image(pil_img):
    """converts a pil Image into a fake file IO stream of image/png
    @type pil_img: Image
    , @rtype: File"""
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')