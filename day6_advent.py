#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:44:16 2023

@author: marcinswierczewski
"""

# 1 milisecond holding the button increases boat speed by 1mm/ms

def algo_part1(time_ms: int, distance_mm: int)->int:
    all_strategies = all_times_per_holding_button(time_ms)
    return len([i for i in all_strategies if i > distance_mm])

def distance_for_max_time(max_time: int, button_holding_time: int)->int:
    mm_per_sec = button_holding_time
    time_left = max_time - button_holding_time
    distance = time_left *  mm_per_sec
    return distance

def all_times_per_holding_button(max_time: int)-> list:
    return [distance_for_max_time(max_time, i) for i in range(max_time)]

result = algo_part1(48, 255) * algo_part1(87, 1288)* algo_part1(69, 1117)* algo_part1(81, 1623)


Time:        48876981
Distance:   255128811171623