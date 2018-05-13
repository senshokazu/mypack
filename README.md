

Overview
・string_dup.py  -The script duplicates strings.


## Description
・string_dup.py  -The script duplicates strings.
  function:
  opeartion_num -The function duplicates strings with increasing(decreasing) numbers in the text.
                 And the func has no args.
  execution:
  First, Input count of iteration.
  Second, Input string.
  Third, Input start number.
  Forth, Input step number.
  Fifth, Input whether to enable zero-format.
  If you want to enable the format,please input 1 and push Enter key. After that You are required to input number_of_significant_figures.
  If you want not to enable, please push Enter without inputting.
  Sixth, Input string. If you finish, please input '@finish'.

  After that it is iteration of 2 to 4 unless you input '@finish'.


  example:

  You want to duplicate below the query from20130501 to 20130531.

  ```sql

  select sale_price
  from sale_20130501
  where department_id=1
  union
  select sale_price
  from sale_20130502
  where department_id=1
  --Omission--
  select sale_price
  from sale_20130531
  where department_id=1

```
  

  First inputting is 31.

  Second inputting is 'select sale_price\nfrom sale_201305'
  (please input line feed code)

  Third inputting is 1

  Forth inputting is 1

  Fifth inputting is 1

  Sixth inputting is 2

  Seventh inputting is 'where department_id=1\nunion'

  Finaly inputting is '@finish'

## Requirement
import codec
import re 
