from django import forms
from captcha.fields import CaptchaField

from appcenter.form import *

all_tables_form = {
    "supermanager": mc_supermanager_form,
    "predictions": mc_predictions_form,
    "models": mc_models_form,
    "trainingdata": mc_trainingdata_form,
    "reviews": mc_reviews_form,
    "movies": mc_movies_form,
    "users": mc_users_form,
}
