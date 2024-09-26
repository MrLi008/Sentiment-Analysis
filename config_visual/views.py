from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.supermanager group by username",
            "管理员姓名",
        )
    # predictions(预测结果表)->predictionid(预测结果的唯一标识符)

    if obj.get("optype") == "predictions.predictionid_pie":
        res = get_pie(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid order by x desc",
            "预测结果的唯一标识符",
        )
    if obj.get("optype") == "predictions.predictionid_pie_v1":
        res = get_pie_v1(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid",
            "预测结果的唯一标识符",
        )
    if obj.get("optype") == "predictions.predictionid_pie_v2":
        res = get_pie_v2(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid",
            "预测结果的唯一标识符",
        )
    if obj.get("optype") == "predictions.predictionid_line":
        res = get_line(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid",
            "预测结果的唯一标识符",
        )
    if obj.get("optype") == "predictions.predictionid_bar":
        res = get_bar(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid",
            "预测结果的唯一标识符",
        )
    if obj.get("optype") == "predictions.predictionid_bar_v1":
        res = get_bar_v1(
            "select predictionid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictionid",
            "预测结果的唯一标识符",
        )
    # predictions(预测结果表)->reviewid(关联到被预测的评论对应评论)

    if obj.get("optype") == "predictions.reviewid_pie":
        res = get_pie(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid order by x desc",
            "关联到被预测的评论对应评论",
        )
    if obj.get("optype") == "predictions.reviewid_pie_v1":
        res = get_pie_v1(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid",
            "关联到被预测的评论对应评论",
        )
    if obj.get("optype") == "predictions.reviewid_pie_v2":
        res = get_pie_v2(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid",
            "关联到被预测的评论对应评论",
        )
    if obj.get("optype") == "predictions.reviewid_line":
        res = get_line(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid",
            "关联到被预测的评论对应评论",
        )
    if obj.get("optype") == "predictions.reviewid_bar":
        res = get_bar(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid",
            "关联到被预测的评论对应评论",
        )
    if obj.get("optype") == "predictions.reviewid_bar_v1":
        res = get_bar_v1(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by reviewid",
            "关联到被预测的评论对应评论",
        )
    # predictions(预测结果表)->modelid(用于做出预测的模型ID关联到模型)

    if obj.get("optype") == "predictions.modelid_pie":
        res = get_pie(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid order by x desc",
            "用于做出预测的模型ID关联到模型",
        )
    if obj.get("optype") == "predictions.modelid_pie_v1":
        res = get_pie_v1(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid",
            "用于做出预测的模型ID关联到模型",
        )
    if obj.get("optype") == "predictions.modelid_pie_v2":
        res = get_pie_v2(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid",
            "用于做出预测的模型ID关联到模型",
        )
    if obj.get("optype") == "predictions.modelid_line":
        res = get_line(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid",
            "用于做出预测的模型ID关联到模型",
        )
    if obj.get("optype") == "predictions.modelid_bar":
        res = get_bar(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid",
            "用于做出预测的模型ID关联到模型",
        )
    if obj.get("optype") == "predictions.modelid_bar_v1":
        res = get_bar_v1(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by modelid",
            "用于做出预测的模型ID关联到模型",
        )
    # predictions(预测结果表)->predictedsentiment(预测的情感倾向结果)

    if obj.get("optype") == "predictions.predictedsentiment_pie":
        res = get_pie(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment order by x desc",
            "预测的情感倾向结果",
        )
    if obj.get("optype") == "predictions.predictedsentiment_pie_v1":
        res = get_pie_v1(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment",
            "预测的情感倾向结果",
        )
    if obj.get("optype") == "predictions.predictedsentiment_pie_v2":
        res = get_pie_v2(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment",
            "预测的情感倾向结果",
        )
    if obj.get("optype") == "predictions.predictedsentiment_line":
        res = get_line(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment",
            "预测的情感倾向结果",
        )
    if obj.get("optype") == "predictions.predictedsentiment_bar":
        res = get_bar(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment",
            "预测的情感倾向结果",
        )
    if obj.get("optype") == "predictions.predictedsentiment_bar_v1":
        res = get_bar_v1(
            "select predictedsentiment x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by predictedsentiment",
            "预测的情感倾向结果",
        )
    # predictions(预测结果表)->confidencescore(预测结果的置信度分数如果模型支持输出的话)

    if obj.get("optype") == "predictions.confidencescore_pie":
        res = get_pie(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore order by x desc",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.confidencescore_pie_v1":
        res = get_pie_v1(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.confidencescore_pie_v2":
        res = get_pie_v2(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.confidencescore_line":
        res = get_line(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.confidencescore_bar":
        res = get_bar(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.confidencescore_bar_v1":
        res = get_bar_v1(
            "select confidencescore x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by confidencescore",
            "预测结果的置信度分数如果模型支持输出的话",
        )
    if obj.get("optype") == "predictions.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm432_bf0a45f882b27e8f.predictions group by createdat order by x",
            "预测结果的创建时间",
        )
    # models(模型表)->modelid(模型的唯一标识符)

    if obj.get("optype") == "models.modelid_pie":
        res = get_pie(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid order by x desc",
            "模型的唯一标识符",
        )
    if obj.get("optype") == "models.modelid_pie_v1":
        res = get_pie_v1(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid",
            "模型的唯一标识符",
        )
    if obj.get("optype") == "models.modelid_pie_v2":
        res = get_pie_v2(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid",
            "模型的唯一标识符",
        )
    if obj.get("optype") == "models.modelid_line":
        res = get_line(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid",
            "模型的唯一标识符",
        )
    if obj.get("optype") == "models.modelid_bar":
        res = get_bar(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid",
            "模型的唯一标识符",
        )
    if obj.get("optype") == "models.modelid_bar_v1":
        res = get_bar_v1(
            "select modelid x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelid",
            "模型的唯一标识符",
        )
    # models(模型表)->modelname(模型的名称或版本信息)

    if obj.get("optype") == "models.modelname_pie":
        res = get_pie(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname order by x desc",
            "模型的名称或版本信息",
        )
    if obj.get("optype") == "models.modelname_pie_v1":
        res = get_pie_v1(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname",
            "模型的名称或版本信息",
        )
    if obj.get("optype") == "models.modelname_pie_v2":
        res = get_pie_v2(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname",
            "模型的名称或版本信息",
        )
    if obj.get("optype") == "models.modelname_line":
        res = get_line(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname",
            "模型的名称或版本信息",
        )
    if obj.get("optype") == "models.modelname_bar":
        res = get_bar(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname",
            "模型的名称或版本信息",
        )
    if obj.get("optype") == "models.modelname_bar_v1":
        res = get_bar_v1(
            "select modelname x,count(*) y from vm432_bf0a45f882b27e8f.models group by modelname",
            "模型的名称或版本信息",
        )
    # models(模型表)->trainingdataid(用于训练该模型的数据集ID关联到训练数据集)

    if obj.get("optype") == "models.trainingdataid_pie":
        res = get_pie(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid order by x desc",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    if obj.get("optype") == "models.trainingdataid_pie_v1":
        res = get_pie_v1(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    if obj.get("optype") == "models.trainingdataid_pie_v2":
        res = get_pie_v2(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    if obj.get("optype") == "models.trainingdataid_line":
        res = get_line(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    if obj.get("optype") == "models.trainingdataid_bar":
        res = get_bar(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    if obj.get("optype") == "models.trainingdataid_bar_v1":
        res = get_bar_v1(
            "select trainingdataid x,count(*) y from vm432_bf0a45f882b27e8f.models group by trainingdataid",
            "用于训练该模型的数据集ID关联到训练数据集",
        )
    # models(模型表)->accuracy(模型的准确率基于验证集或测试集的评估结果)

    if obj.get("optype") == "models.accuracy_pie":
        res = get_pie(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy order by x desc",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.accuracy_pie_v1":
        res = get_pie_v1(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.accuracy_pie_v2":
        res = get_pie_v2(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.accuracy_line":
        res = get_line(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.accuracy_bar":
        res = get_bar(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.accuracy_bar_v1":
        res = get_bar_v1(
            "select accuracy x,count(*) y from vm432_bf0a45f882b27e8f.models group by accuracy",
            "模型的准确率基于验证集或测试集的评估结果",
        )
    if obj.get("optype") == "models.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm432_bf0a45f882b27e8f.models group by createdat order by x",
            "模型的创建时间训练完成时间",
        )
    if obj.get("optype") == "models.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm432_bf0a45f882b27e8f.models group by updatedat order by x",
            "模型的最后更新时间如果有进一步的训练或调整",
        )
    # trainingdata(训练数据集表)->dataid(训练数据条目的唯一标识符)

    if obj.get("optype") == "trainingdata.dataid_pie":
        res = get_pie(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid order by x desc",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.dataid_pie_v1":
        res = get_pie_v1(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.dataid_pie_v2":
        res = get_pie_v2(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.dataid_line":
        res = get_line(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.dataid_bar":
        res = get_bar(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.dataid_bar_v1":
        res = get_bar_v1(
            "select dataid x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by dataid",
            "训练数据条目的唯一标识符",
        )
    if obj.get("optype") == "trainingdata.reviewcontent_wordcloud":
        textlist = get_data(
            "SELECT reviewcontent result FROM vm432_bf0a45f882b27e8f.trainingdata;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # trainingdata(训练数据集表)->sentimentlabel(情感标签用于监督学习如正面为1负面为0)

    if obj.get("optype") == "trainingdata.sentimentlabel_pie":
        res = get_pie(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel order by x desc",
            "情感标签用于监督学习如正面为1负面为0",
        )
    if obj.get("optype") == "trainingdata.sentimentlabel_pie_v1":
        res = get_pie_v1(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel",
            "情感标签用于监督学习如正面为1负面为0",
        )
    if obj.get("optype") == "trainingdata.sentimentlabel_pie_v2":
        res = get_pie_v2(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel",
            "情感标签用于监督学习如正面为1负面为0",
        )
    if obj.get("optype") == "trainingdata.sentimentlabel_line":
        res = get_line(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel",
            "情感标签用于监督学习如正面为1负面为0",
        )
    if obj.get("optype") == "trainingdata.sentimentlabel_bar":
        res = get_bar(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel",
            "情感标签用于监督学习如正面为1负面为0",
        )
    if obj.get("optype") == "trainingdata.sentimentlabel_bar_v1":
        res = get_bar_v1(
            "select sentimentlabel x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by sentimentlabel",
            "情感标签用于监督学习如正面为1负面为0",
        )
    # trainingdata(训练数据集表)->usedfortraining(示该数据条目是否已被用于模型训练)

    if obj.get("optype") == "trainingdata.usedfortraining_pie":
        res = get_pie(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining order by x desc",
            "示该数据条目是否已被用于模型训练",
        )
    if obj.get("optype") == "trainingdata.usedfortraining_pie_v1":
        res = get_pie_v1(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining",
            "示该数据条目是否已被用于模型训练",
        )
    if obj.get("optype") == "trainingdata.usedfortraining_pie_v2":
        res = get_pie_v2(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining",
            "示该数据条目是否已被用于模型训练",
        )
    if obj.get("optype") == "trainingdata.usedfortraining_line":
        res = get_line(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining",
            "示该数据条目是否已被用于模型训练",
        )
    if obj.get("optype") == "trainingdata.usedfortraining_bar":
        res = get_bar(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining",
            "示该数据条目是否已被用于模型训练",
        )
    if obj.get("optype") == "trainingdata.usedfortraining_bar_v1":
        res = get_bar_v1(
            "select usedfortraining x,count(*) y from vm432_bf0a45f882b27e8f.trainingdata group by usedfortraining",
            "示该数据条目是否已被用于模型训练",
        )
    # reviews(评论表)->reviewid(评论的唯一标识符)

    if obj.get("optype") == "reviews.reviewid_pie":
        res = get_pie(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid order by x desc",
            "评论的唯一标识符",
        )
    if obj.get("optype") == "reviews.reviewid_pie_v1":
        res = get_pie_v1(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid",
            "评论的唯一标识符",
        )
    if obj.get("optype") == "reviews.reviewid_pie_v2":
        res = get_pie_v2(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid",
            "评论的唯一标识符",
        )
    if obj.get("optype") == "reviews.reviewid_line":
        res = get_line(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid",
            "评论的唯一标识符",
        )
    if obj.get("optype") == "reviews.reviewid_bar":
        res = get_bar(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid",
            "评论的唯一标识符",
        )
    if obj.get("optype") == "reviews.reviewid_bar_v1":
        res = get_bar_v1(
            "select reviewid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by reviewid",
            "评论的唯一标识符",
        )
    # reviews(评论表)->userid(评论者的用户ID关联到用户)

    if obj.get("optype") == "reviews.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid order by x desc",
            "评论者的用户ID关联到用户",
        )
    if obj.get("optype") == "reviews.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid",
            "评论者的用户ID关联到用户",
        )
    if obj.get("optype") == "reviews.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid",
            "评论者的用户ID关联到用户",
        )
    if obj.get("optype") == "reviews.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid",
            "评论者的用户ID关联到用户",
        )
    if obj.get("optype") == "reviews.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid",
            "评论者的用户ID关联到用户",
        )
    if obj.get("optype") == "reviews.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by userid",
            "评论者的用户ID关联到用户",
        )
    # reviews(评论表)->movieid(被评论的电影ID关联到电影)

    if obj.get("optype") == "reviews.movieid_pie":
        res = get_pie(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid order by x desc",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.movieid_pie_v1":
        res = get_pie_v1(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.movieid_pie_v2":
        res = get_pie_v2(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.movieid_line":
        res = get_line(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.movieid_bar":
        res = get_bar(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.movieid_bar_v1":
        res = get_bar_v1(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by movieid",
            "被评论的电影ID关联到电影",
        )
    if obj.get("optype") == "reviews.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm432_bf0a45f882b27e8f.reviews;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "reviews.sentiment_wordcloud":
        textlist = get_data(
            "SELECT sentiment result FROM vm432_bf0a45f882b27e8f.reviews;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "reviews.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by createdat order by x",
            "评论的创建时间",
        )
    if obj.get("optype") == "reviews.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm432_bf0a45f882b27e8f.reviews group by updatedat order by x",
            "评论的最后更新时间如果允许编辑的话",
        )
    # movies(电影表)->movieid(电影的唯一标识符)

    if obj.get("optype") == "movies.movieid_pie":
        res = get_pie(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid order by x desc",
            "电影的唯一标识符",
        )
    if obj.get("optype") == "movies.movieid_pie_v1":
        res = get_pie_v1(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid",
            "电影的唯一标识符",
        )
    if obj.get("optype") == "movies.movieid_pie_v2":
        res = get_pie_v2(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid",
            "电影的唯一标识符",
        )
    if obj.get("optype") == "movies.movieid_line":
        res = get_line(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid",
            "电影的唯一标识符",
        )
    if obj.get("optype") == "movies.movieid_bar":
        res = get_bar(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid",
            "电影的唯一标识符",
        )
    if obj.get("optype") == "movies.movieid_bar_v1":
        res = get_bar_v1(
            "select movieid x,count(*) y from vm432_bf0a45f882b27e8f.movies group by movieid",
            "电影的唯一标识符",
        )
    # movies(电影表)->title(电影的标题)

    if obj.get("optype") == "movies.title_pie":
        res = get_pie(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title order by x desc",
            "电影的标题",
        )
    if obj.get("optype") == "movies.title_pie_v1":
        res = get_pie_v1(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title",
            "电影的标题",
        )
    if obj.get("optype") == "movies.title_pie_v2":
        res = get_pie_v2(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title",
            "电影的标题",
        )
    if obj.get("optype") == "movies.title_line":
        res = get_line(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title",
            "电影的标题",
        )
    if obj.get("optype") == "movies.title_bar":
        res = get_bar(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title",
            "电影的标题",
        )
    if obj.get("optype") == "movies.title_bar_v1":
        res = get_bar_v1(
            "select title x,count(*) y from vm432_bf0a45f882b27e8f.movies group by title",
            "电影的标题",
        )
    if obj.get("optype") == "movies.releasedate_line":
        res = get_line(
            "select releasedate x,count(*) y from vm432_bf0a45f882b27e8f.movies group by releasedate order by x",
            "电影的发布日期",
        )
    # movies(电影表)->genre(电影的类型如动作、喜剧、剧情等)

    if obj.get("optype") == "movies.genre_pie":
        res = get_pie(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre order by x desc",
            "电影的类型如动作、喜剧、剧情等",
        )
    if obj.get("optype") == "movies.genre_pie_v1":
        res = get_pie_v1(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre",
            "电影的类型如动作、喜剧、剧情等",
        )
    if obj.get("optype") == "movies.genre_pie_v2":
        res = get_pie_v2(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre",
            "电影的类型如动作、喜剧、剧情等",
        )
    if obj.get("optype") == "movies.genre_line":
        res = get_line(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre",
            "电影的类型如动作、喜剧、剧情等",
        )
    if obj.get("optype") == "movies.genre_bar":
        res = get_bar(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre",
            "电影的类型如动作、喜剧、剧情等",
        )
    if obj.get("optype") == "movies.genre_bar_v1":
        res = get_bar_v1(
            "select genre x,count(*) y from vm432_bf0a45f882b27e8f.movies group by genre",
            "电影的类型如动作、喜剧、剧情等",
        )
    # movies(电影表)->director(电影导演的名字)

    if obj.get("optype") == "movies.director_pie":
        res = get_pie(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director order by x desc",
            "电影导演的名字",
        )
    if obj.get("optype") == "movies.director_pie_v1":
        res = get_pie_v1(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director",
            "电影导演的名字",
        )
    if obj.get("optype") == "movies.director_pie_v2":
        res = get_pie_v2(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director",
            "电影导演的名字",
        )
    if obj.get("optype") == "movies.director_line":
        res = get_line(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director",
            "电影导演的名字",
        )
    if obj.get("optype") == "movies.director_bar":
        res = get_bar(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director",
            "电影导演的名字",
        )
    if obj.get("optype") == "movies.director_bar_v1":
        res = get_bar_v1(
            "select director x,count(*) y from vm432_bf0a45f882b27e8f.movies group by director",
            "电影导演的名字",
        )
    # movies(电影表)->cast(电影的主要演员列)

    if obj.get("optype") == "movies.cast_pie":
        res = get_pie(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast order by x desc",
            "电影的主要演员列",
        )
    if obj.get("optype") == "movies.cast_pie_v1":
        res = get_pie_v1(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast",
            "电影的主要演员列",
        )
    if obj.get("optype") == "movies.cast_pie_v2":
        res = get_pie_v2(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast",
            "电影的主要演员列",
        )
    if obj.get("optype") == "movies.cast_line":
        res = get_line(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast",
            "电影的主要演员列",
        )
    if obj.get("optype") == "movies.cast_bar":
        res = get_bar(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast",
            "电影的主要演员列",
        )
    if obj.get("optype") == "movies.cast_bar_v1":
        res = get_bar_v1(
            "select cast x,count(*) y from vm432_bf0a45f882b27e8f.movies group by cast",
            "电影的主要演员列",
        )
    # movies(电影表)->rating(电影的评分可以是用户评分的平均值)

    if obj.get("optype") == "movies.rating_pie":
        res = get_pie(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating order by x desc",
            "电影的评分可以是用户评分的平均值",
        )
    if obj.get("optype") == "movies.rating_pie_v1":
        res = get_pie_v1(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating",
            "电影的评分可以是用户评分的平均值",
        )
    if obj.get("optype") == "movies.rating_pie_v2":
        res = get_pie_v2(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating",
            "电影的评分可以是用户评分的平均值",
        )
    if obj.get("optype") == "movies.rating_line":
        res = get_line(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating",
            "电影的评分可以是用户评分的平均值",
        )
    if obj.get("optype") == "movies.rating_bar":
        res = get_bar(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating",
            "电影的评分可以是用户评分的平均值",
        )
    if obj.get("optype") == "movies.rating_bar_v1":
        res = get_bar_v1(
            "select rating x,count(*) y from vm432_bf0a45f882b27e8f.movies group by rating",
            "电影的评分可以是用户评分的平均值",
        )
    # users(用户表)->userid(用户的唯一标识符)

    if obj.get("optype") == "users.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid order by x desc",
            "用户的唯一标识符",
        )
    if obj.get("optype") == "users.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid",
            "用户的唯一标识符",
        )
    if obj.get("optype") == "users.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid",
            "用户的唯一标识符",
        )
    if obj.get("optype") == "users.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid",
            "用户的唯一标识符",
        )
    if obj.get("optype") == "users.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid",
            "用户的唯一标识符",
        )
    if obj.get("optype") == "users.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm432_bf0a45f882b27e8f.users group by userid",
            "用户的唯一标识符",
        )
    # users(用户表)->username(用户名用于登录和识别用户)

    if obj.get("optype") == "users.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username order by x desc",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.username_line":
        res = get_line(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm432_bf0a45f882b27e8f.users group by username",
            "用户名用于登录和识别用户",
        )
    if obj.get("optype") == "users.email_wordcloud":
        textlist = get_data("SELECT email result FROM vm432_bf0a45f882b27e8f.users;")
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "users.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm432_bf0a45f882b27e8f.users group by createdat order by x",
            "用户账户的创建时间",
        )
    if obj.get("optype") == "users.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm432_bf0a45f882b27e8f.users group by updatedat order by x",
            "用户账户的最后更新时间",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())


def view_predictions(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tppredictions.html", locals())


def view_models(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmodels.html", locals())


def view_trainingdata(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tptrainingdata.html", locals())


def view_reviews(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpreviews.html", locals())


def view_movies(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpmovies.html", locals())


def view_users(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpusers.html", locals())
