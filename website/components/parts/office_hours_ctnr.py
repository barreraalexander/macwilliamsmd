from flask import Markup
from website.blueprints.main import CONTACT_DICT, unpack_elems

def component(office):
    if (office=="office1"):
        address = CONTACT_DICT.get('address1')
        city = CONTACT_DICT.get('address_city1')
        hours = {
            'Monday' : 'Closed',
            'Tuesday' : '9:00am - 5:00pm',
            'Wednesday' : '9:00am - 5:00pm',
            'Thursday' : 'Closed',
            'Friday' : '9:00am - 5:00pm',
            'Saturday' : 'Closed',
            'Sunday' : 'Closed',
        }

    elif (office=="office2"):
        address = CONTACT_DICT.get('address2')
        city = CONTACT_DICT.get('address_city2')
        hours = {
            'Monday' : '9:00am - 5:00pm',
            'Tuesday' : 'Closed',
            'Wednesday' : 'Closed',
            'Thursday' : '9:00am - 5:00pm',
            'Friday' : 'Closed',
            'Saturday' : 'Closed',
            'Sunday' : 'Closed',
        }

    office_hours = [
        f"""
        <div class="office_hour" data-time="{hours.get(elem)}">
            <p class="date">
                {elem}
            </p>
            <p class="time">
                {hours.get(elem)}
            </p>
        </div>
        """
        for elem in hours
    ]



    return Markup(f"""
    <div class="office_hours_ctnr">
        <h2>
            Office Hours | <span> {city} </span>
        </h2>
        <small>
            {address}
        </small>
        {unpack_elems(office_hours)}
    </div>    
    """)