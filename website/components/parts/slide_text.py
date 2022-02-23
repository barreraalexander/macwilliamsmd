from flask import Markup

def component(slide_name):
    slide_h1 = ""
    slide_small = ""
    if slide_name == "welcome":
        slide_h1 = "Mac Williams MD"
        slide_small = "& Associates"

    elif slide_name == "ekg":
        slide_h1 = ""
        slide_small = ""

    elif slide_name == "laboratory":
        slide_h1 = "Lab Work"
        slide_small = "Analysis Solutions"
        
    elif slide_name == "radiology":
        slide_h1 = "Radiology"
        slide_small = "Medical Diagnosis"
        
    elif slide_name == "gynecology":
        slide_h1 = "Gynecology"
        slide_small = "Reproductive Health"
        
    
    return Markup(f"""
    <div id="{slide_name}_slide_text" class="slide_text_ctnr">
        <h1 id="slide_h1">
            {slide_h1}
        </h1>
        <small id="slide_small">
            {slide_small}
        </small>
    </div>
    """)