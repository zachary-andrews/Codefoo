import sys
import math
class unscramble:
    def get_word(self, scrambled):
        var = "abcdefghijklmnopqrstuvwxyz"
        var = var.upper()
        final_str = ""
        for c in scrambled:
            if c != " ":
                addc = var[var.index(c)-13]
            else:
                addc = " "
            final_str += addc
        return final_str