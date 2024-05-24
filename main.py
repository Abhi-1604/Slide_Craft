from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_AI import create_slides_ai
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_Floral import create_slides_floral
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_Flower import create_slides_flower
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_Old_aesthetic import create_slides_old_aesthetic
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_Simple_game import create_slides_simple_game
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_art import create_slides_art
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_business import create_slides_business
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_company import create_slides_company
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_environment import create_slides_environment
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_geometry import create_slides_geometry
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_marketing import create_slides_marketing
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_professional_business import create_slides_professional_business
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_solid_grey import create_slides_solid_grey
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_technology import create_slides_technology
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentation_water import create_slides_water
from Slide_Craft_dupli.Slide_Craft_dupli.Slide_Craft.presentational_plants import create_slides_plants
from presentation_futuristic import create_slides_futuristic
from presentation_galaxy import create_slides_galaxy
from presentation_historical import create_slides_historical
from presentation_modern import create_slides_modern
from chat import chat_with_gpt
from presentation_cyberpunk import create_slides_cyberpunk
from presentation_cube import create_slides_cube
from gui import gui

google_api_key = "AIzaSyBJnQIS_XMOdax8WtjKROG20pgCANHMw0U"
google_search_engine_id = "f6d5812a377554523"

def answer(response):

    topic = response[0]
    pic = response[1]
    slide_number = response[2]
    template = response[3]
    choice = response[4]
    slide_title = []
    if choice == 1:
        for i in range(slide_number):
            slide_title.append(response[i+5])
    if template == 5:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_cyberpunk(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 1:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_cube(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 2:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_futuristic(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 3:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_galaxy(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 4:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_historical(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 6:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_modern(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 7:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_ai(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 8:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_business(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 9:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_company(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 10:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_floral(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 11:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_flower(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 12:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_geometry(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 13:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_marketing(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 14:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_old_aesthetic(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 15:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_professional_business(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 16:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_simple_game(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 17:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_technology(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 18:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_water(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 19:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_plants(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 20:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_environment(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 21:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_art(gpt_response, slide_title, slide_number, topic, choice, pic)
    elif template == 22:
        gpt_response = chat_with_gpt(topic, slide_number, slide_title, choice)
        create_slides_solid_grey(gpt_response, slide_title, slide_number, topic, choice, pic)

    else:
        print("error")

gui(answer)    