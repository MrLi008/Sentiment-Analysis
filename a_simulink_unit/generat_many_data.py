# coding=utf-8

"""
批量生成模拟数据
可在生成后删除.
"""
from datetime import datetime, timedelta
import os
import codecs
import time
import random

from faker import Faker
# from china_regions.data import provinces, get_cities_by_province, get_districts_by_city
import pandas
import numpy as np
import pandas as pd

def normal(size):
    arr = np.random.normal(size=size+1)
    arr = np.round(arr, decimals=2)
    return arr


def get(faker: Faker, mcfieldnamezh, mctablenamezh=''):
    """
    根据表字段的中文名修正为合适的生成方式
    扩展建议:
    根据字段名->实体名->枚举
    关联字段->同时生成多个字段
    """
    val = ''
    if 'ID' in mcfieldnamezh or '主键' in mcfieldnamezh or '唯一标识' in mcfieldnamezh:
        val = str(faker.uuid4())[:8]
        return val
    if '时间戳' == mcfieldnamezh:
        # val = str(int(time.mktime(faker.date_this_decade().timetuple())))
        # return val
        val = faker.date_between(
            start_date=datetime.now() - timedelta(days=3 * 4), end_date=datetime.now()
        )
        return val

    if '时间' in mcfieldnamezh:
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '日期' in mcfieldnamezh:
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '率' == mcfieldnamezh[-1]:
        val = int(normal(10)[faker.random.randint(0,10)])
        return val
    if '地点' in mcfieldnamezh:
        val = faker.address()
        return val
    # if '类型' in mcfieldnamezh or '类别' in mcfieldnamezh:
    #     val = faker.random.choice((
    #         # 根据文心一言/chatgpt/chatglm生产20个左右的类别即可.
    #     ))
    #     return val

        
    # 系统管理员
    
    # 系统管理员.管理员姓名 <CharField>
    # 
    if mcfieldnamezh == '管理员姓名':
        
        # 载入配置成功
        # 给出一些系统管理员表中管理员姓名的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '管理员姓名1', ' 管理员姓名2','管理员姓名示例1', ' 管理员姓名2',
    ))

        val = loadvalue
        
        return val
    
    
    # 预测结果表
    
    # 预测结果表.预测结果的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '预测结果的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 预测结果表.关联到被预测的评论对应评论 <SelectField>
    # 
    if mcfieldnamezh == '关联到被预测的评论对应评论':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 预测结果表.用于做出预测的模型ID关联到模型 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用于做出预测的模型ID关联到模型':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 预测结果表.预测的情感倾向结果 <CharField>
    # 
    if mcfieldnamezh == '预测的情感倾向结果':
        
        # 载入配置成功
        # 给出一些预测结果表表中预测的情感倾向结果的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '积极', ' 消极', ' 中性', ' 积极', ' 积极', ' 消极', ' 中性', ' 积极', ' 消极', ' 中性', ' 积极', ' 中性', ' 消极', ' 积极', ' 中性', ' 消极', ' 积极', ' 中性', ' 消极', ' 积极',
    ))

        val = loadvalue
        
        return val
    
    # 预测结果表.预测结果的置信度分数如果模型支持输出的话 <CharField>
    # 
    if mcfieldnamezh == '预测结果的置信度分数如果模型支持输出的话':
        
        # 载入配置成功
        # 给出一些预测结果表表中预测结果的置信度分数如果模型支持输出的话的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '0.9876543210', ' 0.8765432109', ' 0.7654321098', ' 0.6543210987', ' 0.5432109876','0.9543210987', ' 0.8432109876', ' 0.7321098765', ' 0.6210987654', ' 0.5109876543','0.9012345678', ' 0.8901234567', ' 0.7890123456', ' 0.6789012345', ' 0.5678901234','0.9321098765', ' 0.8210987654', ' 0.7109876543', ' 0.6098765432', ' 0.5987654321',
    ))

        val = loadvalue
        
        return val
    
    # 预测结果表.预测结果的创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '预测结果的创建时间':
        
        # 载入配置成功
        # 给出一些预测结果表表中预测结果的创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 15:30:00', ' 2023-10-24 09:15:45', ' 2023-10-25 12:00:00',
    ))

        val = loadvalue
        
        return val
    
    
    # 模型表
    
    # 模型表.模型的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '模型的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 模型表.模型的名称或版本信息 <CharField>
    # 
    if mcfieldnamezh == '模型的名称或版本信息':
        
        # 载入配置成功
        # 给出一些模型表表中模型的名称或版本信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'ModelA_v1.0', ' ModelB_2.2', ' Version3_of_ModelC', ' ModelD_v4.1', ' ModelE_Release5','ModelF_6.0_Stable', ' Version7_for_ModelG', ' HModel_v8.3', ' ModelI_9.0_Beta', ' Version10_JModel','KModel_v11.1', ' ModelL_12.2_RC', ' Version13_for_ModelM', ' ModelN_v14.0_Patch1', ' OModel_v15.5','Version16_of_ModelP', ' ModelQ_v17.3_Final', ' ModelR_18.0_Gold', ' Version19_for_ModelS', ' TModel_v20.1'
    ))

        val = loadvalue
        
        return val
    
    # 模型表.用于训练该模型的数据集ID关联到训练数据集 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用于训练该模型的数据集ID关联到训练数据集':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 模型表.模型的准确率基于验证集或测试集的评估结果 <CharField>
    # 
    if mcfieldnamezh == '模型的准确率基于验证集或测试集的评估结果':
        
        # 载入配置成功
        # 给出一些模型表表中模型的准确率基于验证集或测试集的评估结果的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '验证集准确率1: 90.5%', ' 验证集准确率2: 89.2%', ' 测试集准确率1: 91.3%', ' 测试集准确率2: 90.8%', ' 测试集准确率3: 91.1%', ' 测试集准确率4: 90.6%', ' 测试集准确率5: 90.9%', ' 测试集准确率6: 91.5%', ' 测试集准确率7: 90.7%', ' 测试集准确率8: 91.0%', ' 测试集准确率9: 90.4%', ' 测试集准确率10: 91.2%', ' 测试集准确率11: 90.1%', ' 测试集准确率12: 91.4%', ' 测试集准确率13: 90.3%', ' 测试集准确率14: 91.6%', ' 测试集准确率15: 90.2%', ' 测试集准确率16: 91.7%', ' 测试集准确率17: 90.0%', ' 测试集准确率18: 91.8%', ' 测试集准确率19: 90.5%', ' 测试集准确率20: 91.9%',
    ))

        val = loadvalue
        
        return val
    
    # 模型表.模型的创建时间训练完成时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '模型的创建时间训练完成时间':
        
        # 载入配置成功
        # 给出一些模型表表中模型的创建时间训练完成时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '(2023-10-23 10:00:00', ' 2023-10-23 14:30:00)','(2023-10-23 10:00:00', ' 2023-10-23 14:30:00)','(2023-10-24 09:15:00', ' 2023-10-24 13:45:00)','(2023-10-25 11:30:00', ' 2023-10-25 16:00:00)','... （其他时间戳）'
    ))

        val = loadvalue
        
        return val
    
    # 模型表.模型的最后更新时间如果有进一步的训练或调整 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '模型的最后更新时间如果有进一步的训练或调整':
        
        # 载入配置成功
        # 给出一些模型表表中模型的最后更新时间如果有进一步的训练或调整的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    
    ))

        val = loadvalue
        
        return val
    
    
    # 训练数据集表
    
    # 训练数据集表.训练数据条目的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '训练数据条目的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 训练数据集表.训练数据中的评论内容文本 <TextField>
    # 
    if mcfieldnamezh == '训练数据中的评论内容文本':
        
        # 载入配置成功
        # 给出一些训练数据集表表中训练数据中的评论内容文本的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的产品', ' 我强烈推荐给所有人', ' 服务非常棒', ' 质量超乎想象', ' 下次还会再来', ' 价格公道', ' 发货速度快', ' 包装很安全', ' 非常满意这次的购物体验', ' 商品与描述相符', ' 客服态度很好', ' 解决了我的问题', ' 使用起来很方便', ' 颜色很漂亮', ' 大小合适', ' 质量上乘', ' 值得购买', ' 已经推荐给朋友了', ' 期待下次合作', ' 感谢卖家',
    ))

        val = loadvalue
        
        return val
    
    # 训练数据集表.情感标签用于监督学习如正面为1负面为0 <CharField>
    # 
    if mcfieldnamezh == '情感标签用于监督学习如正面为1负面为0':
        
        # 载入配置成功
        # 给出一些训练数据集表表中情感标签用于监督学习如正面为1负面为0的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0',
    ))

        val = loadvalue
        
        return val
    
    # 训练数据集表.示该数据条目是否已被用于模型训练 <BooleanField>
    # 
    if mcfieldnamezh == '示该数据条目是否已被用于模型训练':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 评论表
    
    # 评论表.评论的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '评论的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 评论表.评论者的用户ID关联到用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '评论者的用户ID关联到用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 评论表.被评论的电影ID关联到电影 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '被评论的电影ID关联到电影':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 评论表.评论的内容文本 <TextField>
    # 
    if mcfieldnamezh == '评论的内容文本':
        
        # 载入配置成功
        # 给出一些评论表表中评论的内容文本的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的产品，强烈推荐！', '服务很周到，下次还会再来', '产品质量不错，性价比高', '发货速度快，包装也很好', '非常满意这次的购物体验', '希望下次能有更多的优惠活动', '商品质量超乎想象，非常满意', '客服态度很好，解决问题迅速', '物流很快，两天就到了', '非常满意这次的购物，会继续支持', '商品与描述相符，没有失望', '已经多次购买，值得信赖', '推荐给身边的朋友了，都说好', '会继续关注这家店，期待新品', '下次还会选择这家店购买', '性价比超高，物超所值', '包装精美，送礼自用两相宜', '发货迅速，包装严实', '商品质量有保障，值得信赖', '期待下次购物，谢谢！',
    ))

        val = loadvalue
        
        return val
    
    # 评论表.评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果 <TextField>
    # 
    if mcfieldnamezh == '评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果':
        
        # 载入配置成功
        # 给出一些评论表表中评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '正面', ' 负面', ' 中立', ' 正面', ' 负面', ' 中立', ' 正面', ' 中立', ' 负面', ' 中立', ' 正面', ' 负面', ' 中立', ' 正面', ' 中立', ' 负面', ' 正面', ' 中立', ' 负面', ' 中立',
    ))

        val = loadvalue
        
        return val
    
    # 评论表.评论的创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '评论的创建时间':
        
        # 载入配置成功
        # 给出一些评论表表中评论的创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 10:00:00', ' 2023-10-23 10:05:15', ' 2023-10-23 10:10:30', ' 2023-10-23 10:15:45', ' 2023-10-23 10:20:00', ' 2023-10-23 10:25:15', ' 2023-10-23 10:30:30', ' 2023-10-23 10:35:45', ' 2023-10-23 10:40:00', ' 2023-10-23 10:45:15', ' 2023-10-23 10:50:30', ' 2023-10-23 10:55:45', ' 2023-10-23 11:00:00', ' 2023-10-23 11:05:15', ' 2023-10-23 11:10:30', ' 2023-10-23 11:15:45', ' 2023-10-23 11:20:00', ' 2023-10-23 11:25:15', ' 2023-10-23 11:30:30', ' 2023-10-23 11:35:45',
    ))

        val = loadvalue
        
        return val
    
    # 评论表.评论的最后更新时间如果允许编辑的话 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '评论的最后更新时间如果允许编辑的话':
        
        # 载入配置成功
        # 给出一些评论表表中评论的最后更新时间如果允许编辑的话的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 15:45:30','UPDATE your_table_name SET last_comment_update_time = 2023-10-23 15:45:30 WHERE some_condition;'
    ))

        val = loadvalue
        
        return val
    
    
    # 电影表
    
    # 电影表.电影的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '电影的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 电影表.电影的标题 <CharField>
    # 
    if mcfieldnamezh == '电影的标题':
        
        # 载入配置成功
        # 给出一些电影表表中电影的标题的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '电影标题1', ' 电影标题2', ' 电影标题3', ' 电影标题4', ' 电影标题5', ' 电影标题6', ' 电影标题7', ' 电影标题8', ' 电影标题9', ' 电影标题10', ' 电影标题11', ' 电影标题12', ' 电影标题13', ' 电影标题14', ' 电影标题15', ' 电影标题16', ' 电影标题17', ' 电影标题18', ' 电影标题19', ' 电影标题20',
    ))

        val = loadvalue
        
        return val
    
    # 电影表.电影的发布日期 <DateField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '电影的发布日期':
        
        # 载入配置成功
        # 给出一些电影表表中电影的发布日期的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-01-01', ' 2023-01-15', ' 2023-02-14', ' 2023-03-08', ' 2023-04-01','2023-05-05', ' 2023-06-20', ' 2023-07-04', ' 2023-08-15', ' 2023-09-09','2023-10-10', ' 2023-11-11', ' 2023-12-24', ' 2022-12-31', ' 2022-11-22','2022-10-18', ' 2022-09-05', ' 2022-08-08', ' 2022-07-07', ' 2022-06-16'
    ))

        val = loadvalue
        
        return val
    
    # 电影表.电影的类型如动作、喜剧、剧情等 <CharField>
    # 
    if mcfieldnamezh == '电影的类型如动作、喜剧、剧情等':
        
        # 载入配置成功
        # 给出一些电影表表中电影的类型如动作、喜剧、剧情等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '动作', ' 喜剧', ' 剧情', ' 科幻', ' 恐怖', ' 奇幻', ' 冒险', ' 动画', ' 犯罪', ' 传记', ' 历史', ' 战争', ' 悬疑', ' 惊悚', ' 音乐', ' 家庭', ' 爱情', ' 西部', ' 体育', ' 纪录片'
    ))

        val = loadvalue
        
        return val
    
    # 电影表.电影导演的名字 <CharField>
    # 
    if mcfieldnamezh == '电影导演的名字':
        
        # 载入配置成功
        # 给出一些电影表表中电影导演的名字的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '张艺谋', '陈凯歌', '姜文', '贾樟柯', '宁浩', '王小帅', '娄烨', '徐克', '王家卫', '冯小刚', '管虎', '陆川', '吴宇森', '杜琪峰', '许鞍华', '侯孝贤', '蔡明亮', '陈可辛', '忻钰坤', '田壮壮',
    ))

        val = loadvalue
        
        return val
    
    # 电影表.电影的主要演员列 <CharField>
    # 
    if mcfieldnamezh == '电影的主要演员列':
        
        # 载入配置成功
        # 给出一些电影表表中电影的主要演员列的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '演员A', ' 演员B', ' 演员C', ' 演员D', ' 演员E', ' 演员F', ' 演员G', ' 演员H', ' 演员I', ' 演员J', ' 演员K', ' 演员L', ' 演员M', ' 演员N', ' 演员O', ' 演员P', ' 演员Q', ' 演员R', ' 演员S', ' 演员T','INSERT INTO movies (main_actors) VALUES (演员A', ' 演员B', ' 演员C', ' 演员D', ' 演员E', ' 演员F', ' 演员G', ' 演员H', ' 演员I', ' 演员J', ' 演员K', ' 演员L', ' 演员M', ' 演员N', ' 演员O', ' 演员P', ' 演员Q', ' 演员R', ' 演员S', ' 演员T);'
    ))

        val = loadvalue
        
        return val
    
    # 电影表.电影的评分可以是用户评分的平均值 <IntegerField>
    # 
    if mcfieldnamezh == '电影的评分可以是用户评分的平均值':
        
        # 载入配置成功
        # 给出一些电影表表中电影的评分可以是用户评分的平均值的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    1,2,3,4,5
    ))

        val = loadvalue
        
        return val
    
    
    # 用户表
    
    # 用户表.用户的唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '用户的唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户表.用户名用于登录和识别用户 <CharField>
    # 
    if mcfieldnamezh == '用户名用于登录和识别用户':
        
        # 载入配置成功
        # 给出一些用户表表中用户名用于登录和识别用户的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'user1', ' user2', ' user3', ' user4', ' user5', ' user6', ' user7', ' user8', ' user9', ' user10', ' user11', ' user12', ' user13', 'SELECT * FROM users WHERE username IN (user1', ' user2', ' user3', ' user4', ' user5', ' user6', ' user7', ' user8', ' user9', ' user10', ' user11', ' user12', ' user13', ' user14', ' user15', ' user16', ' user17);'
    ))

        val = loadvalue
        
        return val
    
    # 用户表.用户的电子邮件地址用于联系和验证用户 <TextField>
    # 
    if mcfieldnamezh == '用户的电子邮件地址用于联系和验证用户':
        
        # 载入配置成功
        # 给出一些用户表表中用户的电子邮件地址用于联系和验证用户的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'user1@example.com', ' user2@example.com','user1@example.net', ' user2@example.org', ' user3@example.com',
    ))

        val = loadvalue
        
        return val
    
    # 用户表.用户账户的创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户账户的创建时间':
        
        # 载入配置成功
        # 给出一些用户表表中用户账户的创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-07-19T08:00:00Z', ' 2023-07-19T09:15:30Z', ' 2023-07-19T12:45:10Z', ' 2023-07-19T15:30:00Z', ' 2023-07-19T18:15:45Z', ' 2023-07-19T21:00:00Z', ' 2023-07-20T00:30:15Z', ' 2023-07-20T03:15:00Z', ' 2023-07-20T06:00:00Z', ' 2023-07-20T08:45:30Z', ' 2023-07-20T11:30:15Z', ' 2023-07-20T14:15:00Z', ' 2023-07-20T17:00:00Z', ' 2023-07-20T19:45:15Z', ' 2023-07-20T22:30:00Z', ' 2023-07-21T01:15:00Z', ' 2023-07-21T04:00:00Z', ' 2023-07-21T06:45:30Z', ' 2023-07-21T09:30:15Z', ' 2023-07-21T12:15:00Z',
    ))

        val = loadvalue
        
        return val
    
    # 用户表.用户账户的最后更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户账户的最后更新时间':
        
        # 载入配置成功
        # 给出一些用户表表中用户账户的最后更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 15:45:30',
    ))

        val = loadvalue
        
        return val
    
    
    return val




# 系统管理员
def generate_supermanager(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='supermanager'
    fields_en = ['`username`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 管理员姓名 根据名称选择合适的函数来生成数据
        username = get(faker,'管理员姓名')
        values.append('\''+str(username)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 预测结果表
def generate_predictions(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='predictions'
    fields_en = ['`predictionid`', '`reviewid`', '`modelid`', '`predictedsentiment`', '`confidencescore`', '`createdat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 预测结果的唯一标识符 根据名称选择合适的函数来生成数据
        predictionid = get(faker,'预测结果的唯一标识符')
        values.append('\''+str(predictionid)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联到被预测的评论对应评论' not in cache:
            reviewid = get(faker,'关联到被预测的评论对应评论')
        else:
            reviewid = faker.random.choice(list(cache.get('关联到被预测的评论对应评论', )))
        
        # 用于外键补充
        
        if '关联到被预测的评论对应评论' not in cache:
            cache['关联到被预测的评论对应评论'] = set()
        cache['关联到被预测的评论对应评论'].add(reviewid)
        values.append('\''+str(reviewid)+'\'')
        
        
        
        if '用于做出预测的模型ID关联到模型' not in cache:
            modelid = get(faker,'用于做出预测的模型ID关联到模型')
        else:
            modelid = faker.random.choice(list(cache.get('用于做出预测的模型ID关联到模型', )))
        
        # 用于外键补充
        
        if '用于做出预测的模型ID关联到模型' not in cache:
            cache['用于做出预测的模型ID关联到模型'] = set()
        cache['用于做出预测的模型ID关联到模型'].add(modelid)
        values.append('\''+str(modelid)+'\'')
        
        
        
        # 预测的情感倾向结果 根据名称选择合适的函数来生成数据
        predictedsentiment = get(faker,'预测的情感倾向结果')
        values.append('\''+str(predictedsentiment)+'\'')
        
        # 用于外键补充
        
        
        
        # 预测结果的置信度分数如果模型支持输出的话 根据名称选择合适的函数来生成数据
        confidencescore = get(faker,'预测结果的置信度分数如果模型支持输出的话')
        values.append('\''+str(confidencescore)+'\'')
        
        # 用于外键补充
        
        
        
        # 预测结果的创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'预测结果的创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 模型表
def generate_models(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='models'
    fields_en = ['`modelid`', '`modelname`', '`trainingdataid`', '`accuracy`', '`createdat`', '`updatedat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 模型的唯一标识符 根据名称选择合适的函数来生成数据
        modelid = get(faker,'模型的唯一标识符')
        values.append('\''+str(modelid)+'\'')
        
        # 用于外键补充
        
        
        
        # 模型的名称或版本信息 根据名称选择合适的函数来生成数据
        modelname = get(faker,'模型的名称或版本信息')
        values.append('\''+str(modelname)+'\'')
        
        # 用于外键补充
        
        
        
        if '用于训练该模型的数据集ID关联到训练数据集' not in cache:
            trainingdataid = get(faker,'用于训练该模型的数据集ID关联到训练数据集')
        else:
            trainingdataid = faker.random.choice(list(cache.get('用于训练该模型的数据集ID关联到训练数据集', )))
        
        # 用于外键补充
        
        if '用于训练该模型的数据集ID关联到训练数据集' not in cache:
            cache['用于训练该模型的数据集ID关联到训练数据集'] = set()
        cache['用于训练该模型的数据集ID关联到训练数据集'].add(trainingdataid)
        values.append('\''+str(trainingdataid)+'\'')
        
        
        
        # 模型的准确率基于验证集或测试集的评估结果 根据名称选择合适的函数来生成数据
        accuracy = get(faker,'模型的准确率基于验证集或测试集的评估结果')
        values.append('\''+str(accuracy)+'\'')
        
        # 用于外键补充
        
        
        
        # 模型的创建时间训练完成时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'模型的创建时间训练完成时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 模型的最后更新时间如果有进一步的训练或调整 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'模型的最后更新时间如果有进一步的训练或调整')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 训练数据集表
def generate_trainingdata(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='trainingdata'
    fields_en = ['`dataid`', '`reviewcontent`', '`sentimentlabel`', '`usedfortraining`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 训练数据条目的唯一标识符 根据名称选择合适的函数来生成数据
        dataid = get(faker,'训练数据条目的唯一标识符')
        values.append('\''+str(dataid)+'\'')
        
        # 用于外键补充
        
        
        
        # 训练数据中的评论内容文本 根据名称选择合适的函数来生成数据
        reviewcontent = get(faker,'训练数据中的评论内容文本')
        values.append('\''+str(reviewcontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 情感标签用于监督学习如正面为1负面为0 根据名称选择合适的函数来生成数据
        sentimentlabel = get(faker,'情感标签用于监督学习如正面为1负面为0')
        values.append('\''+str(sentimentlabel)+'\'')
        
        # 用于外键补充
        
        
        
        # 示该数据条目是否已被用于模型训练 根据名称选择合适的函数来生成数据
        usedfortraining = get(faker,'示该数据条目是否已被用于模型训练')
        values.append('\''+str(usedfortraining)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 评论表
def generate_reviews(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='reviews'
    fields_en = ['`reviewid`', '`userid`', '`movieid`', '`content`', '`sentiment`', '`createdat`', '`updatedat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 评论的唯一标识符 根据名称选择合适的函数来生成数据
        reviewid = get(faker,'评论的唯一标识符')
        values.append('\''+str(reviewid)+'\'')
        
        # 用于外键补充
        
        
        
        if '评论者的用户ID关联到用户' not in cache:
            userid = get(faker,'评论者的用户ID关联到用户')
        else:
            userid = faker.random.choice(list(cache.get('评论者的用户ID关联到用户', )))
        
        # 用于外键补充
        
        if '评论者的用户ID关联到用户' not in cache:
            cache['评论者的用户ID关联到用户'] = set()
        cache['评论者的用户ID关联到用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        if '被评论的电影ID关联到电影' not in cache:
            movieid = get(faker,'被评论的电影ID关联到电影')
        else:
            movieid = faker.random.choice(list(cache.get('被评论的电影ID关联到电影', )))
        
        # 用于外键补充
        
        if '被评论的电影ID关联到电影' not in cache:
            cache['被评论的电影ID关联到电影'] = set()
        cache['被评论的电影ID关联到电影'].add(movieid)
        values.append('\''+str(movieid)+'\'')
        
        
        
        # 评论的内容文本 根据名称选择合适的函数来生成数据
        content = get(faker,'评论的内容文本')
        values.append('\''+str(content)+'\'')
        
        # 用于外键补充
        
        
        
        # 评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果 根据名称选择合适的函数来生成数据
        sentiment = get(faker,'评论的情感倾向如正面、负面或中立这可以是机器学习模型预测的结果')
        values.append('\''+str(sentiment)+'\'')
        
        # 用于外键补充
        
        
        
        # 评论的创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'评论的创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 评论的最后更新时间如果允许编辑的话 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'评论的最后更新时间如果允许编辑的话')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 电影表
def generate_movies(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='movies'
    fields_en = ['`movieid`', '`title`', '`releasedate`', '`genre`', '`director`', '`cast`', '`rating`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 电影的唯一标识符 根据名称选择合适的函数来生成数据
        movieid = get(faker,'电影的唯一标识符')
        values.append('\''+str(movieid)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影的标题 根据名称选择合适的函数来生成数据
        title = get(faker,'电影的标题')
        values.append('\''+str(title)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影的发布日期 根据名称选择合适的函数来生成数据
        releasedate = get(faker,'电影的发布日期')
        values.append('\''+str(releasedate)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影的类型如动作、喜剧、剧情等 根据名称选择合适的函数来生成数据
        genre = get(faker,'电影的类型如动作、喜剧、剧情等')
        values.append('\''+str(genre)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影导演的名字 根据名称选择合适的函数来生成数据
        director = get(faker,'电影导演的名字')
        values.append('\''+str(director)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影的主要演员列 根据名称选择合适的函数来生成数据
        cast = get(faker,'电影的主要演员列')
        values.append('\''+str(cast)+'\'')
        
        # 用于外键补充
        
        
        
        # 电影的评分可以是用户评分的平均值 根据名称选择合适的函数来生成数据
        rating = get(faker,'电影的评分可以是用户评分的平均值')
        values.append('\''+str(rating)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 用户表
def generate_users(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='users'
    fields_en = ['`userid`', '`username`', '`email`', '`createdat`', '`updatedat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 用户的唯一标识符 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户的唯一标识符')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户名用于登录和识别用户 根据名称选择合适的函数来生成数据
        username = get(faker,'用户名用于登录和识别用户')
        values.append('\''+str(username)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户的电子邮件地址用于联系和验证用户 根据名称选择合适的函数来生成数据
        email = get(faker,'用户的电子邮件地址用于联系和验证用户')
        values.append('\''+str(email)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户账户的创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'用户账户的创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户账户的最后更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'用户账户的最后更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache


def generate():
    cache = dict()
    with codecs.open('faker.sql', 'w', encoding='utf-8') as out:
        sql = 'insert into {databasename}.{table} ({fields_en}) values({values});\r\n'
        faker = Faker('zh_CN')
        database = 'vm432_bf0a45f882b27e8f'
        # 表名字符串,字段英文名

            
        # 系统管理员
        cache.update(generate_supermanager(faker, sql, out, database,cache=cache))
        
        # 预测结果表
        cache.update(generate_predictions(faker, sql, out, database,cache=cache))
        
        # 模型表
        cache.update(generate_models(faker, sql, out, database,cache=cache))
        
        # 训练数据集表
        cache.update(generate_trainingdata(faker, sql, out, database,cache=cache))
        
        # 评论表
        cache.update(generate_reviews(faker, sql, out, database,cache=cache))
        
        # 电影表
        cache.update(generate_movies(faker, sql, out, database,cache=cache))
        
        # 用户表
        cache.update(generate_users(faker, sql, out, database,cache=cache))
        

    from pymysql.connections import Connection
    from pymysql.cursors import DictCursor
    conn = Connection(port=3306, host='localhost', user='root', password=os.getenv('PM_UNIT_DATABASE_PSW', '123456'),
                      database='vm432_bf0a45f882b27e8f')
    with codecs.open('faker.sql', 'r', encoding='utf-8') as ins:
        with conn.cursor(DictCursor) as cursor:
            count = 0
            for i, sql in enumerate(ins.readlines()):
                try:
                    cursor.execute(sql)
                    cursor.fetchall()
                except Exception as e:
                    print('error: ', e)
                    print(sql)
                    continue
                count += 1
                    
        conn.commit()
        print('Generate OK,Insert Total:', count, '个记录', i+1, '个sql')
    os.remove('faker.sql')


if __name__ == '__main__':
    generate()

