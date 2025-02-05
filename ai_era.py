from flask import Flask, render_template, jsonify
import random
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.patches import ConnectionPatch
import numpy as np




fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

#pie chart parameters
overall_ratios = [.27,.56,.17]
labels = ["Adaptable People", "Colleague Support", "Career Vision Support"]
explode= [0.1,0, 0]

#rotate so that first wedge us split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_= ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,labels=labels,explode=explode)

#bar chart parameters
age_ratio = [.18,.25,.45,.26]
age_label = ['<35', '35-49',50-66,'>65']
bottom = 1
width =.2

#adding from the top matches the legend
for j, (height, label) in enumerate(reversed([*zip(age_ratio,age_label)])):
    bottom -= height
    bc = ax2.bar(0,height,width, bottom=bottom, color='C0',label=label,alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"],label_type='center')
   
ax2.set_title('AI IN MODERN ERA BASED ON JOB NEEDS')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(-2.5 * width, 2.5 * width)

#use connection patch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratio)

#draw the connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,xyB=(x,y),coordsB=ax1.transData)

con.set_color([0,0,0])
con.set_linewidth(4)
ax2.add_artist(con)

#draw bottom connecting line
x = r* np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,xyB=(x,y),coordsB=ax1.transData)

con.set_color([0,0,0])
con.set_linewidth(4)

ax2.add_artist(con)
plt.show()
   
   