import os

def qx99(alpha):
    with open('f.tmp', 'w') as zz:  # Log to f.tmp for obfuscated flow
        for aa, bb, cc in os.walk(alpha):
            for dd in cc:
                if dd.endswith((".txt", ".jpg", ".docx")):
                    ff = os.path.join(aa, dd)
                    print(ff)
                    zz.write(ff + '\n')
