# 테스트 설계 보고서

## 1. 모델 평가 기준
    - 정량 평가
        
        정확도, Loss(Cross Entropy Loss), confusion matrix
        precision, recall, f1 score

        
    - 정성 평가
        
        실시간 영상을 입력 받아 운전자의 졸음 감지 테스트
        
    - 처리 속도 (추론 시간, 학습 시간)
      
## 2. 테스트 환경

    - CPU
  
      
## 3. 테스트 결과

### 1. 하이퍼파라미터
        Hyperparameters:
        EPOCHS: 1000
        LR: 0.001
        INPUT_SIZE: 136
        HIDDEN_SIZE: 5
        NUM_LAYERS: 2
        BIDIRECTIONAL: True
        DROPOUT_RATE: 0.2

### 1. 정량 평가

   1. Train, Valid set

   - Epoch 191 에서 Early Stopping
     -  Train Loss: 0.3305
     -  Train Accuracy: 0.8718
     - Validation Loss: 0.3910
     -  Validation Accuracy: 0.8493
    - 학습 시간 : 1324.184초 (약 22분)  - 191epoch에서 earlystopping 

        ![training_results_20240621_193035](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/9fef6195-be17-429d-8eaf-55a80fb9aaa9)
      
3. Test 검증 

   - Test Loss :  0.4016
   - Test Accuracy : 0.8410
     
    - Confusion Matrix
        - ![image](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/1ffd2367-c3d9-4dd0-aafd-f68b6a421e63)
    - Classification Report
        - ![image](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/b2ddd6fc-b570-448d-ad3b-6c9d27f1c905)


### 2. 정성 평가
- 실시간 졸음 추론 모델 개발 및 시연  

