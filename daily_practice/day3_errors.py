unicorn_profiles = ["calafiori", "baleba", "bellingham"]
print(unicorn_profiles[2])

highest_output = {"Kane":80, "Olise":50, "Mbappe":65}
print(highest_output["Olise"])

#print("Goals scored" + 80)

# 1. Define the reusable function signature (using generic parameter names)
def safe_dict_get(d, key, default_value):
    try:
        return d[key]
    except KeyError:
        return default_value

highest_output = {"Kane": 80, "Olise": 50, "Mbappe": 65}

print(safe_dict_get(highest_output, "Kane", 0))
print(safe_dict_get(highest_output, "Haaland", 0))
