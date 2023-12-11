#-*-coding:utf-8-*-
import shapefile as shp
import csv
import codecs
import os

def trans_point(folder, fn, delimiter=','):
    '''transfer a csv file to shapefile'''
    # create a point shapefile
    output_shp = shp.Writer(folder + "%s.shp"%fn.split('.')[0], shp.POINT)
    # for every record there must be a corresponding geometry.
    output_shp.autoBalance = 1
    # create the field names and data type for each.you can omit fields here
    # 顺序一定要与下面的保持一致
    output_shp.field('photo_url', 'C', 50) # string, max-length
    output_shp.field('longitude', 'F', 10, 8) # float
    output_shp.field('latitude', 'F', 10, 8) # float
    output_shp.field('scene', 'C', 20) # string, max-length
    output_shp.field('scene_id', 'N')  # int
    counter = 1 # count the features
    # access the CSV file
    with codecs.open(folder + fn, 'rb', 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        next(reader, None) # skip the header
        #loop through each of the rows and assign the attributes to variables
        for row in reader:
            try:
                photo_url = row[0]
                lng= float(row[1])
                lat = float(row[2])
                scene = row[3]
                scene_id = int(row[4])
                output_shp.point(lng, lat) # create the point geometry
                output_shp.record(photo_url, lng, lat, scene, scene_id) # add attribute data
                if counter % 10000 == 0:
                    print("Feature " + str(counter) + " added to Shapefile.")
                counter = counter + 1
            except:
                print(row)