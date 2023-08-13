import random
# Dummy data to say which hr policies are fit for which category
categories = {
    "Green": {"HR Policies": ["7 days paid menstrual leave per month", "6 months paid maternity leave", "Inclusive bathrooms", "Breastfeeding rooms", "Child care centers", "Strict harassment policies"]},
    "Orange": {"HR Policies": ["2 days paid menstrual leave per month", "3 months paid maternity leave", "no inclusive bathrooms", "Strict harassment policies"]},
    "Red": {"HR Policies": ["no menstrual leave per month", "3 months unpaid maternity leave", "Non-strict harassment policies"]}
}
# Categorize companies based on category dummy data
# Dummy data for companies in green category (for demonstration purposes)
companies_green = [
    {"name": "Unilever", "category": "green", "location": "Cape Town"},
    {"name": "Box Fusion", "category": "green", "location": "Durban"},
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
    {"name": "Glassdoor", "category": "red", "location": "Durban"},
    {"name": "Eskom", "category": "red", "location": "Johannesburg"},
]
# Create a dictionary to map category names to their respective company lists
category_to_companies = {
    "Green": companies_green,
    "Orange": companies_orange,
    "Red": companies_red
}

# Dummy data for job candidates (for demonstration purposes)
resumes = [
    {"name": "Nombali", "skills": ["Javascript", "C#", "C++"], "identity": "woman"},
    {"name": "Sandra", "skills": ["Javascript", "HTML", "CSS", "Python"], "identity": "transgendered"},
    {"name": "Precious", "skills": ["Python", "Ruby", "Flutter"], "identity": "non-binary"},
    {"name": "Alex", "skills": ["C++", "Algorithms"], "identity": "man"},
]

# # Create variable 'candidate' containing the candidate's name (e.g., "Sandra", "Alex")
# # and a variable 'recommended_companies' to store the list of recommended companies

candidate = "Sandra"  # Replace this with the actual candidate's name

if candidate in [resume["name"] for resume in resumes]:
    recommended_companies = companies_green
else:
    recommended_companies = companies_red

print("Recommended companies:", recommended_companies)
