from flask import Markup

def component():
    return Markup(f"""
    <div class="slide_dots_ctnr">
        <div
            class="slide_dot"
            data-active='true'
            data-slide_index=0
        >
        </div>
        <div
            class="slide_dot"
            data-slide_index=1
        >
        </div>
        <div
            class="slide_dot"
            data-slide_index=2
        >
        </div>
        <div
            class="slide_dot"
            data-slide_index=3
        >
        </div>
        <div
            class="slide_dot"
            data-slide_index=4
        >
        </div>
    </div>
    """)