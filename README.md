# **Drowsy Driving Detection System**  

## **Project Overview**  
This project is aimed at detecting drowsy driving in real-time using deep learning techniques. By detecting signs of drowsiness based on the driver’s eye state (open or closed), we can prevent accidents and improve road safety.

---

## **1. Project Objective and Goals**  
- **Objective:** Prevent accidents caused by drowsy driving, which lead to injuries and traffic congestion, by detecting drowsiness in real-time.  
- **Goals:** Develop a system capable of detecting drowsy driving in real-time and alerting the driver.  

---

## **2. Data Description**  

### **1. Data Used**  
- **Type:** Image data (Face and Eye images)  
- **Source:** [Drowsiness Detection Dataset](https://www.kaggle.com/datasets/kutaykutlu/drowsiness-detection)  
- **Data Information:**  
    - Type: `.png` images  
    - Total Images: 48,000  
    - Data Split: 80% training, 10% validation, 10% test  

### **2. Data Preprocessing Steps**  
1. Resize images to 150x150 pixels  
2. Convert images to grayscale (single channel)  
3. Convert images to tensors  
4. Normalize the tensor values with mean 0.5 and standard deviation 0.5  

---

## **3. Model Structure and Training**  

### **1. Model Architecture**  
- The model is not based on pre-trained models; it is custom-designed from scratch.  
- **Architecture:**  
    - **Feature Extractor:** Conv2D → BatchNorm2D → ReLU → Dropout → MaxPool2D  
    - **Inference Layer:** Flatten → Linear → ReLU → Dropout → Linear  
    - **Number of Layers:** 25  
    - **Nodes per Layer:** 64  
    - **Total Parameters:** 830,849  

### **2. Hyperparameter Tuning**  
- **Hyperparameters Adjusted:**  
    - Batch size  
    - Convolution layer output features  
    - Image size after resizing  
    - RGB → Grayscale image channels  
    - Number of epochs  

---

## **4. Model Evaluation**  

### **1. Evaluation Criteria**  
- **Quantitative:** Accuracy, Binary Cross-Entropy Loss  
- **Qualitative:** Real-time drowsiness detection using webcam input  

### **2. Test Environment**  
- **Hardware:** GPU - GeForce RTX 2080 Super, Memory - 16GB  
- **Software:** PyTorch, OpenCV, YOLO  

### **3. Test Results**  
- **Validation Accuracy:** 99%  
- **Validation Loss:** 0.02%

![Training Results Graph](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/20bd0017-ef6c-421b-80a4-8346d75bc65d)  
![Training Results](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/f830faa2-4d26-4cc1-a426-8a97ce633216)  

---

## **5. Process Analysis and Review**  

### **1. Project Phases**  
1. **Data Collection**  
2. **Data Preprocessing**  
3. **Model Design**  
4. **Model Training and Evaluation**  
5. **Model Deployment and Testing**  
   - Real-time video input to detect drowsiness through eye state  
   - Display time on-screen when eyes are closed for detection  
   - After 2 seconds of closed eyes, a warning message is triggered  

### **2. Participants**  
- **Kim Moon-seon:** Data collection, preprocessing, model design, training, evaluation, drowsiness detection system development  
- **Lee Seong-jae:** Data collection, preprocessing, model design, training, evaluation, drowsiness detection system development  

### **3. Tools Used**  
- **PyTorch, OpenCV, YOLOv8-Pose**

---

### **4. Achievements**  
1. **Training Data Generation:** Extracted facial keypoint coordinates from images to create sequential data.  
2. **Model Training:** Improved performance by optimizing model architecture, tuning hyperparameters, and applying feature scaling to training data.  
3. **Model Deployment and Testing:** Real-time video input processed into sequence data for inference, with the output displayed on-screen.  

### **5. Issues and Solutions**  
1. **Shape Errors:** Errors occurred during tensor conversion and normalization due to mismatched input and output shapes.  
   → **Solution:** Errors were resolved by verifying the shapes and ensuring correct input/output formats.  
2. **Eye Detection Accuracy:** The model struggled to detect precise eye coordinates.  
   → **Solution:** A bounding box was created using average eye size to improve detection accuracy.  

### **6. Areas for Improvement**  
- **Performance Lag in OpenCV:** The model is heavy, leading to performance lags during real-time detection.  
- **Bounding Box Variability:** The bounding box size changes depending on the image resolution, causing inconsistency.  

### **7. Potential Applications**  
- **Real-time Drowsiness Prevention System for Accident Prevention**  
   - Real-time inference with no delay and high accuracy.  
   - Example: If eyes remain closed for a certain period, the system alerts the driver to wake up through a warning.

---

## **6. Conclusion**  
This project successfully developed a real-time drowsiness detection system based on deep learning. By utilizing webcam input and detecting drowsiness through eye state, this system can effectively reduce accidents and enhance road safety. Future work will focus on optimizing performance and improving eye detection accuracy.
