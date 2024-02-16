import utils as u

def question1():
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2781

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.0350

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.2364

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.0291

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.0729

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.1711

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.3219

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.1711

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    tree = u.BinaryTree("smoking")
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  
    answer["training_error"] = 0.0  
    return answer

def question2():
    answer = {}

    answer["(a) entropy_entire_data"] = 1.425
    
    answer["(b) x < 0.2"] = 0.177
    answer["(b) x < 0.7"] = 0.355
    answer["(b) y < 0.6"] = 0.347

    answer["(c) attribute"] = 'x<0.7'  

    tree = u.BinaryTree("x<=0.7")
    
    A = tree.insert_left("y<=0.6")
    A.insert_left("B")
    C = A.insert_right("x<=0.2")
    D = C.insert_left("y<=0.8")
    C.insert_right("A")
    D.insert_left("C")
    D.insert_right("B")
    
    B = tree.insert_right("y<=0.6")
    E = B.insert_left("y<=0.3")
    B.insert_right("A")
    E.insert_left("A")
    E.insert_right("C")
    answer["(d) full decision tree"] = tree

    return answer

def question3():
    answer = {}

    answer["(a) Gini, overall"] = 0.5

    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1622
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    answer["(f) explain choice"] = "Car type has the lowest gini among the three attributes(Gender,Car type and Shirt)"

    return answer

def question4():
    answer = {}

    answer["a"] = ['binary','qualitative','ordinal']
    answer["a: explain"] = "Considering Time in AM/PM as Binary"

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = ""

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous','quantitative','interval']
    answer["f: explain"] = ""

    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = ""

    answer["l"] = ['continuous','quantitative','ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = ""

    return answer

def question5():
    explain = {}

    explain["a"] = "Model 2"
    explain["a explain"] = "Model 1 has high accuracy on A but accuracy drops on B which indicates overfitting, But for Model 2 accuracy on both Dataset A and B are almost same indicating better generalization to new data. "

    explain["b"] = "Model 2"
    explain["b explain"] = "Though accuracy drops slightly Model 2 is still preferable due to better generalization observed earlier and it is less likely to overfit."

    explain["c similarity"] = "Regularization"
    explain["c similarity explain"] = "Both techniques aims to reduce overfitting by penalizing models for complexity."

    explain["c difference"] = "Specificity"
    explain["c difference explain"] = "MDL aims for a model that requires fewer bits to describe,whereas pessimistic error aims to adjust tree error to avoid complex decision tree."

    return explain

def question6():
    answer = {}

    answer["a, level 1"] = "x<=0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y<=0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x<=0.2"

    answer["b, expected error"] = 0.

    tree = u.BinaryTree("x<=0.5")
    A = tree.insert_left("y<=0.4")
    C = A.insert_left('A')
    A.insert_right('x<=0.2')

    B = tree.insert_right("A")
    answer["c, tree"] = tree

    return answer

def question7():
    answer = {}

    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    answer["c, which attrib"] = "ID"

    answer["d, gain ratio, ID"] = 0.231
    answer["e, gain ratio, Handedness"] = 0.531

    answer["f, which attrib"] = "Handedness"

    return answer

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)
