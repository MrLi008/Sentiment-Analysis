from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tppredictions",
        views.view_predictions,
        name="bi_tppredictions",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmodels",
        views.view_models,
        name="bi_tpmodels",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tptrainingdata",
        views.view_trainingdata,
        name="bi_tptrainingdata",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpreviews",
        views.view_reviews,
        name="bi_tpreviews",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmovies",
        views.view_movies,
        name="bi_tpmovies",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpusers",
        views.view_users,
        name="bi_tpusers",
    ),
]
