# Pythagorean triples  x² +y² = z² for integers 0 < x,y,z <20 ∈ Ζ
print("# Pythagorean triples  x² +y² = z² for integers 0 < x,y,x <20 ∈ Ζ")
Integers_Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for x in range(1,21):
    print("################################")
    for y in range(1,21):
        z=((x*x)+(y*y))** 0.5
        if z.is_integer():
            print(f"Για χ={x} Για y={y} Για z={z} ")