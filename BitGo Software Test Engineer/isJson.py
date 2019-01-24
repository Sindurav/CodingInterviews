# Complete the checkJSON function below.

import math
import os
import random
import re
import sys
import json


def checkJSON(jsonstring):
    try:
        json.loads(jsonstring)
        return True
    except:
        return False
