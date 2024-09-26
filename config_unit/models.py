from django.db import models
from appcenter.models import *
from config_visual.models import *
from sys_user.models import *
from sys_user.func import *

all_tables = dict()
gl = dict()

# Create your models here.

all_tables = {
    "supermanager": mymeta(mc_supermanager),
    "predictions": mymeta(mc_predictions),
    "models": mymeta(mc_models),
    "trainingdata": mymeta(mc_trainingdata),
    "reviews": mymeta(mc_reviews),
    "movies": mymeta(mc_movies),
    "users": mymeta(mc_users),
}

# 所有用户表

all_tables_user = {
    "supermanager": mymeta(mc_supermanager),
    "users": mymeta(mc_users),
}
gl = {
    "supermanager": mc_supermanager,
    "predictions": mc_predictions,
    "models": mc_models,
    "trainingdata": mc_trainingdata,
    "reviews": mc_reviews,
    "movies": mc_movies,
    "users": mc_users,
}
