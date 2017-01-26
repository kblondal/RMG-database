# This file contains a dictionary of kinetics families.  The families
# set to `True` are recommended by RMG and turned on by default by setting
# kineticsFamilies = 'default' in the RMG input file. Families set to `False` 
# are not turned on by default because the family is severely lacking in data.
# These families should only be turned on with caution.

recommendedFamilies = {
'Surface_Adsorption_Single': True,
'Surface_Adsorption_Double': False,
'Surface_Adsorption_vdW': False, # vdW bond doesn't exist yet
'Surface_Adsorption_Dissociative': True,
'Surface_Adsorption_Bidentate': False,
'Surface_Recombination': False, #DEPRECATED. USE SURFACE_DISSOCIATION INSTEAD!
'Surface_Bidentate_Dissociation': False,
'Surface_Dissociation': True,
'Surface_Abstraction': True,
'1+2_Cycloaddition':False,
'1,2-Birad_to_alkene':False,
'1,2_Insertion_CO':False,
'1,2_Insertion_carbene':False,
'1,2_shiftS':False,
'1,3_Insertion_CO2':False,
'1,3_Insertion_ROR':False,
'1,3_Insertion_RSR':False,
'1,4_Cyclic_birad_scission':False,
'1,4_Linear_birad_scission':False,
'2+2_cycloaddition_CCO':False,
'2+2_cycloaddition_CO':False,
'2+2_cycloaddition_Cd':False,
'Birad_recombination':False,
'Cyclic_Ether_Formation':False,
'Diels_alder_addition':False,
'Disproportionation':False,
'HO2_Elimination_from_PeroxyRadical':False,
'H_Abstraction':False,
'H_shift_cyclopentadiene':False,
'Intra_Diels_alder':False,
'Intra_Disproportionation':False,
'Intra_RH_Add_Endocyclic':False,
'Intra_RH_Add_Exocyclic':False,
'Intra_R_Add_Endocyclic':False,
'Intra_R_Add_ExoTetCyclic':False,
'Intra_R_Add_Exocyclic':False,
'Korcek_step1':False,
'Korcek_step2':False,
'Oa_R_Recombination':False,
'R_Addition_COm':False,
'R_Addition_CSm':False,
'R_Addition_MultipleBond':False,
'R_Recombination':False,
'SubstitutionS':False,
'Substitution_O':False,
'intra_H_migration':False,
'intra_NO2_ONO_conversion':False,
'intra_OH_migration':False,
'intra_substitutionCS_cyclization':False,
'intra_substitutionCS_isomerization':False,
'intra_substitutionS_cyclization':False,
'intra_substitutionS_isomerization':False,
'ketoenol':False,
'lone_electron_pair_bond':False,
}
