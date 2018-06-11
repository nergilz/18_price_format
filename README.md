## Price Formatter
---
Price formatter make the digits of number from string
---

### Discriptions
+ Software Interfase - to use it on the site
+ Command Line Interface - to start in manual mode from the console project

### Example start from the console
```bash
python format_price.py 1734565.89
```

### Example result in console
```bash
1 734 565.89
```
```bash
None
```

### For use this script in your project
```python
from format_price import format_price
```
```python
format_price(price)
```

#### example return format_price()
```python
'1 234 56.78'
```
```python
None
```

### Example start tests
```bash
python -m unittest -v tests.py
```

### Result tests
```bash
test10_price_is_list_of_number (tests.FormatPriceTest) ... ok
test11_price_is_dict (tests.FormatPriceTest) ... ok
test12_price_is_set_of_string (tests.FormatPriceTest) ... ok
test13_price_is_str_of_number_with_many_zero (tests.FormatPriceTest) ... ok
test14_price_is_number_with_many_zero (tests.FormatPriceTest) ... ok
test15_result_not_none (tests.FormatPriceTest) ... ok
test1_string_of_float (tests.FormatPriceTest) ... ok
test2_integer (tests.FormatPriceTest) ... ok
test3_float (tests.FormatPriceTest) ... ok
test4_rounding_of_a_number (tests.FormatPriceTest) ... ok
test5_bin_string_of_float (tests.FormatPriceTest) ... ok
test6_float_with_letter_in_string (tests.FormatPriceTest) ... ok
test7_string_of_number_with_duble_dot (tests.FormatPriceTest) ... ok
test8_bin_string_of_number_with_double_dot (tests.FormatPriceTest) ... ok
test9_isinstance (tests.FormatPriceTest) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK
```

### For get help
```bash
python3 check_sites_health.py --help
```

### Requirements

```bash
Python ver 3.5 (or higher)
```

---
## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
