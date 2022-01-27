from flask import render_template
from app.main import bp
from app.main.Forms import EmailForm



@bp.route('/')
@bp.route('/home')
def home():


    return render_template(
        'home.html',
        title='Home',

        )
@bp.route('/eatmyass')
def eatmyass():
    form = EmailForm()
    return render_template(
        'eatmyass.html',
        title='Joe Byron',
        form = form
    )