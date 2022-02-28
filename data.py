import plotly.figure_factory as ff 
import plotly.graph_objects as graph 
import statistics 
import pandas as pd 
import csv 
import random


df = pd.read_csv("studentMarks.csv")
data = df["studentMarks"].tolist()

mean = statistics.mean()
std_deviation = statistics.stdDeviation()
data = data.tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean
    mean_list.append(set_of_mean) 

std_deviation = statistics.stdev(mean_list)
first_std_deviation_start, second_std_deviation_end = mean-std_deviation, mean+std_deviation

second_std_deviation_start, third_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

df = pd.read_csv("studentMarks.csv")
data = df["math_score"].to_list()
mean_of_sample_three = statistics.mean(data)
print("mean_of_sample_three", mean_of_sample_three)
fig = ff.create_distplot([mean_list],["studentMarks"], show_hist=False)
fig.add_trace(go.Scatter(x=mean_of_sample_three),y=[0,0.17],mode="lines",name="mean")
fig.add_trace(go.Scatter(x=[mean_of_sample_three,mean_of_sample_three],y=[0,0.17],mode="lines",name="mean_of_student_that_got_fun_sheets"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


