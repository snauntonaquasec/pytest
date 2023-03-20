#!/usr/bin/env python3
import jmespath
j = { "numbers": [{ "str": "one", "int": 1 },{ "str": "two", "int": 2 }] }
print(jmespath.search("numbers[*].str", j))
