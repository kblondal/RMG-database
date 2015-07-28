#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Single/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Adsorbate", "Site"], products=["Adsorbed"], ownReverse=False)

reverse = "Surface_Desorption_Single"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1']
])

entry(
    index = 1,
    label = "Adsorbate",
    group = 
"""
1 *1 R u1
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Site",
    group = 
"""
1 *2 X u*
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate

L1: Site
"""
)
