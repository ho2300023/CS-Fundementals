import os

def qx99(alpha):
    with open('f.tmp', 'w') as log:  

        for aa, bb, cc in os.walk(alpha):
            for dd in cc:
                if dd.endswith((".txt", ".jpg", ".docx")):
                    ff = os.path.join(aa, dd)
                    print(ff)
                    zz.write(ff + '\n')

if __name__ == "__main__":
    ee = input("Path: ")
    qx99(ee)
