from enemy_stats import *

########################## Three Character Party  ####################################

# Even Combats
tough_decent = [ tough(PHYSICAL, FINESSE), tough(FINESSE, MENTAL),
                 decent(PHYSICAL, FINESSE), decent(PHYSICAL, FINESSE) ]
tough_weenie = [ tough(PHYSICAL, FINESSE),
                 tough(FINESSE, MENTAL),
                 tough(MENTAL, PHYSICAL),
                 #weenie(FINESSE, PHYSICAL),
                 weenie(FINESSE, PHYSICAL) ]
decent_normal = [ decent(PHYSICAL, FINESSE), decent(PHYSICAL, FINESSE),
                  decent(PHYSICAL, FINESSE), normal(FINESSE, PHYSICAL),
                  normal(FINESSE, PHYSICAL)]
decent_weenie = [ decent(PHYSICAL, FINESSE), decent(PHYSICAL, FINESSE),
                  decent(PHYSICAL, MENTAL),
                  #decent(PHYSICAL, MENTAL),
                  weenie(PHYSICAL, MENTAL)]
normal_all = [ normal(FINESSE, MENTAL), normal(FINESSE, MENTAL), normal(FINESSE, MENTAL),
               normal(FINESSE, MENTAL),
               normal(PHYSICAL, FINESSE),
               #normal(PHYSICAL, FINESSE),
               normal(PHYSICAL, FINESSE)
]
normal_weenie = [ normal(FINESSE, MENTAL),
                  normal(FINESSE, MENTAL), normal(FINESSE, MENTAL),
                  normal(PHYSICAL, FINESSE),
                  #normal(PHYSICAL, FINESSE),
                  weenie(PHYSICAL, MENTAL), weenie(PHYSICAL, MENTAL)]
# Boss
demigods = [ demigod(MENTAL, FINESSE), demigod(FINESSE, MENTAL), demigod(MENTAL, PHYSICAL) ]
gods_all = [ god(), minor_diety(MENTAL), demigod(MENTAL, FINESSE) ]
