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

# 딥러닝 활용 졸음운전 실시간 감지 모델 개발

## 1. 주제

딥러닝을 활용한 졸음운전 실시간 감지 

## 2. 프로젝트 목적 및 목표

- 목적 : 졸음운전 사고로 인해 인명피해와 교통 혼잡 문제를 막기 위해 운전 중 졸음 상태를 실시간으로 감지해 사고를 예방
- 목표 : 실시간 졸음 운전 감지 시스템 개발

## 3. 세부 프로젝트  
- 선행 연구 검토 : 졸음운전 감지 모델 개발을 위한 다양한 데이터셋, 모델링 기법 고려
- **주제**
  1. 운전자 얼굴 좌표의 시계열 분석을 통한 상태 파악 모델 개발
  2. 눈 이미지 데이터의 CNN 활용한 졸음 감지 모델 개발
  
|세부주제|데이터|주요 모델링 기법|
|--|------|------|
|1|운전자 얼굴이미지|LSTM 시계열 분석, FCN 다중분류|
|2|감은 눈/뜬 눈 이미지|CNN, FCN 이진분류|
 
## 4. 팀원과 담당업무 
|세부주제|팀원|담당업무|
|--|------|------|
|1|김세찬|데이터 전처리 및 학습데이터 생성, 모델 학습, 모델 적용 및 테스트, 발표|
|1|하승주|데이터 전처리 및 학습데이터 생성, 모델 학습, 모델 적용 및 테스트, 보고서 작성|
|2|김문선|데이터 수집, 전처리, 모델 설계, 학습, 평가, 감지 시스템 개발|
|2|이성재|데이터 수집, 전처리, 모델 설계, 학습, 평가, 감지 시스템 개발|

## 5. 세부 프로젝트 두 모델의 장단점 비교
  
1. LSTM 활용 운전자 얼굴 좌표의 시계열 분석을 통한 상태 파악
    - 장점 : 운전자의 상태를 시계열 분석으로 파악해 졸음을 예측하고 졸음운전을 예방할 수 있음
    - 단점 : 추론에 4.8초의 delay가 있어 졸음 시에 즉각 조치 불가 

2. 눈 이미지 데이터 CNN 활용한 졸음 감지 모델 개발
      - 장점 : 성능우수, 실시간 추론을 통한 즉각 조치 가능
         -> 졸음 운전이 발생했을 때 사고 방지에 도움
      - 단점 : 선글라스 등올 눈을 가린 경우 졸음 탐지 불가


## 6. 산출물 
- 세부 프로젝트 1 - 운전자 얼굴 좌표의 시계열 분석을 통한 상태 파악
  - [모델링 기법 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/1_modeling_report.md)
  - [테스트 설계 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/2_test_report.md)
  - [프로세스 검토 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project1/3_process_report.md)
- 세부 프로젝트 2 - 눈 이미지 데이터 CNN 활용한 졸음 감지 모델 개발
  - [모델링 기법 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/1_modeling_report.md)
  - [테스트 설계 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/2_test_report.md)
  - [프로세스 검토 보고서](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/blob/main/Reports/project2/3_process_report.md)

