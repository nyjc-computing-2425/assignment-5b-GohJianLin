# Part 1
#from _typeshed import DataclassInstance


def read_csv(filename):
    # Type your code below
  """
  reads CSV data stored in filename and returns column labels and data

  Parameters
  ----------
  filename
    the name of the file

  Returns
  -------
  header
    the column labels
  data
    the data stored under the columns
    
  Example:
  >>> read_csv(pre-u-enrolment-by-age.csv)
  ([year,age,sex,enrolment_jc],
  [[1984,17 YRS,MF,8710],
  [1984,17 YRS,F,4960],
  [...],
  ...])
  """
  with open(filename,"r") as f:
    header = f.readline().strip("\n").split(",")
    data = []
    
    for item in f:
      lits = item.strip().split(",")
      append_be = [int(lits[0])] + lits[1:-1] +[int(lits[-1])]
      data.append(append_be)
  return (header,data)


# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
  """
  Returns enrolment_by_age of a certain sex taken excluding the column 'sex'

  Parameters
  ----------
  enrolment_by_age
    list of records including year, age, sex and enrolment_jc
  sex
    gender of each person

  Returns
  ------
  nested list containing year, age and enrolment.jc

  Example:
  >>> mf_enrolment = filter_gender(enrolment_data, "MF")
  >>> mf_enrolment
  [[1984, '17 YRS', 8710],
   [1984, '18 YRS', 3927],
   [...],
   [...],
   ...]
  """
  box = []
  for sets in enrolment_by_age:#for list in nlist
    if sex == sets[2]:
      sets.remove(sets[2])
      box.append(sets)
  return box

# Part 3
def sum_by_year(enrolment_data):
    # Type your code below
  """
  Adds up total enrolment for each year

  Parameters
  ----------
  enrolment_data
    nested list containing year, age and enrolment_jc

  Returns
  -------
  nested list of year and total enrolment in each year

  Example:
  >>> enrolment_by_year = sum_by_year(mf_enrolment)
  >>> enrolment_by_year
  [[1984, 21471],
   [1985, 24699],
   [...],
   [...],
   ...]
  """
  list_two = []#year and enrolment(nested)
  list_tri = []#year and enrolment(sort by year)
  for one in enrolment_data:
    one_two = one.pop(1)
    list_two.append(one_two)
    
  for two in list_two: 
    for tri in list_tri:
      if two[0] not in tri:
        list_tri.append(two)#add year and its enrolment
      elif two[0] in tri:
        list_tri[1] += two[1]#add enrolment to certain year
  return list_tri

# Part 4
def write_csv(filename, header, data):
    # Type your code below
  """
  write header and data to filename and return the number of lines written

  Parameters
  ----------
  filename
    name of file
  header
    column headers, first line of the file
  data
    data under the column headers

  Return
  ------
  number of lines written 

  Example:
  >>> filename = 'total-enrolment-by-year.csv'
  >>> header = ["year", "total_enrolment"]
  >>> write_csv(filename, header, enrolment_by_year)
  35
  """
  x = 0
  with open(filename, "w") as f2:
    header = ''.join(header)
    f2.write(header)
    f2.write('\n')
    x+=1
    for datae in data:
      f2.write(datae)
      f2.write('\n')
      x+=1
  return x


# TESTING
# You can write code below to call the above functions
# and test the output
