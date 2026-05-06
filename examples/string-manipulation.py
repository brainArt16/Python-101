# --- Pharmacy Example: escape characters in a label ---
# Context: building a compact label string with newlines and tabs

# label = "METFORMIN 500 mg \nTake 1 tablet twice daily with meals.\n\tRefrigerate after opening."
# print(label)
# Output:
# METFORMIN 500 mg
# Take 1 tablet twice daily with meals.
#     Refrigerate after opening.

# Tab-separated dispensing report row
# report_row = "Sarah Johnson 500 mg Twi\nce daily 10 days"
# print(report_row)
# Sarah Johnson   500 mg  Twice daily     10 days

# Indexing
# medication = "METFORMIN"


# # print(medication.index("F"))
# print(len(medication))
# # print(medication[7])
# # print(medication[-1]) # last character

# # Slicing
# # print(medication[2:4]) # first three characters

# # Remove leading and trailing whitespace
# print(len(medication.strip()))


# --- Pharmacy Example: join() for building a medication summary ---
# medications = ["Metformin", "Lisinopril", "Atorvastatin"]

# # Comma-separated for a label
# summary = ", ".join(medications)
# # print(summary)  # Metformin, Lisinopril, Atorvastatin

# # Bullet-point list for a report
# bullet_list = "\n  - ".join(medications)
# print("Current medications:\n  - " + bullet_list)


# --- Pharmacy Example: .format() for a prescription summary ---
patient_name = "Sarah Johnson"
drug = "Amoxicillin"
dose_mg = 500

summary = "{} is prescribed {} {} mg.".format(patient_name, drug, dose_mg)
print(summary)
# Sarah Johnson is prescribed Amoxicillin 500 mg.

# Named placeholders (more readable)
summary_named = "{patient} is prescribed {drug} {dose} mg.".format(
    patient=patient_name, drug=drug, dose=dose_mg
)
print(summary_named)
