#!/usr/bin/env python
# encoding: utf-8

name = "Surface_DiSigma_to_PiBond/groups"
shortDesc = u""
longDesc = u"""
If a species is bidentate with single bonds, convert it to a vdW species with a double bond.


   *1--*2               *1=*2 
    |   |      ---->      : 
  ~*3~~*4~~             ~*3~ + ~*4~~ 


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) 
so k should be in (1/s)
"""

template(reactants=["Combined"], products=["Adsorbate1","VacantSite1"], ownReverse=False)

reverse = "Surface_PiBond_to_DiSigma"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*1', 0, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,[S]} {3,[S]} 
2 *2 R!H u0 {1,[S]} {4,[S]} 
3 *3 Xo  u0 {1,[S]}
4 *4 Xo  u0 {2,[S]}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
"""
)
