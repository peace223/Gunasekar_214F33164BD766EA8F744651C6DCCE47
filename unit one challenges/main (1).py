#leaf year
def leaf_year(year):
  if year%4==0:
    print("{0} is leaf year".format(year))
  elif year%4!=0:
    print("{0} is not a leaf year".format(year))
leaf_year(2017)
leaf_year(2016)