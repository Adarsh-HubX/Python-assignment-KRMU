
# Lab 1: Daily Calorie Tracker CLI

## Project Overview
This project is a **Python console application** to track daily calorie intake.  
Users can log their meals with calorie values, calculate total and average calories, compare against a personal daily limit, and optionally save session reports as text files.

---

## Folder Structure

```text
lab1/
│
├── tracker.py                    ← Python script implementing all tasks
└── sample_data/        ← Folder containing sample output files and README
    ├── Shweta_sample_output.txt  ← Within daily limit case
    ├── Rohit_sample_output.txt  ← Exactly met daily limit case
    ├── Harsh_sample_output.txt   ← Exceeded daily limit case
    └── README.md                 ← Explanation of sample output files
```
---

## How to Run

1. Open `tracker.py` in any Python IDE (e.g., VS Code) or terminal.  
2. Follow on-screen prompts to enter:  
   - Name, Age, Gender  
   - Weight (kg), Height (cm)  
   - Activity factor (1.2=sedentary, 1.375=light, 1.55=moderate, 1.725=very active, 1.9=extra active)  
   - Number of meals and their details (meal name & calorie amount)  
3. The program will calculate total and average calories, check against your daily limit, and display a formatted summary.  
4. Optionally, choose to save the session report. Saved reports will appear in the `daily_calorie_tracker/` folder.

---

## Sample Outputs

Three sample runs are provided in `sample_data/` folder demonstrating:

- **Within daily limit** → `Shweta_sample_output.txt`  
- **Exactly met daily limit** → `Rohit_sample_output.txt`  
- **Exceeded daily limit** → `Harsh_sample_output.txt`  

Refer to `sample_data/README.md` for detailed explanation of each sample output file.

---

## Notes

- The project demonstrates use of:  
  - Python input and type conversion  
  - Lists and basic data structures  
  - Arithmetic and comparison operators  
  - String formatting with f-strings  
  - File I/O for saving session logs
