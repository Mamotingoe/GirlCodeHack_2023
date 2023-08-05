import random

# Dummy data for companies in green category (for demonstration purposes)
companies_green = [
    {"name": "Unilever", "category": "green", "location": "Cape Town"},
    {"name": "Hewlett Packard Enterprise", "category": "green", "location": "Durban"},
    {"name": "Chenosis", "category": "green", "location": "Johannesburg"},
    {"name":"Nestlé","category":"green","location":"Pretoria"},
    {"name":"Vumatel","category":"green","location":"Johannesburg"},
    {"name":"Mint","category":"green","location":"Johannesburg"}
]

# Dummy data for companies in orange category (for demonstration purposes)
companies_orange = [
    {"name": "Liberty Holdings", "category": "orange", "location": "Cape Town"},
    {"name": "Woolworths Group", "category": "orange", "location": "Durban"},
    {"name": "Discovery", "category": "orange", "location": "Johannesburg"},
]

# Dummy data for companies in red category (for demonstration purposes)
companies_red = [
    {"name": "Regus", "category": "red", "location": "Cape Town"},
    {"name": "Glassdor", "category": "red", "location": "Durban"},
    {"name": "Eskom", "category": "red", "location": "Johannesburg"},
]
# Dummy data for job candidates (for demonstration purposes)
resumes = [
    {"name": "Nombali", "skills": ["Javascript", "C#", "C++"], "identity": "woman"},
    {"name": "Sandra", "skills": ["Javascript", "HTML", "CSS", "Python"], "identity": "queer woman"},
    {"name": "Precious", "skills": ["Python", "Ruby", "Flutter"], "identity": "non-binary"},
    {"name": "Alex", "skills": ["C++", "Algorithms"], "identity": "man"},
]

# # Create variable 'candidate' containing the candidate's name (e.g., "Sandra", "Alex")
# # and a variable 'recommended_companies' to store the list of recommended companies

candidate = "Alex"  # Replace this with the actual candidate's name

if candidate in [resume["name"] for resume in resumes]:
    recommended_companies = companies_green
else:
    recommended_companies = companies_red

print("Recommended companies:", recommended_companies)
