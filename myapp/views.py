# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='./logs/myapp.log', filemode='a', format='%(levelname)s %(message)s')


def index(request):
    logger.info("Root page ")
    return HttpResponse("<div > <h1> Вы попали на мою первый Django сайт! </h1> <h2>Добро пожаловать!</h2></div> <h3>About  даст инфомацию обо мне</h>")


def about(request):
    logger.info('About page accessed')
    return HttpResponse("<div > <h2> Меня зовут Ирина </h2><h3>Я живу в Краснодаре</h3> <h3> Я изучаю Python в GeekBrains</h3></div>")