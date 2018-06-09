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
import format_price
```
```python
format_price.main(price)
```

#### return main()
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
test1_main (tests.FormatPriceTest) ... ok
test2_main_int (tests.FormatPriceTest) ... ok
test3_main (tests.FormatPriceTest) ... ok
test4_main (tests.FormatPriceTest) ... ok
test5_main (tests.FormatPriceTest) ... ok
test6_main (tests.FormatPriceTest) ... ok
test7_main (tests.FormatPriceTest) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

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
