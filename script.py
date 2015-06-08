#!/usr/bin/env python
# encoding: utf-8
from plotdevice import *

with export("img/test.png") as image:
    size(800, 600)
    background(1)
    text("Welcome to Quotes", 50, 40)
