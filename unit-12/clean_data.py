name = "  Saviour ISiDoRE  "
state_of_origin = " akwa IBOM State "

clean_name = name.strip().lower()
clean_state_of_origin = state_of_origin.strip().title()
print(f"Original: {name}")
print(f"Original: {state_of_origin}")
print(clean_name)
print(clean_state_of_origin)
print(clean_state_of_origin.replace("State","Nigeria"))
