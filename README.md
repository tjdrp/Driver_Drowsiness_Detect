# **Development of a Real-time Drowsy Driving Detection Model Using Deep Learning**  

## **1. Topic**  
Real-time detection of drowsy driving using deep learning  

## **2. Purpose and Objectives**  
- **Purpose:** Prevent accidents caused by drowsy driving, reducing casualties and traffic congestion by detecting driver drowsiness in real-time.  
- **Objective:** Develop a real-time drowsy driving detection system.  

## **3. Project Details**  
- **Review of Previous Studies:** Examined various datasets and modeling techniques for drowsy driving detection.  
- **Topics:**  
  1. Development of a state detection model using time-series analysis of driver facial coordinates.  
  2. Development of a drowsiness detection model using CNN on eye image data.  

| Sub-topic | Data | Key Modeling Techniques |  
|-----------|------|------------------------|  
| 1 | Driver facial images | LSTM time-series analysis, FCN multi-class classification |  
| 2 | Open/closed eye images | CNN, FCN binary classification |  

## **4. Team Members and Responsibilities**  

| Sub-topic | Team Member | Responsibilities |  
|-----------|------------|------------------|  
| 1 | Kim Se-chan | Data preprocessing, training data creation, model training, model implementation and testing, presentation |  
| 1 | Ha Seung-joo | Data preprocessing, training data creation, model training, model implementation and testing, report writing |  
| 2 | Kim Moon-seon | Data collection, preprocessing, model design, training, evaluation, detection system development |  
| 2 | Lee Sung-jae | Data collection, preprocessing, model design, training, evaluation, detection system development, presentation |  

## **5. Comparison of the Two Models**  

### **1. LSTM-based state detection using time-series analysis of driver facial coordinates**  
- **Advantages:** Predicts drowsiness by analyzing the driver’s state over time, allowing early detection.  
- **Disadvantages:** Has a **4.8-second delay in inference**, preventing immediate action in case of drowsiness.  

### **2. CNN-based drowsiness detection using eye image data**  
- **Advantages:** **High performance** and enables **real-time inference**, allowing immediate response to prevent accidents.  
- **Disadvantages:** Cannot detect drowsiness if the driver wears sunglasses or other accessories that obstruct the eyes.  

## **6. Deliverables**  

### **Sub-project 1 - State detection using time-series analysis of driver facial coordinates**  
- [Modeling technique report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/1_modeling_report.md)  
- [Test design report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/2_test_report.md)
- [Process review report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/3_process_report.md)

### **Sub-project 2 - Drowsiness detection using CNN on eye image data**  
- [Modeling technique report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/1_modeling_report.md) 
- [Test design report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/2_test_report.md)
- [Process review report](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/3_process_report.md)
