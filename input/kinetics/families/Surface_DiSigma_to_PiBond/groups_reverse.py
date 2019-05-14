#!/usr/bin/env python
# encoding: utf-8

name = "Surface_PiBond_to_DiSigma/groups"
shortDesc = u""
longDesc = u"""
If a vdW species has a double bond, then convert it to a bidentate with single bonds.


  *1=*2                   *1--*2   
    :            ---->     |   |     
  ~*3~ + ~*4~~           ~*3~~*4~~ 


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) 
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite1"], products=["Adsorbate1"], ownReverse=False)

reverse = "Surface_DiSigma_to_PiBond"

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,[D]} 
2 *2 R!H u0 {1,[D]} 
3 *3 Xo  u0 
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Combined

L1: VacantSite1
"""
)
