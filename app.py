import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder='layouts')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

