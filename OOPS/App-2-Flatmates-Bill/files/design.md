# three things to define while starting a new requirement:
title
description
object types

# Title: Flatmate bill generation

# Description: 
An app that gets as input the amount of the bill for a particular period and the days that each of the flatmates 
stayed in the flat for that period and returns how much each flatmate has to pay (split). The app should also generate 
a PDF report that should display
1. flatmate name
2. period
3. contribution

# Object required:

Bill:
    bill amount
    bill period

FlatMate:
    name
    days stayed in house
    pays(bill)

pdf report:
    filename
    generate(flatmate, bill)

