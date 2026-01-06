def calculate_avarage(score):
    return sum(score)/len(score)
avg_1 = calculate_avarage([56,76,87,67,98,73]) 
avg_2 = calculate_avarage([54,90,76,91,87,67,98,73])
print(f"Avarage value of 01 ={avg_1:.2f},Avarage value of o2 = {avg_2: .3f}")
