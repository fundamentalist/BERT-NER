# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 01:43:46 2021

@author: vg11995
"""

import pandas

df = pandas.read_csv("data/new_training_data_v14.csv")

train_df_index = range(0,1000)
val_df_index = range(1000,1300)
test_df_index = range(1300,2000)

df_train = df[df["Review ID"].isin(set(train_df_index))].reset_index()
df_val = df[df["Review ID"].isin(set(val_df_index))].reset_index()
df_test = df[df["Review ID"].isin(set(test_df_index))].reset_index()

df.head()



f = open("train.txt",'w',encoding="utf-8")


f.write("-DOCSTART- -X- -X- O\n")

import ast

def tagModifier(tag_list):
    out = []
    for t in tag_list:
        flag = 1
        for tag in TAGS_:
            if(tag in t):
                out.append(t)
                flag = 0
                break
        if(flag==1):
            out.append("O")
    return out

                
for i in range(len(df_train)):
    tokens = ast.literal_eval(df_train["token"][i])
    tags = ast.literal_eval(df_train["ground"][i])
    #tags_mod = tagModifier(tags)
    if(len(tokens)==len(tags)):
        print(1)
        for k in range(len(tokens)):
            f.write(tokens[k] + " " + str(tags[k]) + "\n")
        f.write("\n")
    else:
        continue
 
print("Done Loading Data")
f.close()


##################################


f = open("val.txt",'w',encoding="utf-8")


f.write("-DOCSTART- -X- -X- O\n")

import ast

def tagModifier(tag_list):
    out = []
    for t in tag_list:
        flag = 1
        for tag in TAGS_:
            if(tag in t):
                out.append(t)
                flag = 0
                break
        if(flag==1):
            out.append("O")
    return out

                
for i in range(len(df_val)):
    tokens = ast.literal_eval(df_val["token"][i])
    tags = ast.literal_eval(df_val["ground"][i])
    #tags_mod = tagModifier(tags)
    if(len(tokens)==len(tags)):
        print(1)
        for k in range(len(tokens)):
            f.write(tokens[k] + " " + str(tags[k]) + "\n")
        f.write("\n")
    else:
        continue
 
print("Done Loading Data")
f.close()
    
##################################

f = open("test.txt",'w',encoding="utf-8")


f.write("-DOCSTART- -X- -X- O\n")

import ast

def tagModifier(tag_list):
    out = []
    for t in tag_list:
        flag = 1
        for tag in TAGS_:
            if(tag in t):
                out.append(t)
                flag = 0
                break
        if(flag==1):
            out.append("O")
    return out

                
for i in range(len(df_test)):
    tokens = ast.literal_eval(df_test["token"][i])
    tags = ast.literal_eval(df_test["ground"][i])
    #tags_mod = tagModifier(tags)
    if(len(tokens)==len(tags)):
        print(1)
        for k in range(len(tokens)):
            f.write(tokens[k] + " " + str(tags[k]) + "\n")
        f.write("\n")
    else:
        continue
 
print("Done Loading Data")
f.close()
    

all_labels = []

    
for i in range(len(df_train)):
    tags = ast.literal_eval(df_train["ground"][i])
    for t in tags:
        all_labels.append(t)

list(set(all_labels))
    
    
Out[46]: "['O', 'O', 'B-Quantity', 'O', 'O', 'O', 'O', 'B-Quantity', 'B-Mattress Size', 'O', 'O', 'B-Mattress Size', 'O', 'B-Purchase', 'O', 'B-Amazon', 'O', 'B-Duration', 'I-Duration', 'I-Duration', 'I-Duration', 'O', 'B-Comfort', 'O', 'B-Reliability', 'O', 'O', 'O', 'O', 'O', 'O']"
