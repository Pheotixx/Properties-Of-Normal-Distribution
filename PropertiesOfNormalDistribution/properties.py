import csv
import pandas
import statistics

df = pandas.read_csv('data.csv')

heightList = df["Height(Inches)"].tolist()
weightList = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(heightList)
height_median = statistics.median(heightList)
height_mode = statistics.mode(heightList)
height_std = statistics.stdev(heightList)

weight_mean = statistics.mean(weightList)
weight_median = statistics.median(weightList)
weight_mode = statistics.mode(weightList)
weight_std = statistics.stdev(weightList)

print("Mean,Median,Mode,Standard Deviation for height: {},{},{},{}".format(height_mean,height_median,height_mode,height_std) )
print("Mean,Median,Mode,Standard Deviation for weight: {},{},{},{}".format(weight_mean,weight_median,weight_mode,weight_std) )

height_first_std_start, height_first_std_end = height_mean - height_std, height_mean + height_std
height_second_std_start, height_second_std_end = height_mean - (2*height_std), height_mean + (2*height_std)
height_third_std_start, height_third_std_end = height_mean - (3*height_std), height_mean + (3*height_std)


weight_first_std_start, weight_first_std_end = weight_mean - weight_std, weight_mean + weight_std
weight_second_std_start, weight_second_std_end = weight_mean - (2*weight_std), weight_mean + (2*weight_std)
weight_third_std_start, weight_third_std_end = weight_mean - (3*weight_std), weight_mean + (3*weight_std)

#Percentage of data within first,second,third std's for height

height_data_1_std = [result for result in heightList if result> height_first_std_start and result<height_first_std_end]
height_data_2_std = [result for result in heightList if result> height_second_std_start and result<height_second_std_end]
height_data_3_std = [result for result in heightList if result> height_third_std_start and result<height_third_std_end]

weight_data_1_std = [result for result in weightList if result> weight_first_std_start and result<weight_first_std_end]
weight_data_2_std = [result for result in weightList if result> weight_second_std_start and result<weight_second_std_end]
weight_data_3_std = [result for result in weightList if result> weight_third_std_start and result<weight_third_std_end]

print("{}% of data of height lies within first standard deviation.".format(len(height_data_1_std)*100.0/len(heightList)))
print("{}% of data of height lies within second standard deviation.".format(len(height_data_2_std)*100.0/len(heightList)))
print("{}% of data of height lies within third standard deviation.".format(len(height_data_3_std)*100.0/len(heightList)))

print("{}% of data of weight lies within first standard deviation.".format(len(weight_data_1_std)*100.0/len(weightList)))
print("{}% of data of weight lies within second standard deviation.".format(len(weight_data_2_std)*100.0/len(weightList)))
print("{}% of data of weight lies within third standard deviation.".format(len(weight_data_3_std)*100.0/len(weightList)))




