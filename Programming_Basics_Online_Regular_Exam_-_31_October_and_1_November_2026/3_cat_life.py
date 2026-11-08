breed_cat = str(input())
gender_cat = str(input())

BRITISH_SHORTHAIR_M = 13
BRITISH_SHORTHAIR_F = 14
SIAMESE_M = 15
SIAMESE_F = 16
PRESIAN_M = 14
PRESIAN_F = 15
RAGDOLL_M = 16
RAGDOLL_F = 17
AMERICAN_SHORTHAIR_M = 12
AMERICAN_SHORTHAIR_F = 13
SIBERIAN_M = 11
SIBERIAN_F = 12

cat_months = 0

if breed_cat == "British Shorthair" or breed_cat == "Siamese" or breed_cat == "Persian" or breed_cat == "Ragdoll" or breed_cat == "American Shorthair" or breed_cat == "Siberian":
    if breed_cat == "British Shorthair":
        if gender_cat == "m":
            cat_months += BRITISH_SHORTHAIR_M * 2
        else:
            cat_months += BRITISH_SHORTHAIR_F * 2
    elif breed_cat == "Siamese":
        if gender_cat == "m":
            cat_months += SIAMESE_M * 2
        else:
            cat_months += SIAMESE_F * 2
    elif breed_cat == "Persian":
        if gender_cat == "m":
            cat_months += PRESIAN_M * 2
        else:
            cat_months += PRESIAN_F * 2
    elif breed_cat == "Ragdoll":
        if gender_cat == "m":
            cat_months += RAGDOLL_M * 2
        else:
            cat_months += RAGDOLL_F * 2
    elif breed_cat == "American Shorthair":
        if gender_cat == "m":
            cat_months += AMERICAN_SHORTHAIR_M * 2
        else:
            cat_months += AMERICAN_SHORTHAIR_F * 2
    elif breed_cat == "Siberian":
        if gender_cat == "m":
            cat_months += SIBERIAN_M * 2
        else:
            cat_months += SIBERIAN_F * 2
    print(f"{cat_months} cat months")
else:
    print(f"{breed_cat} is invalid cat!")