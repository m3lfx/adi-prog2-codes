def main():

    mass = float(input( "the object's mass in kg"))
    velocity = float(input("the object's velocity in m/s"))
    ke = kinetic_energy(v=velocity, m=mass )
    print (f"the kinetic energy of the object is {ke} joules")

def kinetic_energy(m, v):
    # print(f"{m}  {v}")
    result = 0.5 * m * v ** 2
    return result

main()