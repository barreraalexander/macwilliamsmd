from flask import Markup

def component():
    return Markup(f"""
    <div class="slide_dots_ctnr">
        <div
            class="slide_dot"
            data-active='true'
            data-panel_id="welcome_slide_ctnr"
            data-full_img_id="welcome_full"
            data-text_id="welcome_slide_text"
            data-slide_index=0
        >
        </div>
        <div
            class="slide_dot"
            data-panel_id="ekg_slide_ctnr"
            data-full_img_id="ekg_full"
            data-text_id="ekg_slide_text"
            data-slide_index=1
        >
        </div>
        <div
            class="slide_dot"
            data-panel_id="laboratory_slide_ctnr"
            data-full_img_id="laboratory_full"
            data-text_id="laboratory_slide_text"
            data-slide_index=2
        >
        </div>
        <div
            class="slide_dot"
            data-panel_id="radiology_slide_ctnr"
            data-full_img_id="radiology_full"
            data-text_id="radiology_slide_text"
            data-slide_index=3
        >
        </div>
        <div
            class="slide_dot"
            data-panel_id="gynecology_slide_ctnr"
            data-full_img_id="gynecology_full"
            data-text_id="gynecology_slide_text"
            data-slide_index=4
        >
        </div>
    </div>

    
    """)