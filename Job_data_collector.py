import Job_Scrapper as js
import pandas as pd

path = "C://Users/vivek/jupyter_file/Python Based Project/Data Science/Job-Recommendation-System/chromedriver"

df = js.get_jobs("Data+Science", 20, False, path, 15)

print(df)