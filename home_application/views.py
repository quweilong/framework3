# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import json
import requests
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
import time, datetime
import re
from common.mymako import render_mako_context
from .models import UserInfo


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def home_page(request):
    return render_mako_context(request, '/home_application/index.html')

def save_info(request):
    results = request.POST
    if results['editId'] != '':
        UserInfo.objects.filter(id=results['editId']).update(user_name=results['name'],phone=results['phone'],education_background=results['xl'],
                                  professional=results['zhuanye'],working_years=results['nianxian'],jobs=results['gangwei'],
                                  specialty=results['tecahgn'],source=results['laiyuan'],use_department=results['usedepartment'],
                                  convention_interview_date=results['mianshiqiqi'],keep_situation=results['shouyue'],
                                  the_interviewer=results['mianshirenyaun'],use_department_score=results['bumendafen'],
                                  hr_score=results['hrdafen'],employment_status=results['luyongzhuangtai'],work_time=results['daogangshijain'],
                                  use_department_bk=results['bmbz'],hr_bk=results['hrbz'],bk=results['bz'])
    else:
        obj = UserInfo.objects.create(user_name=results['name'],phone=results['phone'],education_background=results['xl'],
                                      professional=results['zhuanye'],working_years=results['nianxian'],jobs=results['gangwei'],
                                      specialty=results['tecahgn'],source=results['laiyuan'],use_department=results['usedepartment'],
                                      convention_interview_date=results['mianshiqiqi'],keep_situation=results['shouyue'],
                                      the_interviewer=results['mianshirenyaun'],use_department_score=results['bumendafen'],
                                      hr_score=results['hrdafen'],employment_status=results['luyongzhuangtai'],work_time=results['daogangshijain'],
                                      use_department_bk=results['bmbz'],hr_bk=results['hrbz'],bk=results['bz'])
        obj.save()
    return HttpResponse({})

def all_info(request):
    return render_mako_context(request, '/home_application/details.html')
def get_list(request):
    return render_mako_context(request, '/home_application/list.html')

def get_profile_information(request):
    objs = UserInfo.objects.all()
    all_list = []
    for obj in objs:
        dict ={}
        dict['id'] = obj.id
        dict['user_name'] = obj.user_name
        dict['phone'] = obj.phone
        dict['jobs'] = obj.jobs
        dict['use_department'] = obj.use_department
        dict['use_department_score'] = obj.use_department_score
        dict['employment_status'] = obj.employment_status
        all_list.append(dict)
    return HttpResponse(json.dumps(all_list, ensure_ascii=False), content_type="application/json,charset=utf-8")
def delInfo(request):
    id = request.POST['id']
    UserInfo.objects.filter(id=id).delete()
    return HttpResponse(json.dumps({}, ensure_ascii=False), content_type="application/json,charset=utf-8")

def getEditInfo(request):
    id = request.POST['id']
    obj = UserInfo.objects.get(id=id)
    dict = {}
    dict['id'] = obj.id
    dict['resume_date'] = obj.resume_date
    dict['user_name'] = obj.user_name
    dict['phone'] = obj.phone
    dict['education_background'] = obj.education_background
    dict['professional'] = obj.professional
    dict['working_years'] = obj.working_years
    dict['specialty'] = obj.specialty
    dict['jobs'] = obj.jobs
    dict['source'] = obj.source
    dict['use_department'] = obj.use_department
    dict['convention_interview_date'] = obj.convention_interview_date
    dict['keep_situation'] = obj.keep_situation
    dict['the_interviewer'] = obj.the_interviewer
    dict['use_department_score'] = obj.use_department_score
    dict['hr_score'] = obj.hr_score
    dict['employment_status'] = obj.employment_status
    dict['work_time'] = obj.work_time
    dict['hr_bk'] = obj.hr_bk
    dict['bk'] = obj.bk
    return HttpResponse(json.dumps(dict, ensure_ascii=False), content_type="application/json,charset=utf-8")




