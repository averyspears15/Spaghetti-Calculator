# if    4  = 2 cups of tomato sauce
#then   2 =  ?

# if    4 = 1/3 cups of tomato paste
#then   2 = ?

# if    4 = 2 cloves garlic
#then   2 = ?

# if    4 = 1 tablespoon oregano
#then   2 = ?

print('My name is Avery Spears')
print('My program is complete')

regularServingsForSpaghetti = 4
cupsOfTomatoSaucePer4Servings = 2
cupsOfTomatoPastePer4Servings = 1/3
clovesOfGarlicPer4Servings = 2
tablespoonsOfOreganoPer4Servings = 1

userNumberOfServings = float( input("How many servings would you like to make: ") )


expectedCupsOfTomatoSauce = ( userNumberOfServings / regularServingsForSpaghetti ) * \
                            cupsOfTomatoSaucePer4Servings

expectedCupsOfTomatoPaste = ( userNumberOfServings / regularServingsForSpaghetti ) * \
                            cupsOfTomatoPastePer4Servings

expectedClovesOfGarlic = ( userNumberOfServings / regularServingsForSpaghetti ) * \
                         clovesOfGarlicPer4Servings

expectedTablespoonsOfOregano = ( userNumberOfServings / regularServingsForSpaghetti ) * \
                               tablespoonsOfOreganoPer4Servings

print( " For " + str(userNumberOfServings) + " servings, you will need "  + \
      format( expectedCupsOfTomatoSauce, ".2f" )  +  " cups of tomato sauce, " + \
      format( expectedCupsOfTomatoPaste, ".2f" ) + " cups of tomato paste, " + \
      format( expectedClovesOfGarlic, ".2f" ) + " cloves of garlic and " + \
      format( expectedTablespoonsOfOregano, ".2f" ) + " tablespoons of oregano  " )
                          



                            
