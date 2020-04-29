# importações
from flask import Flask, jsonify, request # preparar resposta HTTP no formato json
import json # ajusta conteúdo json (ex: troca aspas simples para duplas)
import os

# configurações
app = Flask(__name__)