#!/usr/bin/env python3

def main():
    with open('Training_01.txt', 'r') as open_file:
         categories = {}
         cnt = 1
         line = open_file.readline()
         while line:
             print("Line {}: {}".format(cnt, line.strip()))

             category = line.split("/")[2]
             if category not in categories:
                 categories[category] = 1
             else:
                categories[category] += 1

             line = open_file.readline()
             cnt += 1

         for category in categories:
             print ("Category={} :: Occurrences={}".format(category,categories[category]))



main()
