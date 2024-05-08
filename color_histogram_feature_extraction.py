# //  Created by Ngo The Quang Tien on 26/04/2024.
# //
# //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# //
# //                _ooOoo_                       NAM MÔ A DI ĐÀ PHẬT !
# //               o8888888o
# //               88" . "88      Thí chủ con tên là Ngô Thế Quang Tiến, dương lịch mười 15 tháng mười năm 2003
# //               (| -_- |)      Ngụ tại số nhà 24 Ngách 5 Ngõ 112, Trần Phú, Mộ Lao, Hà Nội, Việt Nam
# //                O\ = /O
# //            ____/`---'\____         Con lạy chín phương trời, con lạy mười phương đất
# //            .' \\| |// `.             Chư Phật mười phương, mười phương chư Phật
# //           / \\||| : |||// \        Con ơn nhờ Trời đất chổ che, Thánh Thần cứu độ
# //         / _||||| -:- |||||- \    Xin nhất tâm kính lễ Hoàng thiên Hậu thổ, Tiên Phật Thánh Thần
# //           | | \\\ - /// | |              Giúp đỡ con code sạch ít bug
# //         | \_| ''\---/'' | |           Đồng nghiệp vui vẻ, sếp quý tăng lương
# //         \ .-\__ `-` ___/-. /          Sức khoẻ dồi dào, tiền vào như nước
# //       ___`. .' /--.--\ `. . __
# //    ."" '< `.___\_<|>_/___.' >'"". NAM MÔ VIÊN THÔNG GIÁO CHỦ ĐẠI TỪ ĐẠI BI TẦM THANH CỨU KHỔ CỨU NẠN
# //   | | : `- \`.;`\ _ /`;.`/ - ` : | |  QUẢNG ĐẠI LINH CẢM QUÁN THẾ ÂM BỒ TÁT
# //     \ \ `-. \_ __\ /__ _/ .-` / /
# //======`-.____`-.___\_____/___.-`____.-'======
# //                `=---='
# //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# //

from PIL import Image
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


# from color_recognition_api import knn_classifier as knn_classifier

# import csv
# import random
# import math
# import operator
# import cv2


# # Tính khoảng cách Euclide
# def calculateEuclideanDistance(variable1, variable2, length):
#     distance = 0
#     for x in range(length):
#         distance += pow(variable1[x] - variable2[x], 2)
#     return math.sqrt(distance)


# # Lấy k hàng xóm gần nhất
# def kNearestNeighbors(training_feature_vector, testInstance, k):
#     distances = [] # Danh sách khoảng cách Euclidean
#     length = len(testInstance) # Số chiều của điểm dữ liệu kiểm tra
#     for x in range(len(training_feature_vector)): # Vòng lặp này tính toán khoảng cách của dữ liệu kiểm tra với tất cả các dữ liệu đã được huấn luyện
#         dist = calculateEuclideanDistance(testInstance,
#                 training_feature_vector[x], length)
#         distances.append((training_feature_vector[x], dist))
#     # Sắp xếp danh sách khoảng cách theo khoảng cách từ bé đến lớn
#     distances.sort(key=operator.itemgetter(1))
#     neighbors = []
#     for x in range(k): #Thêm k hàng xóm gần nhất
#         neighbors.append(distances[x][0])
#     return neighbors


# # Biểu quyết của các hàng xóm
# def responseOfNeighbors(neighbors):
#     all_possible_neighbors = {} # Tạo một từ điển để lưu trữ số lượng biểu quyết cho mỗi nhãn
#     for x in range(len(neighbors)):
#         response = neighbors[x][-1] # Lấy nhãn của hàng xóm thứ x
#         if response in all_possible_neighbors:
#             all_possible_neighbors[response] += 1  # Tăng số lượng biểu quyết cho nhãn đó lên 1
#         else:
#             all_possible_neighbors[response] = 1 # Đặt bằng 1 nếu chưa tồn tại
#     # Sắp xếp lại danh sách
#     sortedVotes = sorted(all_possible_neighbors.items(),
#                          key=operator.itemgetter(1), reverse=True)
#     return sortedVotes[0][0] # trả về biểu quyết được biểu quyết nhiều nhất


# # Tải dữ liệu đặc trưng hình ảnh vào các vector đặc trưng huấn luyện và vector đặc trưng kiểm tra
# def loadDataset(
#     filename,
#     filename2,
#     training_feature_vector=[],
#     test_feature_vector=[],
#     ):
#     with open(filename) as csvfile:
#         lines = csv.reader(csvfile)
#         dataset = list(lines)
#         for x in range(len(dataset)):
#             for y in range(3):
#                 dataset[x][y] = float(dataset[x][y])
#             training_feature_vector.append(dataset[x]) # Tải dữ liệu đặc trưng hình ảnh vào các vector đặc trưng huấn luyện và vector đặc trưng kiểm tra

#     with open(filename2) as csvfile:
#         lines = csv.reader(csvfile)
#         dataset = list(lines)
#         for x in range(len(dataset)):
#             for y in range(3):
#                 dataset[x][y] = float(dataset[x][y])
#             test_feature_vector.append(dataset[x]) # Thêm điểm dữ liệu vào vector đặc trưng kiểm tra


# def main(training_data, test_data):
#     training_feature_vector = []  #  vector đặc trưng huấn luyện
#     test_feature_vector = []  #  vector đặc trưng kiểm tra
#     loadDataset(training_data, test_data, training_feature_vector, test_feature_vector)
#     classifier_prediction = []  # Kết quả dự đoán
#     k = 5  # Giá trị K
#     for x in range(len(test_feature_vector)):
#         neighbors = kNearestNeighbors(training_feature_vector, test_feature_vector[x], k)
#         result = responseOfNeighbors(neighbors)
#         classifier_prediction.append(result)
#     return classifier_prediction[0]

# Kích thước cắt
size_percentage = 0.39

# Định nghĩa hàm tính histogram màu của ảnh kiểm tra
def color_histogram_of_test_image(test_src_image):
    # Xóa dữ liệu của tệp 'test.data' trước khi ghi dữ liệu mới
    with open('test.data', 'w') as myfile:
        myfile.write('')
    # Tải ảnh kiểm tra
    image = test_src_image

    height, width = image.shape[:2]

    # Tính toán vị trí bắt đầu của phần cắt
    start_row = int(height * (1. - size_percentage)/2)
    start_col = int(width * (1. - size_percentage)/2)

    # Tính toán kích thước mới cho phần cắt
    end_row = int(height * (1. + size_percentage)/2)
    end_col = int(width * (1. + size_percentage)/2)

    # Cắt phần của ảnh
    cropped_image = image[start_row:end_row, start_col:end_col]
    # Tách ảnh thành các kênh màu (Blue, Green, Red)
    chans = cv2.split(cropped_image)
    colors = ('b', 'g', 'r')  # Các kênh màu
    features = []  # Danh sách để lưu trữ các đặc trưng histogram
    feature_data = ' '  # Chuỗi để lưu trữ dữ liệu đặc trưng
    counter = 0  # Bộ đếm để lặp qua các kênh màu
    for (chan, color) in zip(chans, colors):
        counter = counter + 1
        # Tính histogram của kênh màu hiện tại
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # Tìm giá trị pixel cao nhất cho kênh màu hiện tại
        elem = np.argmax(hist)
        # Đưa vào các giá trị tương ứng của từng kênh màu
        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
    # Ghi dữ liệu đặc trưng vào tập tin có tên 'test.data'
    with open('test.data', 'w') as myfile:
        myfile.write(feature_data)


# Định nghĩa hàm tính histogram màu của ảnh huấn luyện
def color_histogram_of_training_image(img_name):
    # Dùng tên của các ảnh để biết màu của chúng
    if 'red' in img_name:
        data_source = 'red'
    elif 'yellow' in img_name:
        data_source = 'yellow'
    elif 'green' in img_name:
        data_source = 'green'
    elif 'orange' in img_name:
        data_source = 'orange'
    elif 'white' in img_name:
        data_source = 'white'
    elif 'black' in img_name:
        data_source = 'black'
    elif 'blue' in img_name:
        data_source = 'blue'
    elif 'silver' in img_name:
        data_source = 'silver'
    elif 'brown' in img_name:
        data_source = 'brown'
    elif 'grey' in img_name:
        data_source = 'grey'

    # Từ đây tương tự hàm phía trên
    image = cv2.imread(img_name)

    height, width = image.shape[:2]

    # Tính toán vị trí bắt đầu của phần cắt
    start_row = int(height * (1. - size_percentage)/2)
    start_col = int(width * (1. - size_percentage)/2)

    # Tính toán kích thước mới cho phần cắt
    end_row = int(height * (1. + size_percentage)/2)
    end_col = int(width * (1. + size_percentage)/2)

    # Cắt phần của ảnh
    cropped_image = image[start_row:end_row, start_col:end_col]
    chans = cv2.split(cropped_image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
    # Lưu data vào file training.data
    with open('training.data', 'a') as myfile:
        myfile.write(feature_data + ',' + data_source + '\n')


def training():
    with open('training.data', 'w') as myfile:
        myfile.write('')
    # red color training images-
    for f in os.listdir('./training_dataset/red'):
        color_histogram_of_training_image('./training_dataset/red/' + f)

    # yellow color training images-
    for f in os.listdir('./training_dataset/yellow'):
        color_histogram_of_training_image('./training_dataset/yellow/' + f)

    # green color training images-
    for f in os.listdir('./training_dataset/green'):
        color_histogram_of_training_image('./training_dataset/green/' + f)

    # orange color training images-
    # for f in os.listdir('./training_dataset/orange'):
    #     color_histogram_of_training_image('./training_dataset/orange/' + f)

    # white color training images-
    # for f in os.listdir('./training_dataset/white'):
    #     color_histogram_of_training_image('./training_dataset/white/' + f)
    # silver color training images-
    # for f in os.listdir('./training_dataset/silver'):
    #     color_histogram_of_training_image('./training_dataset/silver/' + f)
    # black color training images-
    for f in os.listdir('./training_dataset/black'):
        color_histogram_of_training_image('./training_dataset/black/' + f)

    # blue color training images-
    for f in os.listdir('./training_dataset/blue'):
        color_histogram_of_training_image('./training_dataset/blue/' + f)

    # brown color training images-
    for f in os.listdir('./training_dataset/brown'):
        color_histogram_of_training_image('./training_dataset/brown/' + f)

    # grey color training images-
    for f in os.listdir('./training_dataset/grey'):
        color_histogram_of_training_image('./training_dataset/grey/' + f)
