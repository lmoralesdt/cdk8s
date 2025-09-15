#!/usr/bin/env python
from cdk8s import App
from deployment_template import MyChart

# Variables you want to inject
APP_LABEL = "payment-service"
IMAGE = "nginx:1.25.2"
REPLICAS = 2

app = App()
MyChart(app, "payment-chart", app_label=APP_LABEL, replicas=REPLICAS, image=IMAGE)

app.synth()
