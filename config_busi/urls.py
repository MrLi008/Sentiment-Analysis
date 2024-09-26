from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_busi_view_index"),
    # 如果用到预测算法,图像识别等单页面展示效果的算法去掉下方注释
    path("auto_detect", views.auto_detect, name="config_busi_view_auto_detect"),
    path("supermanager", views.view_supermanager, name="config_busi_view_supermanager"),
    path("predictions", views.view_predictions, name="config_busi_view_predictions"),
    path("models", views.view_models, name="config_busi_view_models"),
    path("trainingdata", views.view_trainingdata, name="config_busi_view_trainingdata"),
    path("reviews", views.view_reviews, name="config_busi_view_reviews"),
    path("movies", views.view_movies, name="config_busi_view_movies"),
    path("users", views.view_users, name="config_busi_view_users"),
]
