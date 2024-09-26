from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统管理员 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_predictions(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 预测结果表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 预测结果的唯一标识符

        mcauthfield_predictionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联到被预测的评论对应评论

        mcauthfield_reviewid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用于做出预测的模型ID关联到模型

        mcauthfield_modelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测的情感倾向结果

        mcauthfield_predictedsentiment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测结果的置信度分数如果模型支持输出的话

        mcauthfield_confidencescore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测结果的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 预测结果表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 预测结果的唯一标识符

        mcauthfield_predictionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联到被预测的评论对应评论

        mcauthfield_reviewid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用于做出预测的模型ID关联到模型

        mcauthfield_modelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测的情感倾向结果

        mcauthfield_predictedsentiment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测结果的置信度分数如果模型支持输出的话

        mcauthfield_confidencescore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 预测结果的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_predictions.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_predictions().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_predictions.objects.filter(**filter)
        else:
            records = mc_predictions.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_reviews_18459 = []
        for m in mc_reviews.objects.all():
            mobj = m.toJson()
            data_mc_reviews_18459.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("createdat"),
                }
            )
        data_mc_models_18460 = []
        for m in mc_models.objects.all():
            mobj = m.toJson()
            data_mc_models_18460.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("modelname"),
                }
            )
        return render(request, "config_busi/predictions.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_predictions()

        # 预测结果的唯一标识符

        if mcauthfield_predictionid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.predictionid = str(uuid.uuid4())
        # 关联到被预测的评论对应评论

        if mcauthfield_reviewid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reviewid = obj.get("reviewid")
        # 用于做出预测的模型ID关联到模型

        if mcauthfield_modelid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.modelid = obj.get("modelid")
        # 预测的情感倾向结果

        if mcauthfield_predictedsentiment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.predictedsentiment = obj.get("predictedsentiment")
        # 预测结果的置信度分数如果模型支持输出的话

        if mcauthfield_confidencescore["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.confidencescore = obj.get("confidencescore")
        # 预测结果的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_predictions.objects.get(id=obj.get("_id_upd"))

        # 预测结果的唯一标识符

        if mcauthfield_predictionid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.predictionid = str(uuid.uuid4())

            ins_table_busi.predictionid = str(ins_table_busi.predictionid)
        # 关联到被预测的评论对应评论

        if mcauthfield_reviewid["mcauthchange"]:

            # SelectField

            ins_table_busi.reviewid = obj.get("reviewid")
        # 用于做出预测的模型ID关联到模型

        if mcauthfield_modelid["mcauthchange"]:

            # SelectField

            ins_table_busi.modelid = obj.get("modelid")
        # 预测的情感倾向结果

        if mcauthfield_predictedsentiment["mcauthchange"]:

            # CharField

            ins_table_busi.predictedsentiment = obj.get("predictedsentiment")
        # 预测结果的置信度分数如果模型支持输出的话

        if mcauthfield_confidencescore["mcauthchange"]:

            # CharField

            ins_table_busi.confidencescore = obj.get("confidencescore")
        # 预测结果的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_predictions.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_predictions.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/predictions")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_models(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 模型表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模型的唯一标识符

        mcauthfield_modelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的名称或版本信息

        mcauthfield_modelname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用于训练该模型的数据集ID关联到训练数据集

        mcauthfield_trainingdataid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的准确率基于验证集或测试集的评估结果

        mcauthfield_accuracy = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的创建时间训练完成时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的最后更新时间如果有进一步的训练或调整

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 模型表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 模型的唯一标识符

        mcauthfield_modelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的名称或版本信息

        mcauthfield_modelname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用于训练该模型的数据集ID关联到训练数据集

        mcauthfield_trainingdataid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的准确率基于验证集或测试集的评估结果

        mcauthfield_accuracy = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的创建时间训练完成时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 模型的最后更新时间如果有进一步的训练或调整

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_models.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_models().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_models.objects.filter(**filter)
        else:
            records = mc_models.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_trainingdata_18454 = []
        for m in mc_trainingdata.objects.all():
            mobj = m.toJson()
            data_mc_trainingdata_18454.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("usedfortraining"),
                }
            )
        return render(request, "config_busi/models.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_models()

        # 模型的唯一标识符

        if mcauthfield_modelid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.modelid = str(uuid.uuid4())
        # 模型的名称或版本信息

        if mcauthfield_modelname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.modelname = obj.get("modelname")
        # 用于训练该模型的数据集ID关联到训练数据集

        if mcauthfield_trainingdataid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.trainingdataid = obj.get("trainingdataid")
        # 模型的准确率基于验证集或测试集的评估结果

        if mcauthfield_accuracy["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.accuracy = obj.get("accuracy")
        # 模型的创建时间训练完成时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 模型的最后更新时间如果有进一步的训练或调整

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_models.objects.get(id=obj.get("_id_upd"))

        # 模型的唯一标识符

        if mcauthfield_modelid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.modelid = str(uuid.uuid4())

            ins_table_busi.modelid = str(ins_table_busi.modelid)
        # 模型的名称或版本信息

        if mcauthfield_modelname["mcauthchange"]:

            # CharField

            ins_table_busi.modelname = obj.get("modelname")
        # 用于训练该模型的数据集ID关联到训练数据集

        if mcauthfield_trainingdataid["mcauthchange"]:

            # SelectField

            ins_table_busi.trainingdataid = obj.get("trainingdataid")
        # 模型的准确率基于验证集或测试集的评估结果

        if mcauthfield_accuracy["mcauthchange"]:

            # CharField

            ins_table_busi.accuracy = obj.get("accuracy")
        # 模型的创建时间训练完成时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 模型的最后更新时间如果有进一步的训练或调整

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_models.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_models.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/models")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_trainingdata(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 训练数据集表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 训练数据条目的唯一标识符

        mcauthfield_dataid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 训练数据中的评论内容文本

        mcauthfield_reviewcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 情感标签用于监督学习如正面为1负面为0

        mcauthfield_sentimentlabel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 示该数据条目是否已被用于模型训练

        mcauthfield_usedfortraining = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 训练数据集表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 训练数据条目的唯一标识符

        mcauthfield_dataid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 训练数据中的评论内容文本

        mcauthfield_reviewcontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 情感标签用于监督学习如正面为1负面为0

        mcauthfield_sentimentlabel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 示该数据条目是否已被用于模型训练

        mcauthfield_usedfortraining = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_trainingdata.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_trainingdata().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_trainingdata.objects.filter(**filter)
        else:
            records = mc_trainingdata.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/trainingdata.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_trainingdata()

        # 训练数据条目的唯一标识符

        if mcauthfield_dataid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.dataid = str(uuid.uuid4())
        # 训练数据中的评论内容文本

        if mcauthfield_reviewcontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.reviewcontent = obj.get("reviewcontent")
        # 情感标签用于监督学习如正面为1负面为0

        if mcauthfield_sentimentlabel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sentimentlabel = obj.get("sentimentlabel")
        # 示该数据条目是否已被用于模型训练

        if mcauthfield_usedfortraining["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.usedfortraining = obj.get("usedfortraining")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_trainingdata.objects.get(id=obj.get("_id_upd"))

        # 训练数据条目的唯一标识符

        if mcauthfield_dataid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.dataid = str(uuid.uuid4())

            ins_table_busi.dataid = str(ins_table_busi.dataid)
        # 训练数据中的评论内容文本

        if mcauthfield_reviewcontent["mcauthchange"]:

            # TextField

            ins_table_busi.reviewcontent = obj.get("reviewcontent")
        # 情感标签用于监督学习如正面为1负面为0

        if mcauthfield_sentimentlabel["mcauthchange"]:

            # CharField

            ins_table_busi.sentimentlabel = obj.get("sentimentlabel")
        # 示该数据条目是否已被用于模型训练

        if mcauthfield_usedfortraining["mcauthchange"]:

            # BooleanField

            ins_table_busi.usedfortraining = obj.get("usedfortraining")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_trainingdata.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_trainingdata.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/trainingdata")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_reviews(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 评论表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论的唯一标识符

        mcauthfield_reviewid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论者的用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 被评论的电影ID关联到电影

        mcauthfield_movieid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的内容文本

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果

        mcauthfield_sentiment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的最后更新时间如果允许编辑的话

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 评论表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 评论的唯一标识符

        mcauthfield_reviewid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论者的用户ID关联到用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 被评论的电影ID关联到电影

        mcauthfield_movieid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的内容文本

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果

        mcauthfield_sentiment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 评论的最后更新时间如果允许编辑的话

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_reviews.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_reviews().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_reviews.objects.filter(**filter)
        else:
            records = mc_reviews.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_users_18442 = []
        for m in mc_users.objects.all():
            mobj = m.toJson()
            data_mc_users_18442.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_movies_18443 = []
        for m in mc_movies.objects.all():
            mobj = m.toJson()
            data_mc_movies_18443.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("title"),
                }
            )
        return render(request, "config_busi/reviews.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_reviews()

        # 评论的唯一标识符

        if mcauthfield_reviewid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.reviewid = str(uuid.uuid4())
        # 评论者的用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 被评论的电影ID关联到电影

        if mcauthfield_movieid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.movieid = obj.get("movieid")
        # 评论的内容文本

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果

        if mcauthfield_sentiment["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.sentiment = obj.get("sentiment")
        # 评论的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 评论的最后更新时间如果允许编辑的话

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_reviews.objects.get(id=obj.get("_id_upd"))

        # 评论的唯一标识符

        if mcauthfield_reviewid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.reviewid = str(uuid.uuid4())

            ins_table_busi.reviewid = str(ins_table_busi.reviewid)
        # 评论者的用户ID关联到用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 被评论的电影ID关联到电影

        if mcauthfield_movieid["mcauthchange"]:

            # SelectField

            ins_table_busi.movieid = obj.get("movieid")
        # 评论的内容文本

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果

        if mcauthfield_sentiment["mcauthchange"]:

            # TextField

            ins_table_busi.sentiment = obj.get("sentiment")
        # 评论的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 评论的最后更新时间如果允许编辑的话

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_reviews.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_reviews.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/reviews")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_movies(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 电影表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 电影的唯一标识符

        mcauthfield_movieid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的发布日期

        mcauthfield_releasedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的类型如动作、喜剧、剧情等

        mcauthfield_genre = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影导演的名字

        mcauthfield_director = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的主要演员列

        mcauthfield_cast = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的评分可以是用户评分的平均值

        mcauthfield_rating = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 电影表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 电影的唯一标识符

        mcauthfield_movieid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的发布日期

        mcauthfield_releasedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的类型如动作、喜剧、剧情等

        mcauthfield_genre = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影导演的名字

        mcauthfield_director = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的主要演员列

        mcauthfield_cast = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电影的评分可以是用户评分的平均值

        mcauthfield_rating = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_movies.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_movies().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_movies.objects.filter(**filter)
        else:
            records = mc_movies.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/movies.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_movies()

        # 电影的唯一标识符

        if mcauthfield_movieid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.movieid = str(uuid.uuid4())
        # 电影的标题

        if mcauthfield_title["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.title = obj.get("title")
        # 电影的发布日期

        if mcauthfield_releasedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.releasedate = obj.get("releasedate")
        # 电影的类型如动作、喜剧、剧情等

        if mcauthfield_genre["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.genre = obj.get("genre")
        # 电影导演的名字

        if mcauthfield_director["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.director = obj.get("director")
        # 电影的主要演员列

        if mcauthfield_cast["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.cast = obj.get("cast")
        # 电影的评分可以是用户评分的平均值

        if mcauthfield_rating["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.rating = obj.get("rating")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_movies.objects.get(id=obj.get("_id_upd"))

        # 电影的唯一标识符

        if mcauthfield_movieid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.movieid = str(uuid.uuid4())

            ins_table_busi.movieid = str(ins_table_busi.movieid)
        # 电影的标题

        if mcauthfield_title["mcauthchange"]:

            # CharField

            ins_table_busi.title = obj.get("title")
        # 电影的发布日期

        if mcauthfield_releasedate["mcauthchange"]:

            # DateField

            ins_table_busi.releasedate = obj.get("releasedate")
        # 电影的类型如动作、喜剧、剧情等

        if mcauthfield_genre["mcauthchange"]:

            # CharField

            ins_table_busi.genre = obj.get("genre")
        # 电影导演的名字

        if mcauthfield_director["mcauthchange"]:

            # CharField

            ins_table_busi.director = obj.get("director")
        # 电影的主要演员列

        if mcauthfield_cast["mcauthchange"]:

            # CharField

            ins_table_busi.cast = obj.get("cast")
        # 电影的评分可以是用户评分的平均值

        if mcauthfield_rating["mcauthchange"]:

            # IntegerField

            ins_table_busi.rating = obj.get("rating")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_movies.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_movies.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/movies")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_users(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户表 系统管理员(3424)

    if user_table_id == str(3424):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户的唯一标识符

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名用于登录和识别用户

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户的电子邮件地址用于联系和验证用户

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户账户的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户账户的最后更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户表 用户表(3418)

    if user_table_id == str(3418):
        config_user_table = mc_users
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户的唯一标识符

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名用于登录和识别用户

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户的电子邮件地址用于联系和验证用户

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户账户的创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户账户的最后更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_users.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_users().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_users.objects.filter(**filter)
        else:
            records = mc_users.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/users.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_users()

        # 用户的唯一标识符

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 用户名用于登录和识别用户

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 用户的电子邮件地址用于联系和验证用户

        if mcauthfield_email["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 用户账户的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 用户账户的最后更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id_upd"))

        # 用户的唯一标识符

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 用户名用于登录和识别用户

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 用户的电子邮件地址用于联系和验证用户

        if mcauthfield_email["mcauthchange"]:

            # TextField

            ins_table_busi.email = obj.get("email")
        # 用户账户的创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 用户账户的最后更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_users.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/users")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())
