#!/usr/bin/env python3
###############################################################################
# Name:     muTS (Microscopic Traffic Simulator)
# Purpose:  This script implements a microscopic traffic simulator.
# Author:   Huidae Cho
# GitHub:   https://github.com/HuidaeCho/muTS
# Since:    August 1, 2022
#
# Copyright (C) 2022 Huidae Cho <https://idea.isnew.info/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
###############################################################################

import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xlim_min = ylim_min = 0
xlim_max = ylim_max = 256 # miles
dt = 60 # seconds
cars_per_day = 100
speed_limit = 60 # mph
roads_coors = [[xlim_min, xlim_max], [ylim_min, ylim_max]]
scale = 1
car_size = 5

def calc_coors(along_dist):
    xs, ys = roads_coors
    if along_dist < 0:
        prev_x = xs[0]
        prev_y = ys[0]
        curr_x = xs[1]
        curr_y = ys[1]
        dist = math.sqrt((curr_x - prev_x)**2 + (curr_y - prev_y)**2) * scale
        x = prev_x + (curr_x - prev_x) / dist * along_dist
        y = prev_y + (curr_y - prev_y) / dist * along_dist
    elif along_dist == 0:
        x, y = xs[0], ys[0]
    else:
        total_dist = 0
        n = len(xs)
        found = False
        for i in range(1, n):
            prev_x = xs[i-1]
            prev_y = ys[i-1]
            curr_x = xs[i]
            curr_y = ys[i]
            dist = math.sqrt((curr_x - prev_x)**2 + (curr_y - prev_y)**2) * scale
            if along_dist == total_dist + dist:
                x, y = curr_x, curr_y
                found = True
                break
            elif along_dist < total_dist + dist:
                delta_dist = along_dist - total_dist
                x = prev_x + (curr_x - prev_x) / dist * delta_dist
                y = prev_y + (curr_y - prev_y) / dist * delta_dist
                found = True
                break
            total_dist += dist
        if not found:
            if along_dist == total_dist:
                x, y = xs[n-1], ys[n-1]
            elif along_dist > total_dist:
                prev_x = xs[n-2]
                prev_y = ys[n-2]
                curr_x = xs[n-1]
                curr_y = ys[n-1]
                total_dist -= dist
                dist = math.sqrt((curr_x - prev_x)**2 + (curr_y - prev_y)**2) * scale
                delta_dist = along_dist - total_dist
                x = prev_x + (curr_x - prev_x) / dist * delta_dist
                y = prev_y + (curr_y - prev_y) / dist * delta_dist
    return x, y

cars_per_dt = cars_per_day / 86400 * dt
dist_per_dt = speed_limit / 3600 * dt

fig = plt.figure()
ax = plt.axes(xlim=(xlim_min, xlim_max), ylim=(ylim_min, ylim_max))
ax.set_aspect("equal")
ax.axis("off")

objs = []
roads_obj, = ax.plot([], [], color="gray", linewidth=1)
objs.append(roads_obj)
car_objs = []
car_dists = []
for i in range(cars_per_day):
    car_dist = -car_size
    car_dists.append(car_dist)
    car_obj = plt.Circle(calc_coors(car_dist), car_size)
    car_objs.append(car_obj)
    objs.append(car_obj)
wait_ticks = 0
delta_ticks = 0
total_lapse = 0
last_idx = 0

def init():
    roads_obj.set_data(roads_coors[0], roads_coors[1])
    for car_obj in car_objs:
        ax.add_patch(car_obj)
    return objs

def update(tick):
    global wait_ticks, delta_ticks, total_lapse, last_idx

    if wait_ticks <= 0:
        for last_idx in range(len(car_dists)):
            if car_dists[last_idx] < 0:
                car_dists[last_idx] = 0
                car_objs[last_idx].center = calc_coors(car_dists[last_idx])
                break

        wait_ticks = delta_ticks = -math.log(random.random()) / cars_per_dt
    else:
        for i in range(last_idx+1):
            car_dists[i] += dist_per_dt #* abs(wait_ticks if wait_ticks < 1 else 1)
            car_objs[i].center = calc_coors(car_dists[i])

        wait_ticks -= 1
    total_lapse += dt

    print("====", tick, "====", wait_ticks, delta_ticks, total_lapse, cars_per_dt)

    return objs

anim = FuncAnimation(fig, update, init_func=init, blit=True, interval=1)
plt.show()
