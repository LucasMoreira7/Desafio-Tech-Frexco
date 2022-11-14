from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Users
from .serializers import UsersSerializer
import string as st
import random
import pandas as pd
import sqlite3
import csv
import io
# Create your views here.



def export_users(): ## função para exportar lista de usuários cadastrados do banco
    connection = sqlite3.connect('db.sqlite3')
    c = connection.cursor()
    c.execute("SELECT * FROM myapp_users")
    registeredClients = c.fetchall()
    registeredClients = pd.DataFrame(registeredClients, columns=['id','login','senha','Data de aniversario'])
    connection.commit()
    connection.close()
    return registeredClients

# view para listar usuários cadastrados

@api_view(['GET'])
def usersList(request):
    users = Users.objects.all()
    users_serializer = UsersSerializer(users, many=True)
    if(request.query_params.get('formato') == "JSON"):
        return JsonResponse(users_serializer.data, safe=False)
    elif (request.query_params.get('formato') == "XLSX"):
        df = export_users()
        output = io.BytesIO()
        writer = pd.ExcelWriter(output,engine='xlsxwriter')
        df.to_excel(writer)
        writer.save()
        output.seek(0)
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': 'attachment; filename="UsuariosCadastrados.xlsx"'},
        )
        return response
    elif (request.query_params.get('formato') == "CSV"):  
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="UsuariosCadastrados.csv"'},
    )  
        df = export_users()
        writer = csv.writer(response)
        for index,row in df.iterrows():
            writer.writerow(row)
        return response
    return JsonResponse("Format invalid", safe=False)

# view para criar usuários

@api_view(['POST'])
def createUser(request):  
        user_data = JSONParser().parse(request)
        try : 
            Users.objects.get(login = user_data['login'])
            return JsonResponse('User already exists', safe=False)
        except Users.DoesNotExist:    
            if(user_data['password']==''):    
                aux = random.choices(st.ascii_letters, k=8) 
                aux = ''.join(str(x) for x in aux)
                user_data['password'] = aux
                users_serializer = UsersSerializer(data=user_data)
                if users_serializer.is_valid():
                    users_serializer.save()
                    return JsonResponse({'Password generated':user_data['password']}, safe=False)
            users_serializer = UsersSerializer(data=user_data)
            if users_serializer.is_valid():
                users_serializer.save()
                return JsonResponse('Added successfully', safe=False)
            return JsonResponse("Failed to Add", safe=False)

# view para listar usuário 

@api_view(['GET'])
def getById(request,id):
        user = Users.objects.filter(id = id)
        if not user:
            return JsonResponse("Users not exists", safe=False)
        users_serializer = UsersSerializer(user, many=True)
        return JsonResponse(users_serializer.data, safe=False)
