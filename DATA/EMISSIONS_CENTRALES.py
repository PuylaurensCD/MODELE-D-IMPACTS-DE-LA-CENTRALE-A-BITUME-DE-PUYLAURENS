#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:09:06 2023

@author: m_a_m
"""
# en (g/Nm3)h_17%O2
emission_ATOSCA = {"Poussières totale":2.4E-3,
                   "CH4":0.4E-3,
                   "CO":6.9E-3,
                   "SOx":72.2E-3,
                   "NOx":44E-3,
                   "COV hors CH4":0.5E-3,
                   "HAP":0.00007E-3,
                   "Cadmium (Cd)":0,
                   "Thallium (Tl)":0,
                   "Mercure (Hg)":0.4E-6,
                   "Arsenic (As)":0,
                   "Plomb (Pb)":0.64E-6,
                   "Chrome (Cr)":0.96E-6,
                   "Antimoine (Sb)":0,
                   "Cobalt (Co)":0.26E-6,
                   "Cuivre (Cu)":0,
                   'Etain (Sn)':0,
                   'Manganèse (Mn)':2.71E-6,
                   "Nickel (Ni)":0.26E-6,
                   "Sellenium (Se)":0,
                   "Tellure (Te)":0,
                   "Vanadium (V)":0,
                   "Zinc (Zn)":8.4E-6,
                   "Benzo(a)pyrène + Naphtalène":0,
                   "Fluoranthène":7E-8, #HAP
                   "Benzo-a-anthracène":0,
                   "Benzo-b-Fluoranthène":0,
                   "Benzo-k-Fluoranthène":0,
                   "Benzo-a-pyrène":0,
                   "Dibenzo-a,h-anthracène":0,
                   "Benzo-g,h,i-pérylène":0,
                   "Indeno-1.2.3,c,d-pyrène":0,
                   "Formaldéhyde":9.6E-5, #Aldhéyde
                   "Acétaldéhyde":3.5E-6,
                   "Acroléine":3.5E-6,
                   "Furfural":0,
                   "Chloroacétaldéhyde":0,
                   "1,1,2-Trichloroéthane":0, #COV spécifique
                   "1,1,2,2-Tétrachloroéthane":0,
                   '1,1-dichloroéthène':0,
                   "1.2-Dicholorobenzène":0,
                   "1,4-dioxane":0,
                   "Benzene (71-43-2)":8.7E-6,
                   "Biphényl":0,
                   "Chloroforme":0,
                   "Chlorométhane":0,
                   "Chlorure de benzyle":0,
                   "Dichlorométhane":0,
                   "Méthacrylate":0,
                   "Méthacrylate de méthyle":0,
                   "Tétrachloroéthylène":0,
                   "Tétrachlorométhane":0,
                   "trichloroéthylène":0,
                   "Pyridine":0,
                   "Diméthylsulfide":0,
                   "Dimethyldisulfide":0,
                   "2-Butanthiol":4.2E-6, #mercaptan
                   "2-Propantiol":4.2E-6,
                   "Butylmercaptan":4.2E-6,
                   "Ethylmercaptan":4.2E-6,
                   "Méthylmercaptan (Methanethiol)":4.2E-6,
                   "Propylmecaptan":4.2E-6,
                   "ter-Butyl mercaptan":4.2E-6,
                   "1,3 Butadiène (H340-H350)":0,#TENEUR EN COMPOSES A PHRASES DE RISQUES
                   "Benzène (H340-H350)":0,
                   "Dichlorométhane (H351)":0,
                   "Tétrahydrofuran (H351)":0,
                   "1,2-diethoxyethane (H360)":0,
                   "Ethylbromide (H351)":0,
                   "1,4-dichlorobenzene (H351)":0,
                   "2,4-TDI (2,4-diisocyanate de toluène":0, #ISOCYANATES
                   "Acide acrylique":1.9E-4,#AMINES ET ACIDES GRAS
                   "Acide chloroacétique":1.9E-4,
                   "Anhydre maléique":1.9E-4,
                   "Diéthylamine":1.9E-5,
                   "Ethylamine":1.9E-5,
                   "Triéthylamine":1.9E-5,
                   "Diméthylamine":1.9E-5,
                   "aniline":0, #ANILINES
                   "o-Toluidine":0,
                   "2,3-Diméthylphénol":4.7E-7,#COMPOSES NITRIQUES
                   "2,4,5-Trichlorophénol":4.7E-7,
                   "2,4,6-Trichlorophénol":4.7E-7,
                   "2,4-Dichlorophénol":4.7E-7,
                   "Phénol 2-nitro":2.4E-6,
                   "2,5-Diméthylphénol":4.7E-7,
                   "2,6-Diméthylphénol":4.7E-7,
                   "2-Méthylphénol (o-crésol)":1.4E-6,
                   "3-Méthylphénol (m-crésol)":0.16/3600,
                   "2-Nitrotoluène":2.4E-6,
                   "3,4-Diméthylphénol":4.7E-7,
                   "3,5-Diméthylphénol":4.7E-7,
                   "4-Nitrotoluène":2.4E-6,
                   "3-Nitrotoluène":2.4E-6,
                   "4-Méthyl-2-nitrophénol":2.4E-6,
                   "4-Méthylphénol (p-crésol)":4.7E-7,
                   "Phénol":4.7E-7,
                   "Nitrobenzène":2.4E-6
                   }

# en (g/Nm3)h_17%O2
emission_DREAL = {"Poussières totale":50E-3,
                  "CO":500E-3,
                  "SOx":300E-3,
                  "NOx":350E-3,
                  "COV hors CH4":110E-3,
                  "COV spécifique":20E-3,
                  "COV dangereux":2E-3,
                  "HAP":2E-4,
                  "Cadmium (Cd)":5E-5,
                  "Thallium (Tl)":5E-5,
                  "Mercure (Hg)":5E-5,
                  "Arsenic (As)":1E-3,
                  "Plomb (Pb)":1E-3,
                  "Chrome (Cr)":5E-3,
                  "Antimoine (Sb)":5E-3,
                  "Cobalt (Co)":5E-3,
                  "Cuivre (Cu)":5E-3,
                  'Etain (Sn)':5E-3,
                  'Manganèse (Mn)':5E-36,
                  "Nickel (Ni)":5E-3,
                  "Sellenium (Se)":1E-3,
                  "Tellure (Te)":1E-3,
                  "Vanadium (V)":5E-3,
                  "Zinc (Zn)":5E-3,
                  "Benzo(a)pyrène + Naphtalène":2E-4,
                  "Benzo-a-pyrène":2E-4,
                  "Formaldéhyde":2E-3,
                  "Benzene (71-43-2)":2E-3,
                  "Acroléine":2E-3, 
                  "Acide acrylique":2E-3,
                  "Acétaldéhyde":2E-3, 
                  "Phénol":2E-3,}

#en g/s
emission_flux_ATOSCA = {"Poussières totale":280/3600,
                       "CO2":4954000/3600,
                       "CH4":43/3600,
                       "CO":800/3600,
                       "SOx":8100/3600,
                       "NOx":5000/3600,
                       "COV hors CH4":63/3600,
                       "COV spécifique":1/3600,
                       "HAP":0.006/3600,
                       "Cadmium (Cd)":0.006/3600,
                       "Thallium (Tl)":0/3600,
                       "Mercure (Hg)":0.047/3600,
                       "Arsenic (As)":0.0033/3600,
                       "Plomb (Pb)":0.09/3600,
                       "Chrome (Cr)":0.21/3600,
                       "Antimoine (Sb)":0/3600,
                       "Cobalt (Co)":0.04/3600,
                       "Cuivre (Cu)":0.08/3600,
                       'Etain (Sn)':0.003/3600,
                       'Manganèse (Mn)':0.5/3600,
                       "Nickel (Ni)":0.07/3600,
                       "Sellenium (Se)":0/3600,
                       "Tellure (Te)":0/3600,
                       "Vanadium (V)":0.013/3600,
                       "Zinc (Zn)":1.34/3600,
                       "Benzo(a)pyrène + Naphtalène":0/3600,
                       "Fluoranthène":0.0011/3600, #HAP
                       "Benzo-a-anthracène":0/3600,
                       "Benzo-b-Fluoranthène":0/3600,
                       "Benzo-k-Fluoranthène":0/3600,
                       "Benzo-a-pyrène":0/3600,
                       "Dibenzo-a,h-anthracène":0/3600,
                       "Benzo-g,h,i-pérylène":0/3600,
                       "Indeno-1.2.3,c,d-pyrène":0/3600,
                       "Formaldéhyde":11/3600, #Aldhéyde
                       "Acétaldéhyde":0.4/3600,
                       "Acroléine":0.4/3600,
                       "Furfural":0/3600,
                       "Chloroacétaldéhyde":0/3600,
                       "1,1,2-Trichloroéthane":0/3600, #COV spécifique
                       "1,1,2,2-Tétrachloroéthane":0/3600,
                       '1,1-dichloroéthène':0/3600,
                       "1.2-Dicholorobenzène":0/3600,
                       "1,4-dioxane":0/3600,
                       "Benzene (71-43-2)":1/3600,
                       "Biphényl":0/3600,
                       "Chloroforme":0/3600,
                       "Chlorométhane":0/3600,
                       "Chlorure de benzyle":0/3600,
                       "Dichlorométhane":0/3600,
                       "Méthacrylate":0/3600,
                       "Méthacrylate de méthyle":0/3600,
                       "Tétrachloroéthylène":0/3600,
                       "Tétrachlorométhane":0/3600,
                       "trichloroéthylène":0/3600,
                       "Pyridine":0/3600,
                       "Diméthylsulfide":0/3600,
                       "Dimethyldisulfide":0/3600,
                       "2-Butanthiol":0.48/3600, #mercaptan
                       "2-Propantiol":0.48/3600,
                       "Butylmercaptan":0.48/3600,
                       "Ethylmercaptan":0.48/3600,
                       "Méthylmercaptan (Methanethiol)":0.48/3600,
                       "Propylmecaptan":0.48/3600,
                       "ter-Butyl mercaptan":0.48/3600,
                       "1,3 Butadiène (H340-H350)":0/3600,#TENEUR EN COMPOSES A PHRASES DE RISQUES
                       "Benzène (H340-H350)":0/3600,
                       "Dichlorométhane (H351)":0/3600,
                       "Tétrahydrofuran (H351)":0/3600,
                       "1,2-diethoxyethane (H360)":0/3600,
                       "Ethylbromide (H351)":0/3600,
                       "1,4-dichlorobenzene (H351)":0/3600,
                       "2,4-TDI (2,4-diisocyanate de toluène":0/3600, #ISOCYANATES
                       "Acide acrylique":22/3600,#AMINES ET ACIDES GRAS
                       "Acide chloroacétique":22/3600,
                       "Anhydre maléique":22/3600,
                       "Diéthylamine":2.2/3600,
                       "Ethylamine":2.2/3600,
                       "Triéthylamine":2.2/3600,
                       "Diméthylamine":2.2/3600,
                       "aniline":0/3600, #ANILINES
                       "o-Toluidine":0/3600,
                       "2,3-Diméthylphénol":0.055/3600,#COMPOSES NITRIQUES
                       "2,4,5-Trichlorophénol":0.055/3600,
                       "2,4,6-Trichlorophénol":0.055/3600,
                       "2,4-Dichlorophénol":0.055/3600,
                       "Phénol 2-nitro":0.27/3600,
                       "2,5-Diméthylphénol":0.055/3600,
                       "2,6-Diméthylphénol":0.055/3600,
                       "2-Méthylphénol (o-crésol)":0.16/3600,
                       "3-Méthylphénol (m-crésol)":0.16/3600,
                       "2-Nitrotoluène":0.27/3600,
                       "3,4-Diméthylphénol":0.055/3600,
                       "3,5-Diméthylphénol":0.055/3600,
                       "4-Nitrotoluène":0.27/3600,
                       "3-Nitrotoluène":0.27/3600,
                       "4-Méthyl-2-nitrophénol":0.27/3600,
                       "4-Méthylphénol (p-crésol)":0.055/3600,
                       "Phénol":0.055/3600,
                       "Nitrobenzène":0.27/3600
                       }
test = list(emission_ATOSCA.keys())
emission_CAREPS_moy = {"Poussières totale":840/3600,
                       "CO":15690/3600,
                       "SOx":1710/3600,
                       "NOx":2690/3600,
                       "COV hors CH4":2490/3600}