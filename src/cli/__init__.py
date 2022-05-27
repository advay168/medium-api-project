from .main import app as app_

is_zipapp = __package__ is None


def app():
    if is_zipapp:
        return app_(prog_name="python app.pyz")
    else:
        return app_()
