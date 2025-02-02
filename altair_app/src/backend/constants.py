class Constants:
    class Gemini:
        #Generate a Latex version of every question from the input file. 
        #For each question, include the complete text and any formulas or equations exactly as they appear. 
        #Make sure that all equations are correctly identified and rendered in LaTeX. 
        #Do not include any additional commentary or text beyond what is present in the paper.
        EXTRACT_PROMPT = "Give me all the question in this paper in latex form. Please spend extra time ensuring that any existing equations are correctly identified. Please include the question itself and any formulas if any. Do not provide any additional text in your response that is not in the paper"
        REMIX_PROMPT = "Create a very similar question to the following. If equations are present, try to keep close to the original in order to not change the question too much. Provide the new question in full latex format. Please do not add any additional text to your output."
        TEMP_QUESTION = """20. Find the radius of convergence of the following power series.
∑
𝑛
=
0
∞
(
−
1
)
𝑛
1
⋅
4
⋅
7
⋯
(
3
𝑛
−
2
)
𝑛
!
3
𝑛
𝑥
3
𝑛
n=0
∑
∞
​
 (−1) 
n
  
n!3 
n
 
1⋅4⋅7⋯(3n−2)
​
 x 
3n
 
(a) 
3
3
(b) 
1
3
3
(c) 
1
(d) 
0
(e) 
∞
(a)  
3
  
3
​
 (b)  
3
  
3
​
 
1
​
 (c) 1(d) 0(e) ∞"""
