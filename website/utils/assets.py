from flask_assets import Bundle

bundles = {
    'main_scss' : Bundle(
        'scss/main.scss',
        filters='libsass',
        depends=[
            'scss/*.scss',
            'scss/pages/*.scss',
            'scss/components/*.scss',
            'scss/components/parts/*.scss',
            'scss/base/*.scss'
            'scss/forms/*.scss'
        ],
        output='gen/css/main.%(version)s.css'
    ),
    'main_js' : Bundle(
        'js/interface_mods/menu.js',
        'js/interface_mods/slideshow.js',
        'js/interface_mods/scroll.js',
        'js/form_mods/submit_contact.js',
        'js/button_like_listeners.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    )
}