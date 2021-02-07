fahrenheit=int(input("Anna lämpötila (F): "))
celsius=(fahrenheit-32)/1.8
print(f"{fahrenheit} fahrenheit-astetta on {celsius} celsius-astetta")
if celsius < 0:
    print("Paleltaa!")