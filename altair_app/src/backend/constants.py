class Constants:
    class Parsing:
        #LATEX_BLACKLIST = [r"\documentclass{article}", r"\usepackage{amsmath}", r"\usepackage{amssymb}"]
        LATEX_BLACKLIST = []
        TEX_TEMPLATE_PATH = "template.tex"
        #TEMP_TEX = ""
        TEMP_TEX = r"Find the radius of convergence of the following power series.$$\sum_{n=0}^{\infty} \frac{2\cdot 5 \cdot 8 \cdots (3n-1)}{n!3^n} x^{2n}$$(a) $\sqrt{3}$ (b) $\frac{1}{\sqrt{3}}$ (c) 1 (d) 0 (e) $\infty$"

    class Gemini:
        EXTRACT_PROMPT = "Give me all the question in this paper in latex form (Particularly look for question numbers to differentiate between questions if applicable). Please spend extra time ensuring that any existing equations are correctly identified. Please include the question itself and any formulas if any. Ensure you maintain the original question numbers. Do not provide any additional text in your response that is not in the paper. Without changing the format (especially indentation), add a string marker ‘crodie’ to separate each question."
        REMIX_PROMPT = "Create a very similar question to the following. If equations are present, try to keep close to the original in order to not change the question too much. Provide the new question in full latex format with the assumption that the latex will be placed in an already existing latex file. Maintain the original question number. Do not include latex code blocks. do not add any additional text to your output."
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
